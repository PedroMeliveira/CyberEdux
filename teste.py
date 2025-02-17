import csv

with open("saida.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Nome", "Idade", "Cidade"])
    escritor.writerow(["João", 30, "São Paulo"])