from PyQt6.QtWidgets import (QApplication, QTableWidget, QWidget, QGridLayout, QLabel, 
                            QLineEdit, QMessageBox, QFormLayout, QDialog, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QDateEdit)
from PyQt6.QtCore import Qt

class Gerenciador_Contatos(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciador de Contatos")
        self.setGeometry(100, 100, 500, 300)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Nome", "Telefone", "Email", "Tipo"])

        self.lbl_busca = QLabel("Buscar:",  self)
        self.input_busca = QLineEdit()

        self.layout_busca = QHBoxLayout()
        self.layout_busca.addWidget(self.lbl_busca)
        self.layout_busca.addWidget(self.input_busca)

        self.lbl_filtro = QLabel("Filtro:", self)
        self.input_filtro = QComboBox()

        self.input_filtro.addItems(["Família", "Trabalho", "Amigos"])

        self.layout_filtro = QHBoxLayout()
        self.layout_filtro.addWidget(self.lbl_filtro)
        self.layout_filtro.addWidget(self.input_filtro)

        self.botao_novo_contato = QPushButton("Novo Contato", self)
        self.botao_editar_contato = QPushButton("Editar Contato", self)
        self.botao_remover_contato = QPushButton("Remover Contato", self)

        self.layout_botoes = QHBoxLayout()
        self.layout_botoes.addWidget(self.botao_novo_contato)
        self.layout_botoes.addWidget(self.botao_editar_contato)
        self.layout_botoes.addWidget(self.botao_remover_contato)

        self.layout_principal = QVBoxLayout()
        self.layout_principal.addWidget(self.table)
        self.layout_principal.addLayout(self.layout_busca)
        self.layout_principal.addLayout(self.layout_filtro)
        self.layout_principal.addLayout(self.layout_botoes)

        self.setLayout(self.layout_principal)
        
        self.botao_novo_contato.clicked.connect(self.abrir_janela_contato)
        self.botao_editar_contato.clicked.connect(self.abrir_janela_contato)

    def abrir_janela_contato(self, contato=None):
        dialogo_contato = QDialog()
        dialogo_contato.setWindowTitle("Editar Contato" if contato else "Adicionar Contato")

        input_nome = QLineEdit()
        input_telefone = QLineEdit()
        input_email = QLineEdit()
        input_tipo = QComboBox()
        input_tipo.addItems(["Família", "Trabalho", "Amigos"])

        if contato: 
            input_nome.setText(contato.nome)
            input_telefone.setText(contato.telefone)
            input_email.setText(contato.email)
            input_tipo.setCurrentText(contato.tipo)

        formulario = QFormLayout()
        formulario.addRow("Nome:", input_nome)
        formulario.addRow("Telefone:", input_telefone)
        formulario.addRow("Email:", input_email)
        formulario.addRow("Tipo:", input_tipo)

        botao_salvar = QPushButton("Salvar")

        layout_janela_contato = QVBoxLayout()
        layout_janela_contato.addLayout(formulario)
        layout_janela_contato.addWidget(botao_salvar)
        dialogo_contato.setLayout(layout_janela_contato)

        def salvar():
            nome = input_nome.text().strip()
            telefone = input_telefone.text().strip()
            email = input_email.text().strip()
            tipo = input_tipo.currentText()           

            if not nome:
                QMessageBox.warning(dialogo_contato, "ERRO", "Nome não pode estar vazio")
            
            else:
                dialogo_contato.accept()

                if contato:
                    contato.atualizar_contato(input_nome, input_telefone, input_email, input_tipo)
                else:
                    contato = Contatos(nome, telefone, email, tipo)
            
        botao_salvar.clicked.connect(salvar)

        if dialogo_contato.exec():
            return contato
        
        return None
    
    def adicionar(self):
        contato_novo = self.abrir_janela_contato()

        # if contato_novo:
            #

    def editar(self):
        contato = self.table.currentRow()
class Contatos():
    def __init__(self, nome, telefone, email, tipo):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.tipo = tipo

    def atualizar_contato(self, nome, telefone, email, tipo):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.tipo = tipo



app = QApplication([])
form = Gerenciador_Contatos()
form.show()
app.exec()