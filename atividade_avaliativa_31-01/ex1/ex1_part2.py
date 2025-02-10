import csv
import re

with open('atividade_avaliativa_31-01/ex1/All_ViewingActivity.csv', 'r', encoding="utf8") as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha)