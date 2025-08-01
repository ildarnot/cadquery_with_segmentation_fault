import sys
import multiprocessing

from PySide6.QtWidgets import QApplication, QMainWindow

from resources.main_window import Ui_main_window

def run_cadquery():
    """Функция, выполняемая в отдельном процессе"""
    import cadquery as cq
    from cadquery.vis import show

    result = cq.Workplane("front").box(2, 3, 0.5)  # создаём простую призму
    result = result.faces(">Z").workplane().hole(1)  # находим верхнюю грань и делаем отверстие

    show(result)

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_main_window()  # Создаем объект нашего интерфейса
        self.ui.setupUi(self)      # Устанавливаем наш интерфейс на главное окно

        self.ui.pushButton_2.clicked.connect(self.on_button_click)

    
    def on_button_click(self):
        """ Обработчик события нажатия кнопки. Запускает создание и визуализацию 3D-модели в отдельном процессе. """
        process = multiprocessing.Process(target=run_cadquery)
        process.start()
        process.join()  # дожидаемся окончания процесса (если хотите завершить синхронно)


if __name__ == "__main__":
    app = QApplication([])           # Инициализация приложения
    window = MyWindow()              # Создаем экземпляр окна
    window.show()                    # Показываем окно
    app.exec()                       # Запускаем цикл обработки событий
