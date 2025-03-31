import pandas as pd

CSV = 'analise_basica_de_dados/aula_01/Ecommerce_Consumer_Behavior_Analysis_Data.csv'

df = pd.read_csv(CSV)

# (1) Qual o público que mais compra os produtos, masculino ou feminino?
# (2) Qual a média de idade dos clientes?
# (4) Qual é a quantidade de clientes em cada status de casamento?
# (5) Qual é o preço médio de cada compra?
# (5.1) Preço médio de compra por gênero
# (5.2) Preço médio de compra por Income
# (6) Qual é a frequência média de compra?

# (1)
# print(f"{df['Marital_Status'].unique()}")

print(f"Masculino: {df['Gender'].value_counts().get('Male')} Pessoas\n ")
print(f"Feminino: {df['Gender'].value_counts().get('Female')} Pessoas\n ")
print(f"Casadas: {df['Marital_Status'].value_counts().get('Married')} Pessoas\n ")
print(f"Solteiras: {df['Marital_Status'].value_counts().get('Single')} Pessoas\n ")
print(f"Viúvos: {df['Marital_Status'].value_counts().get('Widowed')} Pessoas\n ")
print(f"Divorciadas: {df['Marital_Status'].value_counts().get('Divorced')} Pessoas\n ")

