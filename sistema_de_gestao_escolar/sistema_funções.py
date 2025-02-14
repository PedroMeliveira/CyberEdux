def menu():
    print(f'\n======SISTEMA DE GESTÃO ESCOLAR EM TERMINAL======\n')
    print(f'1 - Adicionar Aluno')
    print(f'2 - Remover Aluno')
    print(f'3 - Listar Alunos')
    print(f'4 - Gerar Relatório')
    print(f'5 - Gerar Planilha')
    print(f'0 - Sair\n')
    print(f'==================================================')


def função_escolha(min, max):
    while True:
        try:
            escolha = int(input(f'\nDigite o número da opção que deseja realizar: '))
            while escolha < min or escolha > max:
                print(f'\nNúmero inválido! Digite um número entre {min} e {max}.')
                escolha = int(input(f'\nDigite o número da opção que deseja realizar: '))
            return escolha
        except ValueError:
            print(f'\nEntrada inválida! Tente novamente.')

def adicionar_aluno(lista):
    print(f'\nPreencha as informações do aluno para adicionar-lo ao sistema.')
    nome = input(f'\nNome: ')
    matricula = input(f'\nMatricula: ')
    data = input(f'\nData de Nascimento, (XX/XX/XXXX): ')
    qnt_disc = int(input(f'\nQuantas disciplinas devemos adicionar no registro desse aluno, (Mínimo de 3 disciplinas): '))
    disciplinas = ['Português', 'Matemática', 'Geografia', 'História', 'Física', 'Química', 'Biologia']
    for i, disc in enumerate(disciplinas):
        print(f'{i + 1} - {disc}')
    notas = []
    for i in range(qnt_disc):
        disc = int(input(f'\nOpção da {i + 1}º disciplina: '))
        nota = int(input(f'Nota de {disciplinas[disc - 1]}: '))
        notas.append({disciplinas[disc - 1]: nota})


