import sys
import multiprocessing
import math
import pandas as pd

from PySide6.QtWidgets import QApplication, QMainWindow

from resources.main_window import Ui_main_window

def run_cadquery(params):
    """Функция, выполняемая в отдельном процессе"""
    import cadquery as cq
    from cadquery import Workplane
    from cadquery.vis import show

    length, width, height, diameter, points_list = params
    # result = cq.Workplane("front").box(length, width, height)  # создаём простую призму
    # result = result.faces(">Z").workplane().hole(diameter)     # находим верхнюю грань и делаем отверстие
    # show(result)

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

    show(final_shape)

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_main_window()  # Создаем объект нашего интерфейса
        self.ui.setupUi(self)      # Устанавливаем наш интерфейс на главное окно
        self.ui.pushButton_2.clicked.connect(self.on_button_click)

    def on_button_click(self):
        """Обработчик события нажатия кнопки."""
        # Получаем актуальные значения из UI
        length = self.ui.length_doubleSpinBox.value()
        width = self.ui.width_doubleSpinBox.value()
        height = self.ui.height_doubleSpinBox.value()
        diameter = 2 * self.ui.radius_doubleSpinBox.value()
        # Читаем файл с точками
        df = pd.read_csv('dots_for_gear.txt', sep=' ', header=None, names=['X', 'Y'])

        # Получаем список точек
        points_list = list(zip(df['X'], df['Y']))

        # Передаем параметры в отдельный процесс
        process = multiprocessing.Process(target=run_cadquery, args=((length, width, height, diameter, points_list),))
        process.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)           # Инициализация приложения
    window = MyWindow()              # Создаем экземпляр окна
    window.show()                    # Показываем окно
    sys.exit(app.exec())                     # Запускаем цикл обработки событий