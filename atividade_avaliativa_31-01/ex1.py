import csv
import re

with open('CyberEdux/atividade_avaliativa_31-01/weblog.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)


# Quantas requisições de cada método foram feitas? 

    requisições = {}
    qntd_get = qntd_post = 0
    for linha in leitor:
        metodo = linha[2].split()
        if metodo[0] not in requisições and (metodo[0] == 'GET' or metodo[0] == 'POST'):
            requisições[metodo[0]] = 1
        elif metodo[0] in requisições:
            requisições[metodo[0]] += 1
    
    for metodo, qnt in requisições.items():
        print(f'\nO método {metodo} foi usado {qnt} vezes.')

# Quais os IPs que mais acessaram?

with open('CyberEdux/atividade_avaliativa_31-01/weblog.csv', 'r') as arquivo:
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
    print('\n Os ips que mais acessaram:')
    for ip, qnt in ips.items():
        print(f'{i} - {ip}: {qnt} vezes.')
        i += 1




