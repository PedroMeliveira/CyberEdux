import csv
import re

with open('atividade_avaliativa_31-01/ex1/part1/weblog.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)


# Quantas requisições de cada método foram feitas? 
    requisições = {}
    qntd_get = qntd_post = 0
    for linha in leitor:
        metodo = linha[2].split(',')
        requisição = metodo[0][:4]
        if requisição not in requisições and requisição == 'GET ': 
            requisições[requisição] = 1
        elif requisição in requisições:
            requisições[requisição] += 1
        if requisição not in requisições and requisição == 'POST':
            requisições[requisição] = 1
        elif requisição in requisições:
            requisições[requisição] += 1

    for metodo, qnt in requisições.items():
        print(f'\nO método {metodo} foi usado {qnt} vezes.')

# Quais os IPs que mais acessaram?

with open('atividade_avaliativa_31-01/ex1/part1/weblog.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)

    ips = {}

    for linha in leitor:
        ip = linha[0].split(',')
        pattern = '[\d]{2}[.][\d]{3}[.][\d][.][\d]'
        if ip[0] not in ips and re.search(pattern, ip[0]):
            ips[ip[0]] = 1
        elif ip[0] in ips:
            ips[ip[0]] += 1

    ips = dict(sorted(ips.items(), key=lambda item: item[1], reverse=True))

    i = 1
    print('\nOs ips que mais acessaram:')
    for ip, qnt in ips.items():
        print(f'{i} - {ip}: {qnt} vezes.')
        i += 1

# Quantas requisições com status de erro tiveram?

with open('atividade_avaliativa_31-01/ex1/part1/weblog.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)

    qnt_erro = 0

    for linha in leitor:
        stat = linha[-1].split(',')
        if stat[0] == '404':
            qnt_erro += 1
    print(f'\nTiveram {qnt_erro} requisições com status de erro.')

# Qual foi o dia que mais teve requisições?

with open('atividade_avaliativa_31-01/ex1/part1/weblog.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)

    datas = {}

    for linha in leitor:
        data = linha[1].split(',')
        dia = data[0][1:12]
        pattern = '[\d]{2}[/][A-Z][a-z]{2}[/][\d]{4}'
        if dia not in datas and re.search(pattern, dia):
            datas[dia] = 1
        elif dia in datas:
            datas[dia] += 1
    
    datas = dict(sorted(datas.items(), key=lambda item: item[1], reverse=True))
    
    i = 1

    print('\nOs dias que mais tiveram requisições:')

    for dia, qnt in datas.items():
        print(f'{i} - {dia}: {qnt} vezes.')
        i += 1
        if i == 6:
            break
