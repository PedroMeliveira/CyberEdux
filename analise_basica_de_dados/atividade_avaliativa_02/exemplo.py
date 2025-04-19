import time
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Configuração inicial da página
st.set_page_config(page_title="Guia Streamlit", layout="wide")

# Título principal
st.title("Guia básico de componentes Streamlit e integração com Pandas e Seaborn")
st.markdown("---")

# Seção 1: Componentes de Input
st.header("1. Componentes de Input Básicos")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Inputs Básicos")
    
    # Text Input
    nome = st.text_input("Digite seu nome:", placeholder="Seu nome aqui")
    
    # Number Input
    idade = st.number_input("Sua idade:", min_value=0, max_value=120, value=25)
    
    # Slider
    altura = st.slider("Altura (metros):", 1.0, 2.5, 1.7)
    
    # Selectbox
    profissao = st.selectbox(
        "Selecione sua profissão:",
        ["Desenvolvedor", "Cientista de Dados", "Designer", "Outros"]
    )
    
    # Checkbox
    concorda = st.checkbox("Concordo com os termos de uso")
    
    # Radio Buttons
    genero = st.radio("Gênero:", ["Masculino", "Feminino", "Prefiro não informar"])
    
    # Button
    if st.button("Salvar dados"):
        st.session_state.dados_usuario = {
            "Nome": nome,
            "Idade": idade,
            "Altura": altura,
            "Profissão": profissao,
            "Concordou": concorda,
            "Gênero": genero
        }
        st.success("Dados salvos com sucesso!")

with col2:
    st.subheader("Resultados")
    
    # Mostrar dados do usuário
    if "dados_usuario" in st.session_state:
        st.write("### Dados Armazenados:")
        st.json(st.session_state.dados_usuario)
    else:
        st.warning("Nenhum dado salvo ainda!")
    
    # File Uploader
    arquivo = st.file_uploader("Carregar arquivo CSV:", type="csv")
    if arquivo is not None:
        dados_csv = pd.read_csv(arquivo)
        st.write("Pré-visualização do arquivo:")
        st.dataframe(dados_csv.head())
    
    # Color Picker
    cor = st.color_picker("Escolha uma cor:", "#00FF00")
    st.write(f"Cor selecionada: {cor}")
    
    # Text Area
    comentario = st.text_area("Deixe seu comentário:")
    if comentario:
        st.write("Seu comentário:")
        st.code(comentario)

# Seção 2: Outros Componentes
st.header("2. Outros Componentes Úteis")

    
# Progress Bar
st.subheader("Progress Bar")
progresso = st.progress(0)
for i in range(100):
    progresso.progress(i + 1)

# Spinner
if st.button("Processar dados"):
    with st.spinner("Processando..."):
        time.sleep(2)
        st.balloons()

# Expander
with st.expander("Clique para ver informações adicionais"):
    st.write("""
        Este é um conteúdo adicional que pode ser mostrado ou ocultado.
        - Item 1
        - Item 2
        - Item 3
    """)

# Metric
st.subheader("Métricas")
col1, col2, col3 = st.columns(3)
col1.metric("Temperatura", "25 °C", "1.2 °C")
col2.metric("Velocidade", "120 km/h", "-8 km/h")
col3.metric("Umidade", "65%", "4%")

# Seção 3: Carregamento e exibição de dados
st.header("3. Trabalhando com DataFrames")

# Criar DataFrame de exemplo
data = pd.DataFrame({
    'Data': pd.date_range(start='2023-01-01', periods=100),
    'Valor': np.random.randn(100).cumsum(),
    'Categoria': np.random.choice(['A', 'B', 'C'], 100)
})

# Mostrar DataFrame
st.subheader("DataFrame de exemplo")
st.dataframe(data, use_container_width=True)

# Mostrar estatísticas básicas
st.subheader("Estatísticas descritivas")
st.write(data.describe())

# Opção para download
st.subheader("Download dos dados")
st.download_button(
    label="Baixar CSV",
    data=data.to_csv(index=False).encode('utf-8'),
    file_name='dados_exemplo.csv',
    mime='text/csv'
)

# Seção 4: Visualização de dados
st.header("4. Visualização com Seaborn")

tab1, tab2, tab3 = st.tabs(["Linha", "Barras", "Boxplot"])
    
with tab1:
    st.subheader("Gráfico de Linha")
    fig, ax = plt.subplots()
    sns.lineplot(data=data, x='Data', y='Valor', hue='Categoria', ax=ax)
    st.pyplot(fig)
    st.markdown("*Gráfico mostrando a evolução temporal dos valores*")

with tab2:
    st.subheader("Gráfico de Barras")
    fig, ax = plt.subplots()
    sns.barplot(data=data, x='Categoria', y='Valor', ax=ax)
    st.pyplot(fig)
    st.markdown("*Média de valores por categoria*")

with tab3:
    st.subheader("Boxplot")
    fig, ax = plt.subplots()
    sns.boxplot(data=data, x='Categoria', y='Valor', ax=ax)
    st.pyplot(fig)
    st.markdown("*Distribuição dos valores por categoria*")

# Seção 5: Interatividade
st.header("5. Componentes Interativos")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Filtros de dados")
    # Slider para seleção de intervalo
    min_val = int(data['Valor'].min())
    max_val = int(data['Valor'].max())
    selected_range = st.slider(
        "Selecione o intervalo de valores:",
        min_val, max_val, (min_val, max_val)
    )
    
    # Filtragem dos dados
    filtered_data = data[
        (data['Valor'] >= selected_range[0]) & 
        (data['Valor'] <= selected_range[1])
    ]
    st.write(f"Registros filtrados: {len(filtered_data)}")

with col2:
    st.subheader("Seleção de categoria")
    # Selectbox para escolha de categoria
    selected_category = st.selectbox(
        "Escolha uma categoria:",
        data['Categoria'].unique()
    )
    
    # Mostrar dados da categoria selecionada
    st.write(data[data['Categoria'] == selected_category])

# Seção 6: Layout e organização
st.header("6. Organização do Layout")

# Colunas
st.subheader("Usando colunas")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total de Registros", len(data))

with col2:
    st.metric("Média de Valores", f"{data['Valor'].mean():.2f}")

with col3:
    st.metric("Valor Máximo", f"{data['Valor'].max():.2f}")

# Expanders
st.subheader("Expanders para organização")
with st.expander("Mostrar dados brutos"):
    st.write(data)

# Checkbox
st.subheader("Controle de exibição")
if st.checkbox("Mostrar informações estatísticas"):
    st.write(data.describe())

