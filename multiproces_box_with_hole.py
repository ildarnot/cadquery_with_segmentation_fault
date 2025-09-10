import sys
import multiprocessing

from PySide6.QtWidgets import QApplication, QMainWindow

from resources.main_window import Ui_main_window
print("box Дочернего окна")
def run_cadquery(params):
    """Функция, выполняемая в отдельном процессе"""
    import cadquery as cq
    from cadquery.vis import show

    length, width, height, diameter = params
    result = cq.Workplane("front").box(length, width, height)  # создаём простую призму
    result = result.faces(">Z").workplane().hole(diameter)     # находим верхнюю грань и делаем отверстие
    show(result)
    print("run_cadquery Функция самого подпроцесса")        


# class MyWindow_main(QMainWindow):
#     def __init__(self):
#         super(MyWindow_main, self).__init__()
#         self.ui = Ui_main_window()  # Создаем объект нашего интерфейса
#         self.ui.setupUi(self)      # Устанавливаем наш интерфейс на главное окно
        
        
#         # Создаем список для хранения открытых окон
#         self.open_windows = []
        
#         # Классы окон модулей приложения, при добавлении нового окна нужно сюда добавлять классы       
#         self.classes = {
#             "MyWindow": MyWindow,
#         }
        
#         self.ui.pushButton_2.clicked.connect(lambda: self.open_sliders_window(self.classes["MyWindow"])) # При нажатии на кнопку запускается окно построения шестерни
              
#     def open_sliders_window(self, class_name, **kwargs):
#         self.sliders_window = class_name(**kwargs)
#         self.sliders_window.show()
#         # Сохраняем ссылку на новое окно в списке
#         self.open_windows.append(self.sliders_window)    

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_main_window()  # Создаем объект нашего интерфейса
        self.ui.setupUi(self)      # Устанавливаем наш интерфейс на главное окно
        self.ui.pushButton_2.clicked.connect(self.on_button_click)
        self.ui.pushButton.setText("0")
        print("MyWindow Функция инит дочернего окна")        


    def on_button_click(self):
        """Обработчик события нажатия кнопки."""
        # Получаем актуальные значения из UI
        length = self.ui.length_doubleSpinBox.value()
        width = self.ui.width_doubleSpinBox.value()
        height = self.ui.height_doubleSpinBox.value()
        diameter = 2 * self.ui.radius_doubleSpinBox.value()

        # Передаем параметры в отдельный процесс
        process = multiprocessing.Process(target=run_cadquery, args=((length, width, height, diameter),))
        process.start()
        print("on_button_click Функция запуска нового процесса")        


if __name__ == "__main__":
    app = QApplication(sys.argv)           # Инициализация приложения
    # window = MyWindow_main()              # Создаем экземпляр окна
    # window.show()                    # Показываем окно
    # sys.exit(app.exec())                     # Запускаем цикл обработки событий