from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


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

# EXERCICIO 2

# class Janela(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Botão A e Botão B")
#         self.setGeometry(500, 300, 250, 150)

#         self.label = QLabel("Nenhum Botão pressionado", self)
#         self.botaoA = QPushButton("Botão A", self)
#         self.botaoB = QPushButton("Botão B", self)

#         layout = QVBoxLayout()
#         layout.addWidget(self.label)

#         layout.addWidget(self.botaoA)
#         layout.addWidget(self.botaoB)
        
#         self.setLayout(layout)

#         self.botaoA.clicked.connect(self.botaoA_clicked)
#         self.botaoB.clicked.connect(self.botaoB_clicked)


#     def botaoA_clicked(self):
#         self.label.setText("Botão A foi pressionado!")

    
#     def botaoB_clicked(self):
#         self.label.setText("Botão B foi pressionado!")
      
      
# EXERCICIO 3

# class Janela(QWidget):
#     def __init__(self):
#         super().__init__()
#         global num
#         self.num = 0
        
#         self.setWindowTitle("Contador")
#         self.setGeometry(500, 300, 250, 150)

#         self.label = QLabel(str(self.num), self)
#         self.label.setStyleSheet(f"font-size: 48px; color: white;")
#         self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        
#         self.botaoAumentar = QPushButton("+", self)
#         self.botaoAumentar.setStyleSheet("color: green")
#         self.botaoDiminuir = QPushButton("-", self)
#         self.botaoDiminuir.setStyleSheet("color: red")

#         layout = QVBoxLayout()
#         layout.addWidget(self.label)

#         layout.addWidget(self.botaoAumentar)
#         layout.addWidget(self.botaoDiminuir)
        
#         self.setLayout(layout)

#         self.botaoAumentar.clicked.connect(self.botaoAumentar_clicked)
#         self.botaoDiminuir.clicked.connect(self.botaoDiminuir_clicked)
        
        
#     def define_cor(self):
#         global num
#         if self.num < 0:
#             self.label.setStyleSheet(f"font-size: 48px; color: red;")
            
#         elif self.num == 0:
#             self.label.setStyleSheet(f"font-size: 48px; color: white;")
            
#         else:
#             self.label.setStyleSheet(f"font-size: 48px; color: green;")
        
#     def botaoAumentar_clicked(self):
#         global num
#         self.num += 1
#         self.label.setText(str(self.num))
#         self.define_cor()
        
#     def botaoDiminuir_clicked(self):
#         global num
#         self.num -= 1
#         self.label.setText(str(self.num))
#         self.define_cor()
        
        
# EXERCICIO 4

# class Janela(QWidget):
#     def __init__(self):
#         super().__init__()
        
#         self.setWindowTitle("Visivel")
#         self.setGeometry(500, 300, 250, 150)
        
#         self.label = QLabel("Bom dia!")
#         self.label.setStyleSheet("font-size: 48px; color: pink")
#         self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
#         self.botao = QPushButton("Alterar visibilidade", self)
#         self.botao.setStyleSheet("color: pink")
        
#         layout = QVBoxLayout()
#         layout.addWidget(self.label)
#         layout.addWidget(self.botao)
        
#         self.setLayout(layout)
        
#         self.botao.clicked.connect(self.botao_clicked)
        
#     def botao_clicked(self):
#         self.label.setVisible(not self.label.isVisible())
        
        
# DESAFIO

# class Janela(QWidget):
#     def __init__(self):
#         super().__init__()
#         global votos_A, votos_B
#         self.votos_A = self.votos_B = 0
        
        
#         self.setWindowTitle("Do the éli!")
#         self.setGeometry(500, 300, 400, 400)
#         self.
        
    
# if __name__ == "__main__":
#     app = QApplication([])
#     janela = Janela()
#     janela.show()
#     app.exec()