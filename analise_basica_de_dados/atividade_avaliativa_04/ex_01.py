import pandas as pd
import streamlit as st
import plotly.express as px
CSV = 'Ecommerce_Consumer_Behavior_Analysis_Data.csv'

df = pd.read_csv(CSV)

st.set_page_config(page_title='Analise de Dados Ecommerce', layout='wide')

st.title('Análises de Dados')
st.markdown('---')

tab1, tab2 = st.tabs(['Publico Alvo', 'Vendas'])

with tab1:
    tab1_1, tab1_2, tab1_3, tab1_4 = st.tabs(['Genero', 'Estado Civil', 'Idade', 'Nivel de Renda'])
    
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
    
    with tab1_4:
        fig = px.pie(df['Income_Level'].value_counts().reset_index(), values='count', names='Income_Level', title='Percentual nivel de renda')
        st.plotly_chart(fig)

with tab2:
    tab2_1, tab2_2, tab2_3 = st.tabs(['Categoria', 'Média', 'Pagamento'])

    with tab2_1:
        fig = px.bar(df.groupby('Purchase_Category')['Frequency_of_Purchase'].sum().sort_values(ascending=False).reset_index(), x='Purchase_Category', y='Frequency_of_Purchase', title='Categorias mais vendidas')
        st.plotly_chart(fig)

    with tab2_2:
        col2_2_1, col2_2_2 = st.columns(2)

        with col2_2_1:
            col2_2_1_1, col2_2_1_2 = st.columns(2)

            with col2_2_1_1:
                df['Valor'] = df.apply(lambda x:float(x['Purchase_Amount'][1:]), axis=1)
                st.metric('Valor médio gasto por compra', f"$ {df['Valor'].mean():.2f}")

            with col2_2_1_2:
                st.metric('Avaliação média dos produtos', int(df['Customer_Satisfaction'].mean()))
    
        with col2_2_2:
            col2_2_2_1, col2_2_2_2 = st.columns(2)
            with col2_2_2_1:
                fig = px.bar(df.groupby('Gender')['Valor'].mean().reset_index(), x='Gender', y='Valor', title='Média de compra por genêro')
                st.plotly_chart(fig)
            
            with col2_2_2_2:
                fig = px.bar(df.groupby('Marital_Status')['Valor'].mean().reset_index(), x='Marital_Status', y='Valor', title='Média de compra por estado civil')
                st.plotly_chart(fig)
    
    with tab2_3:
        fig = px.bar(df['Purchase_Channel'].value_counts().reset_index(), x='Purchase_Channel', y='count' , title='Compras feitas Misto x Online x Fisica')
        st.plotly_chart(fig)


