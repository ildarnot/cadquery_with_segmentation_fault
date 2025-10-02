import sys
import multiprocessing
from PySide6.QtWidgets import QApplication, QMainWindow, QProgressBar
from PySide6.QtCore import QThread, Signal, Slot
from resources.main_window import Ui_main_window
import time

print("box Дочернего окна")

class ProgressThread(QThread):
    finished_signal = Signal()  # Сигнал завершения

    def __init__(self, event):
        super().__init__()
        self.event = event  # Подписываемся на событие завершения внешнего процесса

    @Slot()
    def run(self):
        while not self.event.is_set():
            time.sleep(0.1)  # Проверяем каждые 100 мс статус завершения
        self.finished_signal.emit()  # Сообщаем главному окну о завершении работы

def run_cadquery(event, params):
    """
    Выполняемый процесс. По окончании вызывает событие event.
    """
    import cadquery as cq
    from cadquery.vis import show

    length, width, height, diameter = params
    result = cq.Workplane("front").box(length, width, height)  # создаём простую призму
    result = result.faces(">Z").workplane().hole(diameter)     # добавляем отверстие сверху
    event.set() 
    show(result)                                               # визуализируем деталь
    # event.set()                                                # Устанавливаем флаг завершения
    print("run_cadquery Функция самого подпроцесса")

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_main_window()                              # Загружаем UI главного окна
        self.ui.setupUi(self)                                  # Настраиваем интерфейс
        self.ui.pushButton_2.clicked.connect(self.on_button_click)
        self.ui.pushButton.setText("0")
        print("MyWindow Функция инициализации дочернего окна")

        # Добавляем ProgressBar в дочернее окно
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(10, 10, 300, 20)

    def on_button_click(self):
        """Обработчик события нажатия кнопки."""
        # Получаем текущие значения из элементов управления
        length = self.ui.length_doubleSpinBox.value()
        width = self.ui.width_doubleSpinBox.value()
        height = self.ui.height_doubleSpinBox.value()
        diameter = 2 * self.ui.radius_doubleSpinBox.value()

        # Используем многопоточность и процессы
        event = multiprocessing.Event()                        # Объект синхронизации процессов
        self.progress_bar.setRange(0, 0)                       # Переходим в режим неопределенного ожидания
        process = multiprocessing.Process(
            target=run_cadquery,                               # Задача выполняется здесь
            args=(event, (length, width, height, diameter)))   # Аргументы: сам объект события + параметры детали
        process.start()

        # Ждём завершения работы в отдельном потоке
        self.progress_thread = ProgressThread(event)
        self.progress_thread.finished_signal.connect(self.stop_progress)
        self.progress_thread.start()

        print("on_button_click Функция запуска нового процесса")

    @Slot()
    def stop_progress(self):
        """При получении сигнала завершения остановим прогресс-бар."""
        # self.progress_bar.setRange(0, 100)                     # Убираем неопределенность
        # self.progress_bar.setValue(100)                        # Прогресс закончен
        self.progress_bar.setRange(0, 1)      # устанавливаем диапазон минимального и максимального значений, так есть возможность остановить progressbar
        self.progress_bar.reset()              # и сбрасываем значение
        print("stop_progress Завершили работу!")

if __name__ == "__main__":
    app = QApplication(sys.argv)          # Инициализация приложения
    window = MyWindow()                   # Экземпляр класса окна
    window.show()                         # Отображаем окно
    sys.exit(app.exec())