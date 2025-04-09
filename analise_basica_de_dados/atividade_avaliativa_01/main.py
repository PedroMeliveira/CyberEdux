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

# 14. Existem valores faltantes (NaN) na coluna "Year"? Quantos?

# 15. Quantos jogos venderam mais de 30 milhões globalmente (Global_Sales)?

# 16. Qual a posição no ranking (Rank) do jogo "Mario Kart Wii"?

# 17. Quais são os dados completos do jogo que está na terceira posição do ranking?

# 18. Crie uma nova coluna "Total_Regional" somando NA_Sales + EU_Sales + JP_Sales + Other_Sales

# 19. Qual a diferença percentual entre Global_Sales e Total_Regional para o primeiro jogo da lista?

# Desafios:

# 20. Encontre o jogo com vendas "Other_Sales" mais próximas da média dessa coluna.

# 21. Qual jogo possui vendas na América do Norte (NA_Sales) maiores do que as vendas na Europa (EU_Sales) e no Japão (JP_Sales) combinadas?

# 22. Qual editora (Publisher) tem a maior média de vendas globais por jogo (Global_Sales)?

# 23. Qual jogo tem a maior porcentagem de vendas no Japão (JP_Sales) em relação às vendas globais (Global_Sales)?

# 24. Quantos jogos foram lançados pela mesma Publisher em pelo menos 3 plataformas (Platform) diferentes?

# 25. Qual é o jogo mais antigo (Year) no dataset que ainda possui vendas globais (Global_Sales) acima de 20 milhões?