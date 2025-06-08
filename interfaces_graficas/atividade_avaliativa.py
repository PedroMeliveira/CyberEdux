from PyQt6.QtWidgets import (QApplication, QTableWidget, QWidget, QGridLayout, QLabel, 
                            QLineEdit, QVBoxLayout, QComboBox, QPushButton, QDateEdit)
from PyQt6.QtCore import Qt

class Gerenciador_Contatos(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciador de Contatos")
        self.setGeometry(100, 100, 500, 300)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Nome", "Telefone", "Email", "Tipo"])



        layout = QVBoxLayout()
        layout.addWidget(self.table)

        self.setLayout(layout)

app = QApplication([])
form = Gerenciador_Contatos()
form.show()
app.exec()