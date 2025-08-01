import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from resources.main_window import Ui_main_window

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_main_window()  # Создаем объект нашего интерфейса
        self.ui.setupUi(self)      # Устанавливаем наш интерфейс на главное окно


if __name__ == "__main__":
    app = QApplication([])           # Инициализация приложения
    window = MyWindow()              # Создаем экземпляр окна
    window.show()                    # Показываем окно
    app.exec()                       # Запускаем цикл обработки событий