from PyQt6.QtWidgets import (QApplication, QTableWidget, QWidget, QGridLayout, QLabel, 
                            QLineEdit, QTableWidgetItem, QMessageBox, QFormLayout, QDialog, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QDateEdit)
from PyQt6.QtCore import Qt
import json

def carregar_contatos():
    try:
        with open("interfaces_graficas/atividade_avaliativa_06-06/contatos.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            return [Contatos(**contato) for contato in dados]
        
    except FileNotFoundError:
        with open("interfaces_graficas/atividade_avaliativa_06-06/contatos.json", "w", encoding="utf-8") as arquivo:
            json.dump([], arquivo)
        return []
    

def salvar_contatos(contatos):
    contatos_como_dict = [
        {
            "nome": c.nome,
            "telefone": c.telefone,
            "email": c.email,
            "tipo": c.tipo
        }
        for c in contatos
    ]
    with open("contatos.json", "w", encoding="utf-8") as arquivo:
        json.dump(contatos_como_dict, arquivo, indent=4, ensure_ascii=False)




class Gerenciador_Contatos(QWidget):
    def __init__(self):
        super().__init__()

        self.contatos = carregar_contatos()

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

        self.input_filtro.addItems(["Todos", "Família", "Trabalho", "Amigos"])

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

        self.input_busca.textChanged.connect(self.atualizar_tabela)
        self.input_filtro.currentIndexChanged.connect(self.atualizar_tabela)
        
        self.botao_novo_contato.clicked.connect(self.adicionar)
        self.botao_editar_contato.clicked.connect(self.editar)
        self.botao_remover_contato.clicked.connect(self.excluir)

        self.atualizar_tabela()

    def atualizar_tabela(self):
        self.table.setRowCount(0)
        termo_busca = self.input_busca.text().lower()
        filtro = self.input_filtro.currentText()
        for contato in self.contatos:
            if termo_busca and termo_busca not in contato.nome.lower():
                continue

            if filtro != "Todos" and contato.tipo != filtro:
                continue

            linha_contato = self.table.rowCount()
            self.table.insertRow(linha_contato)
            self.table.setItem(linha_contato, 0, QTableWidgetItem(contato.nome))
            self.table.setItem(linha_contato, 1, QTableWidgetItem(contato.telefone))
            self.table.setItem(linha_contato, 2, QTableWidgetItem(contato.email))
            self.table.setItem(linha_contato, 3, QTableWidgetItem(contato.tipo))

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

        novo_contato = [contato]

        def salvar():
            nome = input_nome.text().strip()
            telefone = input_telefone.text().strip()
            email = input_email.text().strip()
            tipo = input_tipo.currentText()           

            if not nome:
                QMessageBox.warning(dialogo_contato, "ERRO", "Nome não pode estar vazio")
            
            else:

                if novo_contato[0]:
                    novo_contato[0].atualizar_contato(nome, telefone, email, tipo)
                else:
                    novo_contato[0] = Contatos(nome, telefone, email, tipo)
        
                dialogo_contato.accept()


        botao_salvar.clicked.connect(salvar)

        if dialogo_contato.exec():
            return novo_contato[0]
        
        return None
    
    def adicionar(self):
        contato_novo = self.abrir_janela_contato()

        if contato_novo:
            self.contatos.append(contato_novo)
            salvar_contatos(self.contatos)
            self.atualizar_tabela()

    def editar(self):
        linha_contato = self.table.currentRow()
        if linha_contato < 0:
            QMessageBox.warning(Gerenciador_Contatos(), "Erro", "Selecione um contato para editar.")
            return           
        
        contato_atual = self.contatos[linha_contato]
        contato_atual = self.abrir_janela_contato(contato_atual)
        
        if contato_atual:
            self.contatos[linha_contato] = contato_atual
            salvar_contatos(self.contatos)
            self.atualizar_tabela()
    
    def excluir(self):
        linha_contato = self.table.currentRow()

        if linha_contato < 0:
            QMessageBox.warning(Gerenciador_Contatos(), "Erro", "Selecione um contato para excluir.")
            return
        
        resposta = QMessageBox.question(Gerenciador_Contatos(), "Confirmar", "Deseja realmente excluir este contato?")
        if resposta == QMessageBox.StandardButton.Yes:
            self.contatos.pop(linha_contato)
            salvar_contatos(self.contatos)
            self.atualizar_tabela()


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