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

    elif escolha == 4:
        print(f'\n1 - Relatório de um aluno\n2 - Relatório de todos alunos')
        escolha_aux = fun.função_escolha(1,2)
        if escolha_aux == 1:
            matricula = input(f'\nDigite a matricula do aluno para gerarmos um relatório: ')
            achou = False
            for aluno in alunos:
                if matricula == aluno[1]:
                    fun.relatorio_word_unico(matricula, alunos)
                    achou = True
            if not achou:
                print(f'\nAluno não encontrado!')
        else:
            fun.relatorio_word_grupo(alunos)

    elif escolha == 5:
        fun.planilha_excel(alunos)

    elif escolha == 0:
        break