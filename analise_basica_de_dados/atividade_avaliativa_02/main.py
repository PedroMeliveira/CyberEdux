import time
import streamlit as st
import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import funcao as fun

fun.criar_tabelas_sql()
# fun.insere_perfil()
DADOS = 'dados.db'

st.set_page_config(page_title='Gerenciador de Orçamento', layout='wide')

st.title("Bem vindo ao seu Gerenciador de Orçamento")
st.markdown("---")

col1, col2 = st.columns(2)
id_cliente = 1
with col1:
    st.subheader('Adicionar Despesa')

    valor_despesa = st.number_input("Valor da Despesa: ", min_value=0, value=100)

    data_despesa = st.date_input("Data da Despesa: ", format="DD/MM/YYYY")

    tipo_de_despesa = st.radio("Tipo da Despesa:", ["Lazer", "Transporte", "Alimentação", "Outros"])

    if st.button("Salvar dados"):
        # st.session_state.dados_usuario = {
        #     "Categoria": tipo_de_despesa,
        #     "Valor": valor_despesa,
        #     "Data": data_despesa
        # }

        conexao = sqlite3.connect(DADOS, check_same_thread=False)
        cursor = conexao.cursor()
        cursor.execute(f"INSERT INTO Despesas (Valor, Data, Categoria, ID_Cliente) VALUES ('{valor_despesa}', '{data_despesa}', '{tipo_de_despesa}', {id_cliente})")
        conexao.commit()
        st.success("Dados salvos com sucesso!")

with col2:
    st.subheader('Adicionar Receita')

    valor_receita = st.number_input("Valor da Receita: ", min_value=0, value=100)

    data_receita = st.date_input("Data da Receita: ", format="DD/MM/YYYY")

    tipo_de_receita = st.radio("Tipo da Receita:", ["Salario", "Pix", "Renda Extra", "Outros"])

    if st.button("Salvar dados", key=:
        # st.session_state.dados_usuario = {
        #     "Categoria": tipo_de_receita,
        #     "Valor": valor_receita,
        #     "Data": data_receita
        # }
        conexao = sqlite3.connect(DADOS, check_same_thread=False)
        cursor = conexao.cursor()
        cursor.execute(f"INSERT INTO Receitas (Valor, Data, Categoria, ID_Cliente) VALUES ('{valor_receita}', '{data_receita}', '{tipo_de_receita}', {id_cliente})")
        conexao.commit()
        st.success("Dados salvos com sucesso!")