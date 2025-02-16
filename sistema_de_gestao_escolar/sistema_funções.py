import re

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

    matricula = input(f'\nMatricula, (XXXXXXXXX): ')
    while True:
        if validar_matricula(matricula):
            print(f'\nMatricula válida!')
            break
        else:
            matricula = input(f'\nMatricula inválida, tente novamente: ')

    data = input(f'\nData de Nascimento, (XX/XX/XXXX): ')
    while True:
        if validar_data(data):
            print(f'\nData válida!')
            break
        else:
            data = input(f'\nData inválida, tente novamente: ')

    msg = f'\nQuantas disciplinas devemos adicionar no registro desse aluno, (Mínimo de 3 disciplinas): '
    qnt_disc = função_try_int(qnt_disc, msg)
    while qnt_disc < 3:
        print(f'\nNo mínimo 3 disciplinas! ')
        qnt_disc = função_try_int(qnt_disc, msg)

    disciplinas = ['Português', 'Matemática', 'Geografia', 'História', 'Física', 'Química', 'Biologia']
    for i, disc in enumerate(disciplinas):
        print(f'{i + 1} - {disc}')
    notas = {}
    for i in range(qnt_disc):
        msg = f'\nOpção da {i + 1}º disciplina: '
        disc = função_try_int(disc, msg)
        while disc < 1 and disc > 7:
            print(f'\nEscolha uma opção entre 1 e 7')
            disc = função_try_int(disc, msg)

        msg = f'\nNota de {disciplinas[disc - 1]}: '
        nota = função_try_float(nota, msg)
        while nota < 0 and nota > 10:
            print(f'\nA nota deve ser entre 0 e 10! ')
            nota = função_try_float(nota, msg)
        notas[disciplinas[disc - 1]] = nota

    msg = f'\nQuantas aulas esse aluno já teve? '
    qnt_aulas = função_try_int(qnt_aulas, msg)
    while qnt_aulas < 0:
        print(f'\nDigite um valor positivo! ')
        qnt_aulas = função_try_int(qnt_aulas, msg)

    qnt_faltas = int(input(f'\nQuantas faltas esse aluno já teve? '))

    lista.append([nome, matricula, data, notas, 100 * (qnt_faltas/qnt_aulas)])


def validar_data(data):
    pattern = "(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19[5-9][0-9]|202[0-5]|20[0-1][0-9])"

    if re.search(pattern, data):
        return True
    else:
        return False
    
def validar_matricula(matricula):
    if any(chr.isalpha() for chr in matricula) or len(matricula) != 9:
        return False
    else:
        return True

def função_try_int(var, msg):
    while True:
        try:
            var = int(input(msg))
            return var
        except ValueError:
            print(f'\nEntrada inválida, tente novamente. ')


def função_try_float(var, msg):
    while True:
        try:
            var = float(input(msg))
            return var
        except ValueError:
            print(f'\nEntrada inválida, tente novamente. ')