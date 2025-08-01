import sys
import multiprocessing

from PySide6.QtWidgets import QApplication, QMainWindow

from resources.main_window import Ui_main_window

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_main_window()  # Создаем объект нашего интерфейса
        self.ui.setupUi(self)      # Устанавливаем наш интерфейс на главное окно

        self.ui.pushButton_2.clicked.connect(self.create_and_show)

    
    def create_and_show(self):
        '''Функция, выполняемая в отдельном процессе'''

        import cadquery as cq
        from cadquery.vis import show

        result = cq.Workplane("front").box(2, 3, 0.5)  # make a basic prism
        result = (
            result.faces(">Z").workplane().hole(1)
        )  # find the top-most face and make a hole

        show(result)


if __name__ == "__main__":
    app = QApplication([])           # Инициализация приложения
    window = MyWindow()              # Создаем экземпляр окна
    window.show()                    # Показываем окно
    app.exec()                       # Запускаем цикл обработки событий
    
    # p=multiprocessing.Process(target=create_and_show)
    # p.start()

    # p.join()

    # sys.exit(0)