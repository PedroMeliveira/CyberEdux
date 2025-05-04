import pandas as pd
import streamlit as st
import plotly.express as px
CSV = 'Ecommerce_Consumer_Behavior_Analysis_Data.csv'

df = pd.read_csv(CSV)

st.set_page_config(page_title='Analise de Dados Ecommerce', layout='wide')

st.title('Análises de Dados')
st.markdown('---')

tab1, tab2 = st.tabs(['Publico Alvo', 'Região'])

with tab1:
    tab1_1, tab1_2, tab1_3 = st.tabs(['Genero', 'Estado Civil', 'Idade'])
    with tab1_1:
        fig = px.pie(df['Gender'].value_counts().reset_index(), values='count', names='Gender', title='Percentual gênero')
        st.plotly_chart(fig)
    with tab1_2:
        fig = px.pie(df['Marital_Status'].value_counts().reset_index(), values='count', names='Marital_Status', title='Percentual estado civil')
        st.plotly_chart(fig)

    with tab1_3:
        st.metric('Idade média', value=int(df["Age"].mean()))
        col1_3_1, col1_3_2, col1_3_3 = st.columns(3)
        with col1_3_1:
            col1_3_1_1, col1_3_1_2, col1_3_1_3 = st.columns(3)
            fig = px.bar(df.groupby('Income_Level')['Age'].mean().reset_index(), x='Income_Level', y='Age', title='Idade média por nivel de renda')
            st.plotly_chart(fig)
        with col1_3_2:
            fig = px.bar(df.groupby('Gender')['Age'].mean().reset_index(), x='Gender', y='Age', title='Percentual de idade por gênero')
            st.plotly_chart(fig)
        with col1_3_3:
            fig = px.bar(df['Age'].value_counts().reset_index(), x='Age', y='count', title='Percentual Idade')
            st.plotly_chart(fig)
# print(f'Idade média dos clientes: {df["Age"].mean()}')

# Qual é a idade média por nível de renda?

# print(df.groupby('Income_Level')['Age'].mean())

# Qual é a idade média por gênero?

# print(df.groupby('Gender')['Age'].mean())

# Qual é a proporção de clientes por nível de renda (Baixa, Média, Alta)?

# print(df['Income_Level'].value_counts(normalize=True) * 100)

# Qual é a categoria de produto mais comprada?

# print(df.groupby('Purchase_Category')['Frequency_of_Purchase'].sum().sort_values(ascending=False).head(1))

# Qual é o valor médio gasto por compra?

# df['Valor'] = df.apply(lambda x:float(x['Purchase_Amount'][1:]), axis=1)
# print(df['Valor'].mean())

# Qual é o método de pagamento mais usado?

# print(df['Payment_Method'].value_counts().head(1))

# Quantas compras foram feitas online vs. em loja física?

# print(df['Purchase_Channel'].value_counts())

# Qual é a avaliação média dos produtos?

# print(df['Customer_Satisfaction'].mean())

# O valor médio de compra é maior para clientes do gênero feminino ou masculino?

# print(df.groupby('Gender')['Valor'].mean())

# O valor médio de compra pelo marital status

# print(df.groupby('Marital_Status')['Valor'].mean())