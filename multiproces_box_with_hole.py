import sys
import multiprocessing

from PySide6.QtWidgets import QApplication, QMainWindow, QProgressBar
from PySide6.QtCore import QThread, Signal

from resources.main_window import Ui_main_window
print("box Дочернего окна")

class ProgressThread(QThread):
    progress_signal = Signal(int)
    
    def __init__(self, params):
        super().__init__()
        self.params = params
        
    def run(self):
        # Имитация прогресса (в реальном коде нужно добавить реальную логику)
        for i in range(101):
            self.progress_signal.emit(i)
            # Здесь можно добавить реальную логику расчета
            # Например, разбиение процесса на этапы
            # И отправку прогресса после каждого этапа
            
        run_cadquery(self.params)

def run_cadquery(params):
    """Функция, выполняемая в отдельном процессе"""
    import cadquery as cq
    from cadquery.vis import show

    length, width, height, diameter = params
    result = cq.Workplane("front").box(length, width, height)  # создаём простую призму
    result = result.faces(">Z").workplane().hole(diameter)     # находим верхнюю грань и делаем отверстие
    show(result)
    print("run_cadquery Функция самого подпроцесса")        

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_main_window()  # Создаем объект нашего интерфейса
        self.ui.setupUi(self)      # Устанавливаем наш интерфейс на главное окно
        self.ui.pushButton_2.clicked.connect(self.on_button_click)
        self.ui.pushButton.setText("0")
        print("MyWindow Функция инит дочернего окна")     

        # Добавляем ProgressBar в дочернее окно
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(10, 10, 300, 20)
        self.progress_bar.setValue(0)   


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

        # Создаем и запускаем поток с прогрессом
        self.progress_thread = ProgressThread((length, width, height, diameter))
        self.progress_thread.progress_signal      


if __name__ == "__main__":
    app = QApplication(sys.argv)           # Инициализация приложения