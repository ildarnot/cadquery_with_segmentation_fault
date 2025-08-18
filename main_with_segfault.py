import sys
import cadquery as cq
from cadquery.vis import show

from PySide6.QtWidgets import QApplication, QMainWindow

from resources.main_window import Ui_main_window

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_main_window()  # Создаем объект нашего интерфейса
        self.ui.setupUi(self)      # Устанавливаем наш интерфейс на главное окно
        self.ui.pushButton_2.clicked.connect(self.on_button_click)

    def on_button_click(self):
        """Обработчик события нажатия кнопки."""
        # получаем актуальные значения из UI
        length = self.ui.length_doubleSpinBox.value()
        width = self.ui.width_doubleSpinBox.value()
        height = self.ui.height_doubleSpinBox.value()
        diameter = 2 * self.ui.radius_doubleSpinBox.value()

        # передаем параметры в дочерний процесс
        result = cq.Workplane("front").box(length, width, height)  # создаём простую призму
        result = result.faces(">Z").workplane().hole(diameter)     # находим верхнюю грань и делаем отверстие

        show(result)

if __name__ == "__main__":
    app = QApplication([])           # Инициализация приложения
    window = MyWindow()              # Создаем экземпляр окна
    window.show()                    # Показываем окно
    app.exec()                       # Запускаем цикл обработки событий