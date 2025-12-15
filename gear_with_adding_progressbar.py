import sys
import multiprocessing
import math
import time
import pandas as pd

from PySide6.QtWidgets import QApplication, QMainWindow, QProgressBar
from PySide6.QtCore import QThread, Signal, Slot, QTimer
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QProgressBar
from PySide6.QtCore import Qt
from resources.main_window import Ui_main_window

class LoadingDialog(QDialog):
    finished_signal = Signal()
    update_text_signal = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setModal(True)
        self.setWindowTitle("Подождите...")

        layout = QVBoxLayout()
        self.label = QLabel("                           Идёт обработка...                          ", alignment=Qt.AlignCenter)
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)
        button_cancel = QPushButton("Отмена")
        button_cancel.clicked.connect(self.reject)

        layout.addWidget(self.label)
        layout.addWidget(self.progress_bar)
        layout.addWidget(button_cancel)
        self.setLayout(layout)

        self.update_text_signal.connect(self.update_text)

    def update_text(self, text):
        self.label.setText(text)
        # Если пришло финальное сообщение — запускаем задержку
        if text == "Процесс завершён!":
            self._delayed_close()

    def _delayed_close(self):
        """Закрываем диалог через 1.5 секунды"""
        QTimer.singleShot(1500, self.close)  # 1500 мс = 1.5 сек

    def closeEvent(self, event):
        self.finished_signal.emit()
        event.accept()



class ProgressThread(QThread):
    finished_signal = Signal()
    update_text_signal = Signal(str)

    def __init__(self, event, queue):
        super().__init__()
        self.event = event
        self.queue = queue

    def run(self):
        while not self.event.is_set():
            try:
                status = self.queue.get(timeout=0.1)
                self.update_text_signal.emit(status)
            except:
                pass

        # Только отправляем финальный текст — НЕ эмитируем finished_signal здесь!
        self.update_text_signal.emit("Процесс завершён!")
        # finished_signal будет эмитирован при закрытии диалога (через closeEvent)


def run_cadquery(event, queue, params):
    """Функция, выполняемая в отдельном процессе"""
    import cadquery as cq
    from cadquery import Workplane
    from cadquery.vis import show

    length, width, height, diameter, points_list = params
    # result = cq.Workplane("front").box(length, width, height)  # создаём простую призму
    # result = result.faces(">Z").workplane().hole(diameter)     # находим верхнюю грань и делаем отверстие
    # show(result)
    queue.put("Процесс запущен, идёт подготовка данных...")

    # pass
    """Функция предпросмотра файла шестерни"""
    def merge_close_points(points, tolerance=1e-4):
            # pass
            """
            Объединяет точки, расстояние между которыми меньше указанного порога.
            :param points: Список точек (кортежи (x, y)).
            :param tolerance: Максимальное расстояние для объединения точек.
            :return: Очищенный список точек.
            """
            merged_points = []
            for point in points:
                added = False
                for idx, existing_point in enumerate(merged_points):
                    distance = math.hypot(existing_point[0] - point[0], existing_point[1] - point[1])
                    if distance <= tolerance:
                        # Среднее арифметическое существующих координат
                        new_x = (existing_point[0] + point[0]) / 2
                        new_y = (existing_point[1] + point[1]) / 2
                        merged_points[idx] = (new_x, new_y)
                        added = True
                        break
                if not added:
                    merged_points.append(point)
            return merged_points
        
            # Применяем фильтрацию близких точек
    points_list_merged = merge_close_points(points_list)
    # Замыкание первой и последней точки
    points_list_merged += [tuple(points_list_merged[0])]

    # # Высота профиля
    # width = height
    # # Угол бэтта в радианах
    # betta=0.5
    # # Радиус делительной окружности
    # r_del=gear.r_del
    # # общий угол поворота на всю высоту (Угол проворота торцов друг относительно друга, в градусах)
    # total_rotation_angle = ((width*math.tan(betta))/(r_del))*(180/math.pi)
    total_rotation_angle=30
    # Создаем базовый профиль (контур)
    initial_profile = Workplane("XY").polyline(points_list_merged[:-1]).close()

    # Производим экструзию с поворотом
    final_shape = initial_profile.twistExtrude(height, total_rotation_angle)
    # Отправляем статус перед отображением   
    queue.put("Подготовка завершена. Проверьте окна приложения — модель должна отобразиться.")


    event.set() 
    show(final_shape)


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.on_button_click)

        

    def on_button_click(self):
        length = self.ui.length_doubleSpinBox.value()
        width = self.ui.width_doubleSpinBox.value()
        height = self.ui.height_doubleSpinBox.value()
        diameter = 2 * self.ui.radius_doubleSpinBox.value()
        df = pd.read_csv('dots_for_gear.txt', sep=' ', header=None, names=['X', 'Y'])
        points_list = list(zip(df['X'], df['Y']))

        event = multiprocessing.Event()
        queue = multiprocessing.Queue()

        loading_dialog = LoadingDialog(parent=self)

        # Можно отключать 
        loading_dialog.show()

        # Создаём поток мониторинга
        self.progress_thread = ProgressThread(event, queue)
        self.progress_thread.update_text_signal.connect(self.update_status_label)
        # Подключаем сигналы:
        # - к диалогу (как было)
        self.progress_thread.update_text_signal.connect(
            loading_dialog.update_text_signal
        )
        # - к label_6 в главном окне (новое подключение)
        self.progress_thread.update_text_signal.connect(
            self.update_status_label
        )
        
        # Сигнал завершения
        self.progress_thread.finished_signal.connect(
            lambda: self.on_task_finished(process, loading_dialog)
        )

        process = multiprocessing.Process(
            target=run_cadquery,
            args=(event, queue, (length, width, height, diameter, points_list))
        )
        process.start()
        self.progress_thread.start()


    def update_status_label(self, text):
        """Обновляет label_6 в главном окне"""
        self.ui.label_6.setText(text)
        
        if text == "Процесс завершён!":
            self.ui.label_6.setStyleSheet("color: green;")
            # Запускаем таймер: через 1500 мс установим "Строка состояния"
            QTimer.singleShot(1500, self.reset_status_label)
        else:
            self.ui.label_6.setStyleSheet("")  # Сброс стиля

    def reset_status_label(self):
        """Сбрасывает label_6 к исходному тексту"""
        self.ui.label_6.setText("Строка состояния")
        self.ui.label_6.setStyleSheet("")  # Убираем зелёный цвет

    def on_task_finished(self, process, dialog):
        # 1. Ждём завершения процесса (с таймаутом)
        process.join(timeout=5)  # Ждать не более 5 секунд
        if process.is_alive():
            print("Процесс завис — принудительно завершаем")
            process.terminate()
            process.join()

        # 2. Закрываем диалог
        dialog.close()

        # 3. Останавливаем поток мониторинга (если ещё работает)
        if self.progress_thread.isRunning():
            self.progress_thread.quit()
            self.progress_thread.wait()

        print("Работа завершена!")

    # @Slot()
    # def stop_progress(self):
    #     """При получении сигнала завершения остановим прогресс-бар."""
    #     self.progress_bar.setRange(0, 1)      # устанавливаем диапазон минимального и максимального значений, так есть возможность остановить progressbar
    #     self.progress_bar.reset()              # и сбрасываем значение\
    #     print("stop_progress Завершили работу!")

if __name__ == "__main__":
    app = QApplication(sys.argv)           # Инициализация приложения
    window = MyWindow()              # Создаем экземпляр окна
    window.show()                    # Показываем окно
    sys.exit(app.exec())                     # Запускаем цикл обработки событий