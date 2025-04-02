import pandas as pd

CSV = 'analise_basica_de_dados/aula_01/Ecommerce_Consumer_Behavior_Analysis_Data.csv'

df = pd.read_csv(CSV)

# Qual é o público alvo?

# quantidade de cada gênero

# print(df['Gender'].value_counts())

# porcentagem de cada gênero

# print(df['Gender'].value_counts(normalize=True) * 100)

# Quantos solteiros tem?

# print(f"Número de solteiros: {df['Marital_Status'].value_counts().get('Single')}")

# Qual é a idade média dos clientes?

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