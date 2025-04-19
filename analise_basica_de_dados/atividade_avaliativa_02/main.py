import time
import streamlit as st
import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import funcao as fun

fun.criar_tabelas_sql()
fun.insere_perfil()
DADOS = 'analise_basica_de_dados/atividade_avaliativa_02/dados.db'

st.set_page_config(page_title='Gerenciador de Orçamento', layout='wide')

st.title("Bem vindo ao seu Gerenciador de Orçamento")
st.markdown("---")

col1, col2 = st.columns(2)
id_cliente = 1
with col1:
    st.subheader('Adicionar Despesa')

    valor_despesa = st.number_input("Valor da Despesa: ", min_value=0, max_value=1000000000, value=100)

    data_despesa = st.date_input("Data da Despesa: ", format="DD/MM/YYYY")

    tipo_de_despesa = st.radio("Tipo da Despesa:", ["Lazer", "Transporte", "Alimentação", "Outros"])

    if st.button("Salvar dados"):
        st.session_state.dados_usuario = {
            "Categoria": tipo_de_despesa,
            "Valor": valor_despesa,
            "Data": data_despesa
        }
        st.success("Dados salvos com sucesso!")

        conexao = sqlite3.connect(DADOS)
        cursor = conexao.cursor()
        cursor.execute(f"INSERT INTO Despesas (Valor, Data, Categoria, ID_Cliente) VALUES ('{valor_despesa}', '{data_despesa}', '{tipo_de_despesa}', {id_cliente})")