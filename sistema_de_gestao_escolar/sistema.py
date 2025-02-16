import sistema_funções as fun
import csv

alunos = []

while True:
    fun.menu()

    escolha = fun.função_escolha(0, 5)

    fun.adicionar_aluno(alunos)
    print(alunos)

    break