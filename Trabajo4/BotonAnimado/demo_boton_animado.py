from PySide6.QtCore import QPoint, Qt, QSize
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QMainWindow, QPushButton
from boton_animado import BotonAnimado
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()       

        self.setWindowTitle("My App")

        self.button = BotonAnimado()

        self.setCentralWidget(self.button)




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()