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

def cria_credito():
    numero = st.number_input("Número do cartão: ", min_value=1000000000000000, max_value=9999999999999999)
    
    nome = st.text_input("Nome do titular: ")
    
    validade = st.date_input("Data de validade: ", format='DD/MM/YYYY', min_value='20/05/2025')
    
    cvv = st.number_input("CVV: ", min_value=100, max_value=999)
    
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

def cria_paypal():
    
    email = st.text_input("Email: ")
    if email:
        if validar_email(email):
            st.success("✅ E-mail válido!")
        else:
            st.error("❌ E-mail inválido. Tente novamente.")

    senha = st.text_input("Qual a senha: ")
    
    return Paypal(email, senha)
    
    
class Bancaria():
    def __init__(self, codigo, origem, destino):
        self.codigo = codigo
        self.origem = origem
        self.destino = destino
        
def cria_bancaria():
    codigo = input("Qual o código do banco? \n")
    
    origem = input("Qual a conta de origem? \n")
    
    destino = input("Qual a conta de destino? \n")
    
    return Credito(codigo, origem, destino)
    
def menu():
    st.set_page_config(page_title='Sistema de Pagamentos', layout='centered')

    st.title("Bem vindo ao seu Sistema de Pagamentos")
    st.markdown("---")

    st.subheader('Adicionar Pagamento')

def cria_pagamento():

    col1, col2, col3 = st.columns(3)
    with col1:
        valor = st.number_input("Valor do seu pagamento: ", min_value=0, value=100)
    
    with col2:
        data = st.date_input("Data do seu pagamento: ", format="DD/MM/YYYY")
    
    with col3:
        metodo = st.radio("Método do seu pagamento: ", ['Crédito', 'Paypal', 'Transferência Bancária'])
    
    st.markdown("---")
    return Pagamento(metodo, valor, data)


    


    
    
    
    
    
        