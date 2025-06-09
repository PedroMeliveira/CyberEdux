import json
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QTableWidget, QTableWidgetItem, QMessageBox, QDialog, QFormLayout

def carregar_contatos():
    try:
        with open("contatos.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        with open("contatos.json", "w", encoding="utf-8") as arquivo:
            json.dump([], arquivo)
        return []

def salvar_contatos(contatos):
    with open("contatos.json", "w", encoding="utf-8") as arquivo:
        json.dump(contatos, arquivo, indent=4, ensure_ascii=False)

def abrir_formulario(janela, contato=None):
    dialogo = QDialog(janela)
    dialogo.setWindowTitle("Adicionar / Editar Contato")
    layout = QVBoxLayout()

    nome_input = QLineEdit()
    telefone_input = QLineEdit()
    email_input = QLineEdit()
    tipo_input = QComboBox()
    tipo_input.addItems(["Pessoal", "Profissional", "Outro"])

    if contato:
        nome_input.setText(contato["nome"])
        telefone_input.setText(contato["telefone"])
        email_input.setText(contato["email"])
        tipo_input.setCurrentText(contato["tipo"])

    formulario = QFormLayout()
    formulario.addRow("Nome:", nome_input)
    formulario.addRow("Telefone:", telefone_input)
    formulario.addRow("Email:", email_input)
    formulario.addRow("Tipo:", tipo_input)

    botao_salvar = QPushButton("Salvar")
    layout.addLayout(formulario)
    layout.addWidget(botao_salvar)
    dialogo.setLayout(layout)

    def salvar():
        nome = nome_input.text().strip()
        telefone = telefone_input.text().strip()
        email = email_input.text().strip()
        tipo = tipo_input.currentText()
        if not nome:
            QMessageBox.warning(dialogo, "Erro", "Nome não pode estar vazio.")
            return
        dialogo.accept()
        dialogo.resultado = {
            "nome": nome,
            "telefone": telefone,
            "email": email,
            "tipo": tipo
        }

    botao_salvar.clicked.connect(salvar)
    if dialogo.exec():
        return dialogo.resultado
    return None

def atualizar_tabela(tabela, contatos, filtro_nome, filtro_tipo):
    tabela.setRowCount(0)
    for contato in contatos:
        if filtro_nome and filtro_nome.lower() not in contato["nome"].lower():
            continue
        if filtro_tipo != "Todos" and contato["tipo"] != filtro_tipo:
            continue
        linha = tabela.rowCount()
        tabela.insertRow(linha)
        tabela.setItem(linha, 0, QTableWidgetItem(contato["nome"]))
        tabela.setItem(linha, 1, QTableWidgetItem(contato["telefone"]))
        tabela.setItem(linha, 2, QTableWidgetItem(contato["email"]))
        tabela.setItem(linha, 3, QTableWidgetItem(contato["tipo"]))

aplicativo = QApplication([])
janela = QWidget()
janela.setWindowTitle("Gerenciador de Contatos")
layout = QVBoxLayout(janela)

layout_filtros = QHBoxLayout()
entrada_busca = QLineEdit()
entrada_busca.setPlaceholderText("Buscar")
filtro_tipo = QComboBox()
filtro_tipo.addItems(["Todos", "Pessoal", "Profissional", "Outro"])
layout_filtros.addWidget(entrada_busca)
layout_filtros.addWidget(filtro_tipo)
layout.addLayout(layout_filtros)

tabela = QTableWidget(0, 4)
tabela.setHorizontalHeaderLabels(["Nome", "Telefone", "Email", "Tipo"])
tabela.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
layout.addWidget(tabela)

layout_botoes = QHBoxLayout()
botao_adicionar = QPushButton("Adicionar")
botao_editar = QPushButton("Editar")
botao_excluir = QPushButton("Excluir")
layout_botoes.addWidget(botao_adicionar)
layout_botoes.addWidget(botao_editar)
layout_botoes.addWidget(botao_excluir)
layout.addLayout(layout_botoes)

contatos = carregar_contatos()

def atualizar_interface():
    atualizar_tabela(tabela, contatos, entrada_busca.text(), filtro_tipo.currentText())

entrada_busca.textChanged.connect(atualizar_interface)
filtro_tipo.currentIndexChanged.connect(atualizar_interface)

def adicionar():
    novo = abrir_formulario(janela)
    if novo:
        contatos.append(novo)
        salvar_contatos(contatos)
        atualizar_interface()

def editar():
    linha = tabela.currentRow()
    if linha < 0:
        QMessageBox.warning(janela, "Erro", "Selecione um contato para editar.")
        return
    contato_atual = contatos[linha]
    atualizado = abrir_formulario(janela, contato_atual)
    if atualizado:
        contatos[linha] = atualizado
        salvar_contatos(contatos)
        atualizar_interface()

def excluir():
    linha = tabela.currentRow()
    if linha < 0:
        QMessageBox.warning(janela, "Erro", "Selecione um contato para excluir.")
        return
    resposta = QMessageBox.question(janela, "Confirmar", "Deseja realmente excluir este contato?")
    if resposta == QMessageBox.StandardButton.Yes:
        contatos.pop(linha)
        salvar_contatos(contatos)
        atualizar_interface()

botao_adicionar.clicked.connect(adicionar)
botao_editar.clicked.connect(editar)
botao_excluir.clicked.connect(excluir)

atualizar_interface()
janela.resize(600, 400)
janela.show()
aplicativo.exec()