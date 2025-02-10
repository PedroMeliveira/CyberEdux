import csv
import re

with open('atividade_avaliativa_31-01/ex1/part2/All_ViewingActivity.csv', 'r', encoding="utf8") as arquivo:
    leitor = csv.reader(arquivo)



# # Quais perfil mais acessou?
#     perfils = {}

#     for linha in leitor:
#         perfil = linha[0]
#         pattern = '[User ][\d]'
#         if perfil not in perfils and re.search(pattern, perfil):
#             perfils[perfil] = 1
#         elif perfil in perfils:
#             perfils[perfil] += 1

#     perfils = dict(sorted(perfils.items(), key=lambda item: item[1], reverse=True))

#     i = 1
#     for perfil, qnt in perfils.items():
#         print(f'{i} - {perfil} acessou {qnt} vezes.')
#         i += 1

# Dias que tiveram mais requisições?

with open('atividade_avaliativa_31-01/ex1/part2/All_ViewingActivity.csv', 'r', encoding="utf8") as arquivo:
    leitor = csv.reader(arquivo)

    datas = {}

    for linha in leitor:
        data = linha[1].split(',')
        dia = data[0][:11]
        pattern = '[\d]{4}[-][\d]{2}[-][\d]{2}'
        if dia not in datas and re.search(pattern, dia):
            datas[dia] = 1
        elif dia in datas:
            datas[dia] += 1

    datas = dict(sorted(datas.items(), key=lambda item: item[1], reverse=True))


    print('\nOs dias que mais tiveram requisições:\n')
    i = 1
    for dia, qnt in datas.items():
        print(f'{i} - {dia}: {qnt} vezes.')
        i += 1
        if i == 6:
            print()
            break
    

   