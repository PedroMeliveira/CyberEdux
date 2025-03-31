import pandas as pd

idades = pd.Series([23, 35, 45], index=['Ana', 'Bruno', 'Carlos'])

serie = pd.Series([10, 20,  30, 40])
print(serie + 5)
print(serie * 2)

print(serie.sum())      # Soma total
print(serie.mean())     # Média
print(serie.median())   # Mediana
print(serie.std())      # Desvio padrão
print(serie.min())      # Valor mínimo
print(serie.max())      # Valor máximo

# Filtra valores maiores que 20
print(serie[serie > 20])
# Soma apenas os valores maiores que 20
print((serie[serie > 20]).sum()) 

serie1 = pd.Series([10, 20, 30])
serie2 = pd.Series([5, 15, 25])
print(serie1 + serie2) # Soma elemento a elemento
print(serie1 * serie2) # Multiplicação elemento a elemento
