# QUESTAO 4

# OPCÕES DE REGRA: 'dobrar', 'ao quadrado', 'somar 10'
# , 'subtrair 5', 'dividir 10', 'somar 10, dividir 5, e multiplicar 50'

def gerar_sequencia_personalizada(inicio, fim, regra):
    lista = []
    if regra == 'dobrar':
        for i in range(inicio, fim):
            lista.append(i*2)
    if regra == 'ao quadrado':
        for i in range(inicio, fim):
            lista.append(i**2)
    if regra == 'somar 10':
        for i in range(inicio, fim):
            lista.append(i + 10)
    if regra == 'subtrair 5':
        for i in range(inicio, fim):
            lista.append(i - 5)
    if regra == 'dividir 10':
        for i in range(inicio, fim):
            lista.append(i / 10)
    if regra == 'somar 10, dividir 5, e multiplicar 50':
        for i in range(inicio, fim):
            lista.append(((i+10)/5)*50)
    return lista





  
