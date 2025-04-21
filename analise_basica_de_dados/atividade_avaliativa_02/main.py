import streamlit as st
import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import funcao as fun

fun.criar_tabelas_sql()
fun.insere_perfil()
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

    if st.button("Salvar dados", key= 'unique'):
        conexao = sqlite3.connect(DADOS, check_same_thread=False)
        cursor = conexao.cursor()
        cursor.execute(f"INSERT INTO Receitas (Valor, Data, Categoria, ID_Cliente) VALUES ('{valor_receita}', '{data_receita}', '{tipo_de_receita}', {id_cliente})")
        conexao.commit()
        st.success("Dados salvos com sucesso!")

st.markdown("---")

st.header('Resultados')

col3, col4 = st.columns(2) 

with col3:
    st.subheader('Despesas')

    con = sqlite3.connect(DADOS)
    df_despesas = pd.read_sql('SELECT * FROM Despesas', con)
    if not df_despesas.empty:
        st.metric("Total de Receitas", f"R$ {df_despesas['Valor'].sum():.2f}")
        st.metric("Maior Receita", f"R$ {df_despesas['Valor'].max():.2f}")
        st.metric("Menor Receita", f"R$ {df_despesas['Valor'].min():.2f}")
        df_despesas = df_despesas.sort_values(by='Data')

        st.subheader('Gráfico de Despesas')
        fig1, ax1 = plt.subplots()
        imagem = sns.lineplot(data=df_despesas, x='Data', y='Valor', ax=ax1)
        plt.ylabel('Valor')
        plt.xlabel('Data')
        plt.xticks(rotation=45)
        st.pyplot(fig1)
    else:
        st.info("Nenhuma despesa registrada.")

with col4:
    st.subheader('Receitas')

    con = sqlite3.connect(DADOS)
    df_receitas = pd.read_sql('SELECT * FROM Receitas', con)
    if not df_receitas.empty:
        st.metric("Total de Receitas", f"R$ {df_receitas['Valor'].sum():.2f}")

        st.metric("Maior Receita", f"R$ {df_despesas['Valor'].max():.2f}")

        st.metric("Menor Receita", f"R$ {df_despesas['Valor'].min():.2f}")

        st.subheader('Gráfico de Receitas')
        
        df_receitas = df_receitas.sort_values(by='Data')

        fig1, ax1 = plt.subplots()
        imagem = sns.lineplot(data=df_receitas, x='Data', y='Valor', ax=ax1)
        plt.ylabel('Valor')
        plt.xlabel('Data')
        plt.xticks(rotation=45)
        st.pyplot(fig1)
    else:
        st.info("Nenhuma receita registrada.")   
