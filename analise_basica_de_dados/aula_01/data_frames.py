import pandas as pd

dados = {
 'Nome': ['Ana', 'Bruno', 'Carlos'],
 'Idade': [23, 35, 45],
 'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}
df = pd.DataFrame(dados)

# print(df)

# ===============

df = pd.DataFrame({
 'Produto': ['A', 'B', 'C'],
 'Preço': [100, 200, 300],
 'Quantidade': [2, 3, 5]
})
df['Total'] = df['Preço'] * df['Quantidade'] # Cria uma nova coluna "Total"
# print(df)

# Estatísticas descritivas para colunas numéricas:
# print(df.describe())
# print(df['Preço'].mean()) # Média da coluna "Preço"
# print(df['Quantidade'].sum()) # Soma da coluna "Quantidade"

df['Lucro'] = df.apply(lambda row: row['Total'] * 0.2, axis=1) #Calcula lucro de cada produto (20% do total)

# print(df)

# Filtra produtos com preço maior que R$150
produtos_caros = df[df['Preço'] > 150]
# Soma as quantidades dos produtos filtrados
# print(produtos_caros['Quantidade'].sum()) 
