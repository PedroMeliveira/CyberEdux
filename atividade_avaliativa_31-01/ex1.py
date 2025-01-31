import csv

with open('atividade_avaliativa_31-01/weblog.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)

    requisições = []

    for linha in leitor:
        url = linha[2].split()
        metodo = url[0]
        if metodo not in requisições:
            requisições.append(metodo)

print(requisições)