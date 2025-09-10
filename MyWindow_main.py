import sys
import multiprocessing

from PySide6.QtWidgets import QApplication, QMainWindow

from resources.main_window import Ui_main_window
from multiproces_box_with_hole import MyWindow
print("box Главного окна")

class MyWindow_main(QMainWindow):
    def __init__(self):
        super(MyWindow_main, self).__init__()
        self.ui = Ui_main_window()  # Создаем объект нашего интерфейса
        self.ui.setupUi(self)      # Устанавливаем наш интерфейс на главное окно
        print("MyWindow_main Функция инит первого окна")
        self.setWindowTitle("Стартовое окно")
        self.ui.pushButton.setText("Кнопка без действий")
        self.ui.pushButton_2.setText("Запуск нового окна для предпросмотра")
  
        
        # Создаем список для хранения открытых окон
        self.open_windows = []
        
        # Классы окон модулей приложения, при добавлении нового окна нужно сюда добавлять классы       
        self.classes = {
            "MyWindow": MyWindow,
        }
        
        self.ui.pushButton_2.clicked.connect(lambda: self.open_sliders_window(self.classes["MyWindow"])) # При нажатии на кнопку запускается окно построения шестерни
              
    def open_sliders_window(self, class_name, **kwargs):
        self.sliders_window = class_name(**kwargs)
        self.sliders_window.show()
        # Сохраняем ссылку на новое окно в списке
        self.open_windows.append(self.sliders_window)
        print("open_sliders_window Функция открытия нового окна")    


if __name__ == "__main__":
    app = QApplication(sys.argv)           # Инициализация приложения
    window = MyWindow_main()              # Создаем экземпляр окна
    window.show()                    # Показываем окно
    sys.exit(app.exec())                     # Запускаем цикл обработки событий