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
    while True:
        if validar_nome(nome):
            print(f'\nNome válido')
            break
        nome = input(f'\nNome inválido, tente novamente: ')
            
    matricula = input(f'\nMatricula, (XXXXXXXXX): ')
    while True:
        if validar_matricula(matricula):
            print(f'\nMatricula válida!')
            break
        matricula = input(f'\nMatricula inválida, tente novamente: ')

    data = input(f'\nData de Nascimento, (XX/XX/XXXX): ')
    while True:
        if validar_data(data):
            print(f'\nData válida!')
            break
        else:
            data = input(f'\nData inválida, tente novamente: ')

    msg = f'\nQuantas disciplinas devemos adicionar no registro desse aluno, (Mínimo de 3 disciplinas): '
    qnt_disc = função_try_int( msg)
    while qnt_disc < 3:
        print(f'\nNo mínimo 3 disciplinas! ')
        qnt_disc = função_try_int(msg)

    disciplinas = ['Português', 'Matemática', 'Geografia', 'História', 'Física', 'Química', 'Biologia']
    for i, disc in enumerate(disciplinas):
        print(f'{i + 1} - {disc}')

    notas = {}

    for i in range(qnt_disc):
        msg = f'\nOpção da {i + 1}º disciplina: '
        disc = verifica_disc(disciplinas, notas, msg)
        
        msg = f'\nNota de {disciplinas[disc - 1]}: '
        nota = função_try_float(msg)
        while nota < 0 or nota > 10:
            print(f'\nA nota deve ser entre 0 e 10! ')
            nota = função_try_float(msg)
        notas[disciplinas[disc - 1]] = nota

    msg = f'\nQuantas aulas esse aluno já teve? '
    qnt_aulas = função_try_int(msg)
    while qnt_aulas <= 0:
        print(f'\nDigite um valor positivo! ')
        qnt_aulas = função_try_int(msg)

    msg = f'\nQuantas faltas esse aluno já teve? '
    qnt_faltas = função_try_int(msg)
    while qnt_faltas < 0:
        print(f'\nDigite um valor válido! ')
        qnt_faltas = função_try_int(msg)

    lista.append([nome, matricula, data, notas, round(100 * (qnt_faltas/qnt_aulas), 2)])


def validar_data(data):
    pattern = "(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19[5-9][0-9]|202[0-5]|20[0-1][0-9])"

    if re.search(pattern, data):
        return True
    else:
        return False
    
def validar_matricula(matricula):
    if any(chr.isalpha() for chr in matricula) or len(matricula) != 9:
        return False
    return True
    
def validar_nome(nome):
    if any(chr.isdigit() for chr in nome):
        return False
    return True

def função_try_int(msg):
    while True:
        try:
            var = int(input(msg))
            return var
        except ValueError:
            print(f'\nEntrada inválida, tente novamente. ')


def função_try_float(msg):
    while True:
        try:
            var = float(input(msg))
            return var
        except ValueError:
            print(f'\nEntrada inválida, tente novamente. ')


def verifica_disc(disciplinas, lista, msg):
    disc = função_try_int(msg)
    while disciplinas[disc - 1] in lista or (disc < 1 and disc > 7):
        if disciplinas[disc - 1] in lista:
            print(f'\nEssa matéria já foi escolhida, tente outra.')
            disc = função_try_int(msg)

        if disc < 1 and disc > 7:
            print(f'\nEscolha uma opção entre 1 e 7')
            disc = função_try_int(msg)

    return disc

def matricula_unica(matricula, lista):
    for i in len(lista):
        if matricula == lista[i][1]:
            return False
        
    return True