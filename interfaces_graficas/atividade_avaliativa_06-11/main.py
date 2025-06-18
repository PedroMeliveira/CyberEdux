import requests
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPixmap

class Pexel(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("interfaces_graficas/atividade_avaliativa_06-11/teste.ui")

if __name__ == "__main__":
    app = QApplication([])
    janela = Pexel()
    janela.show()
    app.exec()