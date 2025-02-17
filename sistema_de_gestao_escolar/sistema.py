import sistema_funções as fun
import csv

alunos = []

try:
    with open("sistema_de_gestao_escolar/alunos.csv", "r") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            alunos.append(linha)
            
except FileNotFoundError:
    alunos = []

print(alunos)
while True:
    fun.menu()

    escolha = fun.função_escolha(0, 5)

    if escolha == 1:
        fun.adicionar_aluno(alunos)
    
    elif escolha == 2:
        if len(alunos) == 0:
            print(f'\nNão existem alunos cadastrados no seu sistema. ')
        else:
            fun.remover_aluno(alunos)

    elif escolha == 3:
        if len(alunos) == 0:
            print(f'\nNão existem alunos cadastrados no seu sistema. ')
        else:
            fun.listar_alunos(alunos)


    elif escolha == 0:
        break