from funcoes import *

st.set_page_config(page_title='Analise de Dados VGA Sales', layout='wide')

st.title('Análises de Dados')
st.markdown('---')

with st.sidebar:
    ano_min = int(df['Year'].min())
    ano_max = int(df['Year'].max())
    fil_ano = st.slider('Ano', ano_min, ano_max, (ano_min, ano_max))

    regioes = ['Global_Sales', 'NA_Sales', 'EU_Sales', 'JP_Sales']
    fil_regioes = st.multiselect("Regiões", regioes, placeholder='Escolha as opções')

    df_plataformas = df['Platform'].unique()
    fil_plat = st.multiselect("Plataformas", df_plataformas, placeholder='Escolha as opções')

    df_genero = df['Genre'].unique()
    fil_genero = st.multiselect("Gênero", df_genero, placeholder='Escolha as opções')

col1, col2, col3 = st.columns(3)

col1.metric('Total Jogos', str(df['Name'].nunique()))

with col2:
    col2_1, col2_2 = st.columns(2)
    col2_1.metric('Jogo mais antigo', str(ano_min))
    col2_2.metric('Jogo mais recente', str(ano_max))

with col3:
    st.metric('Editora Maior Número de Jogos', df['Publisher'].value_counts().idxmax())

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Jogos mais vendidos', 'Região', 'Popularidade','Tendências', 'Busca']) 

df_media_vendas = df.groupby('Name')['Global_Sales'].mean()