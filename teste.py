import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QCheckBox
)


class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Checkboxes ao lado da tabela")

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(2)
        self.tabela.setHorizontalHeaderLabels(["Nome", "Idade"])

        self.checkboxes = []  # Lista para armazenar os QCheckBox
        self.layout_checkboxes = QVBoxLayout()

        self.botao_adicionar = QPushButton("Adicionar Linha")
        self.botao_adicionar.clicked.connect(self.adicionar_linha)

        # Layouts principais
        layout_tabela = QVBoxLayout()
        layout_tabela.addWidget(self.tabela)
        layout_tabela.addWidget(self.botao_adicionar)

        layout_geral = QHBoxLayout()
        layout_geral.addLayout(self.layout_checkboxes)  # coluna de checkboxes
        layout_geral.addLayout(layout_tabela)

        container = QWidget()
        container.setLayout(layout_geral)
        self.setCentralWidget(container)

    def adicionar_linha(self):
        linha = self.tabela.rowCount()
        self.tabela.insertRow(linha)

        # Adiciona dados à tabela
        self.tabela.setItem(linha, 0, QTableWidgetItem(f"Pessoa {linha + 1}"))
        self.tabela.setItem(linha, 1, QTableWidgetItem("0"))

        # Cria checkbox correspondente
        checkbox = QCheckBox()
        self.layout_checkboxes.addWidget(checkbox)
        self.checkboxes.append(checkbox)

    def obter_selecionados(self):
        for i, checkbox in enumerate(self.checkboxes):
            if checkbox.isChecked():
                print(f"Linha {i} selecionada")


# Executa o app
app = QApplication(sys.argv)
janela = JanelaPrincipal()
janela.show()
sys.exit(app.exec())
