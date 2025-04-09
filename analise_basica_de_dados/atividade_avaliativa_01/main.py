import pandas as pd

df = pd.read_csv('analise_basica_de_dados/atividade_avaliativa_01/vgsales.csv')

# 1. Quantas linhas e colunas existem no dataset?

# print(df.shape)

# 2. Qual é o total de vendas globais (Global_Sales) somando todas as linhas?

# print(df['Global_Sales'].sum())

# 3. Liste os 10 primeiros jogos do ranking.

# print(df.head(10))

# 4. Quantos jogos foram lançados no ano de 2006?

# print(df[df['Year'] == 2006].value_counts().sum())

# 5. Mostre todos os jogos publicados pela "Nintendo" com vendas europeias (EU_Sales) acima de 10 milhões.

# print(df[(df['Publisher'] == 'Nintendo') & (df['EU_Sales'] > 10)])

# 6. Quais jogos do gênero "Racing" estão presentes no dataset?

# print(df[df['Genre'] == 'Racing'])

# 7. Qual é a média de vendas na América do Norte (NA_Sales) para todos os jogos?

# print(round(df['NA_Sales'].mean(), 2))

# 8. Qual editora (Publisher) aparece mais vezes no dataset?

# print(df['Publisher'].value_counts().head(1))

# 9. Quantos gêneros diferentes (Genre) existem na base de dados?

# print(df['Genre'].nunique())

# 10. Quais são os 5 jogos com maiores vendas no Japão (JP_Sales)?

# print(df.sort_values(['JP_Sales'], ascending=False).head(5)['Name'])

# 11. Ordene o dataset por ano de lançamento em ordem decrescente.

# print(df.sort_values(['Year'], ascending=False).dropna())

# 12. Qual jogo tem a maior diferença entre vendas norte-americanas (NA_Sales) e japonesas (JP_Sales)?


# df['NA_JP_Diff'] = (df['NA_Sales'] - df['JP_Sales']).abs()

# maior_diferença = df.loc[df['NA_JP_Diff'].idxmax()]

# print(maior_diferença[['Name', 'NA_Sales','JP_Sales', 'NA_JP_Diff']])

# 13. Qual gênero tem o maior total de vendas globais?

# print(df.groupby('Genre')['Global_Sales'].sum().idxmax())

# 14. Existem valores faltantes (NaN) na coluna "Year"? Quantos?

# print(df['Year'].isna().value_counts())

# 15. Quantos jogos venderam mais de 30 milhões globalmente (Global_Sales)?

# jogos_30milhoes = df[df['Global_Sales'] > 30]

# print(jogos_30milhoes.shape[0])

# 16. Qual a posição no ranking (Rank) do jogo "Mario Kart Wii"?

# print(df[df['Name'] == 'Mario Kart Wii']['Rank'])

# 17. Quais são os dados completos do jogo que está na terceira posição do ranking?

# print(df[df['Rank'] == 3])

# 18. Crie uma nova coluna "Total_Regional" somando NA_Sales + EU_Sales + JP_Sales + Other_Sales

# df['Total_Regional'] = df['NA_Sales'] + df['EU_Sales'] + df['JP_Sales'] + df['Other_Sales']

# print(df)

# 19. Qual a diferença percentual entre Global_Sales e Total_Regional para o primeiro jogo da lista?

# df['Diferença'] = df['Global_Sales'] - df['Total_Regional']

# print(df[df['Rank'] == 1]['Diferença'])

# Desafios:

# 20. Encontre o jogo com vendas "Other_Sales" mais próximas da média dessa coluna.

# df['Diferença_Média'] = (df['Other_Sales'] - df['Other_Sales'].mean()).abs()
# menor_diferença = df.loc[df['Diferença_Média'].idxmin()]

# print(menor_diferença[['Name', 'Diferença_Média']])

# 21. Qual jogo possui vendas na América do Norte (NA_Sales) maiores do que as vendas na Europa (EU_Sales) e no Japão (JP_Sales) combinadas?

# df['EU_JP_Sales'] = df['EU_Sales'] + df['JP_Sales']

# print(df[df['EU_JP_Sales'] < df['NA_Sales']])

# 22. Qual editora (Publisher) tem a maior média de vendas globais por jogo (Global_Sales)?

# media_vendas_por_editora = df.groupby('Publisher')['Global_Sales'].mean()

# print(media_vendas_por_editora.idxmax())

# 23. Qual jogo tem a maior porcentagem de vendas no Japão (JP_Sales) em relação às vendas globais (Global_Sales)?

df_valid = df[df["Global_Sales"] > 0]

df['Diff_JP_Sales_Global_Sales'] = (df['JP_Sales']/df_valid) * 100

print(df.loc[df['Diff_JP_Sales_Global_Sales'].idxmax()])
# 24. Quantos jogos foram lançados pela mesma Publisher em pelo menos 3 plataformas (Platform) diferentes?

# 25. Qual é o jogo mais antigo (Year) no dataset que ainda possui vendas globais (Global_Sales) acima de 20 milhões?