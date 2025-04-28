from funcoes import *

st.set_page_config(page_title='Analise de Dados VGA Sales', layout='wide')

st.title('Análises de Dados')
st.markdown('---')

with st.sidebar:
    ano_min = int(df['Year'].min())
    ano_max = int(df['Year'].max())
    fil_ano = st.slider('Ano', ano_min, ano_max, (ano_min, ano_max))

    regioes = ['Global_Sales', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']
    fil_regioes = st.multiselect("Regiões", regioes, placeholder='Escolha as opções')

    df_plataformas = df['Platform'].unique()
    fil_plat = st.multiselect("Plataformas", df_plataformas, placeholder='Escolha as opções')

    df_genero = df['Genre'].unique()
    fil_genero = st.multiselect("Gênero", df_genero, placeholder='Escolha as opções')

df_filtrado = df[(df['Year'] >= fil_ano[0]) & (df['Year'] <= fil_ano[1])]

if len(fil_plat) > 0:
    df_filtrado = df_filtrado[df_filtrado['Platform'].isin(fil_plat)]

if len(fil_genero) > 0:
    df_filtrado = df_filtrado[df_filtrado['Genre'].isin(fil_genero)]

df_filtrado['Soma_Vendas'] = df['Global_Sales']  
if len(fil_regioes) > 0:
    df_filtrado['Soma_Vendas'] = 0
    for regiao in fil_regioes:
        if regiao != 'Global_Sales':
            df_filtrado['Soma_Vendas'] = df_filtrado['Soma_Vendas'] + df_filtrado[regiao]



col1, col2, col3 = st.columns(3)

st.subheader('Métricas Gerais')

with col1:
    col1_1, col1_2 = st.columns(2)
    col1_1.metric('Total Jogos', str(df_filtrado['Name'].nunique()))
    col1_2.metric('Media de Vendas', f"R$ {df_filtrado['Soma_Vendas'].mean():.2f}M")

with col2:
    col2_1, col2_2 = st.columns(2)
    col2_1.metric('Jogo mais antigo', str(df_filtrado['Year'].min()))
    col2_2.metric('Jogo mais recente', str(df_filtrado['Year'].max()))

with col3:
    st.metric('Editora Maior Número de Jogos', df_filtrado['Publisher'].value_counts().idxmax())



tab1, tab2, tab3, tab4, tab5 = st.tabs(['Jogos mais vendidos', 'Região', 'Popularidade','Tendências', 'Busca']) 

with tab1:
    qnt = st.selectbox("Quantidade de Jogos:", [5, 10, 15, 20])
    fig = px.line(df_filtrado.sort_values(['Soma_Vendas'], ascending=False).head(qnt), x ='Name', y='Soma_Vendas',hover_data=['Platform', 'Year'])
    st.plotly_chart(fig)

with tab2:
    fig = px.pie(df_filtrado, values='', names='country', title='Population of European continent')