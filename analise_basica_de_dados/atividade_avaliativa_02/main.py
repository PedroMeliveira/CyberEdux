import time
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title='Gerenciador de Orçamento', layout='wide')

st.title("Bem vindo ao seu Gerenciador de Orçamento")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader('Adicionar Gastos')

    tipo_de_gasto = st.radio("Tipo de gasto:", ["Lazer", "Transporte", "Alimentação", "Outros"])