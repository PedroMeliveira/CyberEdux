import streamlit as st
import sqlite3
import re

class Pagamento:
    def __init__(self, metodo, valor, data):
        self.metodo = metodo
        self.valor = valor
        self.data = data
        self.status = 'Pendente'
        
    def set_status(self, status):
        self.status = status


class Credito():
    def __init__(self, numero, nome, validade, cvv):
        self.numero = numero
        self.nome = nome
        self.validade = validade
        self.cvv = cvv


def validar_cartao(numero):
    regex_cartao = r'^\d{13,19}$'   
    return re.fullmatch(regex_cartao, numero.replace(" ", "")) is not None

def validar_cvv(cvv):
    return re.fullmatch(r'^\d{3,4}$', cvv) is not None

def cria_credito():
    numero = st.text_input("Número do cartão de crédito:")
    
    if numero:
        if validar_cartao(numero):
            st.success("✅ Número de cartão válido!")
        else:
            st.error("❌ Número inválido. Digite apenas números (13 a 19 dígitos).")
    
    nome = st.text_input("Nome do titular: ")
    
    validade = st.date_input("Data de validade: ", format='DD/MM/YYYY', min_value='today')
    
    cvv = st.text_input("CVV: ", max_chars=4)
    
    if cvv:
        if validar_cvv(cvv):
            st.success("✅ CVV válido!")
            
        else:
            st.error("❌ CVV inválido. Deve conter 3 ou 4 dígitos numéricos.")
    
    if validar_cartao(numero) and validar_cvv(cvv):
        return Credito(numero, nome, validade, cvv)
    

class Paypal():
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha
        
    def get_senha(self):
        return self.__senha
    

# Função para validar e-mail
def validar_email(email):
    regex_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex_email, email) is not None


def validar_senha(senha):
    regex_senha = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$'
    return re.fullmatch(regex_senha, senha) is not None


def cria_paypal():
    email = st.text_input("Email: ")
    
    if email:
        if validar_email(email):
            st.success("✅ E-mail válido!")
            
        else:
            st.error("❌ E-mail inválido. Tente novamente.")

    senha = st.text_input("Senha: ", type='password')
    
    if senha:
        if validar_senha(senha):
            st.success("✅ Senha válida!")
            
        else:
            st.error("❌ A senha deve ter:\n- Mínimo 8 caracteres\n- Letra maiúscula e minúscula\n- Número\n- Caractere especial")
    
    if validar_email(email) and validar_senha(senha):
        return Paypal(email, senha)
    
    
class Bancaria():
    def __init__(self, codigo, origem, destino):
        self.codigo = codigo
        self.origem = origem
        self.destino = destino

def validar_codigo_banco(codigo):
    return re.fullmatch(r'^\d{3}$', codigo) is not None

def validar_conta(conta):
    return re.fullmatch(r'^\d{4,12}(-\d{1})?$', conta) is not None

def cria_bancaria():
    codigo = st.text_input("Ccódigo do banco: ", max_chars=3)
    
    if codigo:
        if validar_codigo_banco(codigo):
            st.success("✅ Código de banco válido!")
        else:
            st.error("❌ Código inválido. Deve conter exatamente 3 dígitos numéricos.")
    
    origem = st.text_input("Conta de origem: ")
    
    if origem:
        if validar_conta(origem):
            st.success("✅ Conta válida!")
        
        else:
            st.error("❌ Conta inválida. Deve ter de 4 a 12 dígitos, com DV opcional (ex: 123456-7).")
    
    destino = st.text_input("Conta de destino: ")
    
    if destino:
        if validar_conta(destino):
            st.success("✅ Conta válida!")
        
        else:
            st.error("❌ Conta inválida. Deve ter de 4 a 12 dígitos, com DV opcional (ex: 123456-7).")
    
    if validar_codigo_banco(codigo) and validar_conta(origem) and validar_conta(destino):
        return Credito(codigo, origem, destino)

    
def menu():
    st.set_page_config(page_title='Sistema de Pagamentos', layout='centered')

    st.title("Bem vindo ao seu Sistema de Pagamentos")
    st.markdown("---")

    st.subheader('Adicionar Pagamento')

def cria_trans():

    col1, col2, col3 = st.columns(3)
    with col1:
        valor = st.number_input("Valor do seu pagamento: ", min_value=0, value=100)
    
    with col2:
        data = st.date_input("Data do seu pagamento: ", format="DD/MM/YYYY")
    
    with col3:
        metodo = st.radio("Método do seu pagamento: ", ['Crédito', 'Paypal', 'Transferência Bancária'])
    
    st.markdown("---")
    return Pagamento(metodo, valor, data)

def cria_tabela():
    conexao = sqlite3.connect('dados.db')
    cursor = conexao.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Pagamentos (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Metodo TEXT NOT NULL,
            Valor FLOAT,
            Data TEXT NOT NULL,
            Status TEXT NOT NULL
        )
       ''')
    
    conexao.commit()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cartão_Crédito (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Número_Cartão TEXT NOT NULL,
            Nome TEXT NOT NULL,
            Validade TEXT NOT NULL,
            CVV TEXT NOT NULL,
            Pagamento_ID INTEGER,
            FOREIGN KEY (Pagamento_ID) REFERENCES Pagamentos(ID)
        )
       ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Paypal (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Email TEXT NOT NULL,
            Senha TEXT NOT NULL,
            Pagamento_ID INTEGER,
            FOREIGN KEY (Pagamento_ID) REFERENCES Pagamentos(ID)
        )           
        ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Trans_Bancária (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Código_Banco TEXT NOT NULL,
            Conta_Origem TEXT NOT NULL,
            Conta_Destino TEXT NOT NULL,
            Pagamento_ID INTEGER,
            FOREIGN KEY (Pagamento_ID) REFERENCES Pagamentos(ID)
        )         
        ''')
    
    conexao.commit()
    
def insert_pagamento_retorna_id(trans):
    conexao = sqlite3.connect('dados.db')
    cursor = conexao.cursor()
    
    cursor.execute('INSERT INTO Pagamentos (Metodo, Valor, Data, Status) VALUES (?, ?, ?, ?)', (trans.metodo, trans.valor, trans.data, trans.status))
    
    conexao.commit()
    
    return cursor.lastrowid

def insert_credito(pagamento, pag_id):
    conexao = sqlite3.connect('dados.db')
    cursor = conexao.cursor()
    
    cursor.execute('INSERT INTO Cartão_Crédito (Número_Cartão, Nome, Validade, CVV, Pagamento_ID) VALUES (?, ?, ?, ?, ?)', (pagamento.numero, pagamento.nome, pagamento.validade, pagamento.cvv, pag_id))
    
    conexao.commit()
    
def insert_paypal(pagamento, pag_id):
    conexao = sqlite3.connect('dados.db')
    cursor = conexao.cursor()
    
    cursor.execute('INSERT INTO Paypal (Email, Senha, Pagamento_ID) VALUES (?, ?, ?)', (pagamento.email, pagamento.get_senha(), pag_id))
    
    conexao.commit()
    
def insert_trans_bancaria(pagamento, pag_id):
    conexao = sqlite3.connect('dados.db')
    cursor = conexao.cursor()
    
    cursor.execute('INSERT INTO Trans_Bancária (Código_Banco, Conta_Origem, Conta_Destino, Pagamento_ID) VALUES (?, ?, ?, ?)', (pagamento.codigo, pagamento.origem, pagamento.destino, pag_id))
    
    conexao.commit()