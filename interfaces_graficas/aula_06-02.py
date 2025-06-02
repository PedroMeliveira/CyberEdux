from PyQt6.QtWidgets import *


# class Janela(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Botão e Label")
#         self.setGeometry(100, 100, 300, 200)

#         self.label = QLabel("Texto Original", self)
#         self.botao = QPushButton("Clique para Mudar", self)

#         layout = QVBoxLayout()
#         layout.addWidget(self.label)
#         layout.addWidget(self.botao)
#         self.setLayout(layout)

#         self.botao.clicked.connect(self.atualizar_label)

#     def atualizar_label(self):
#         self.label.setText("Texto Alterado!")


# if __name__ == "__main__":
#     app = QApplication([])
#     janela = Janela()
#     janela.show()
#     app.exec()


# EXERCICIO 1

# class Janela(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Desligado e Ligado")
#         self.setGeometry(100, 100, 300, 200)

#         self.label = QLabel("Desligado", self)
#         self.botao = QPushButton("Mudar o estado", self)

#         layout = QVBoxLayout()
#         layout.addWidget(self.label)
#         layout.addWidget(self.botao)
#         self.setLayout(layout)

#         self.botao.clicked.connect(self.atualizar_label)

#     def atualizar_label(self):
#         if self.label.text() == "Desligado":
#             self.label.setText("Ligado")

#         else:
#             self.label.setText("Desligado")

# if __name__ == "__main__":
#     app = QApplication([])
#     janela = Janela()
#     janela.show()
#     app.exec()

# EXERCICIO 2

class Janela()
