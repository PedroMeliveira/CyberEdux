
import sqlite3

conexao = sqlite3.connect('nocoes_de_banco_de_dados/aula_01/aula01.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL
    )
''')

conexao.commit()


def função_escolha(min, max):
    while True:
        try:
            escolha = int(input(f'\nDigite a opção que deseja executar: '))

            while escolha < min or escolha > max:
                print(f'\nEscolha uma opção entre {min} e {max}!')
                escolha = int(input('\nDigite a opção que deseja: '))

            return escolha
        
        except:
            print(f'\nOpção Inválida!')

def adicionar_contatos(qnt):

    for i in range(qnt):
        nome = input(f'\nDigite o nome do {i + 1}º contato: ')
        while nome in contatos:
            print(f'\nEsse nome já está registrado! Tente outro.')
            nome = input(f'\nDigite o nome do {i + 1}º contato: ')

        telefone = input(f'\nDigite o telefone do {i + 1}º contato: ')
        while telefone in contatos.values():
            print(f'\nEsse telefone já está registrado! Tente outro.')
            nome = input(f'\nDigite o nome do {i + 1}º contato: ')

        contatos[nome] = telefone


cursor.execute("SELECT * FROM contatos")
contatos_sql = cursor.fetchall()
contatos = {}
for i in range(len(contatos_sql)):
    contatos[contatos_sql[i][1]] = contatos_sql[i][2]



while True:
    print(f'\nBem vindo a sua Agenda de contatos!\n')
    print(f'1 - Listar Contatos')
    print(f'2 - Adicionar Contato')
    print(f'3 - Remover Contato')
    print(f'0 - Sair')

    escolha = função_escolha(0, 3)

    if escolha == 1:
        if len(contatos) == 0:
            print(f'\nVocê não possui nenhum contato em sua lista.')
        
        else:
            i = 1
            print(f'\n====== LISTA DE CONTATOS ======\n')
            for nome, telefone in contatos.items():
                print(f'{i} - {nome}: {telefone}')
                i += 1

    elif escolha == 2:
        while True:
            try:
                qnt = int(input(f'\nQuantos contatos você deseja adicionar? '))
                adicionar_contatos(qnt)
                break

            except ValueError:
                print(f'\nEntrada inválida! Tente novamente.')


            for nome, telefone in contatos.items():

                cursor.execute("SELECT * FROM contatos")
                contatos_sql = cursor.fetchall()
                
                params = (nome, telefone)

                achou = False

                for i in range(len(contatos_sql)):
                    if nome == contatos_sql[i][1]:
                        achou = True

                if not achou:
                    cursor.execute(f"INSERT INTO contatos (nome, telefone) VALUES (?, ?)", params)

                conexao.commit()

    elif escolha == 3:
        if len(contatos) == 0:
            print(f'\nVocê não possui nenhum contato em sua lista.')
        
        else:
            i = 1
            print(f'\n====== LISTA DE CONTATOS ======\n')
            for nome, telefone in contatos.items():
                print(f'{i} - {nome}: {telefone}')
                i += 1
            while True:
                try:
                    contato_remover = int(input('\nDigite a opção do contato que deseja remover: '))
                    while contato_remover < 1 or contato_remover > len(contatos):
                        print(f'\nNão existe nenhum contato registrado com essa opção! Tente novamente.')
                        contato_remover = int(input('\nDigite a opção do contato que deseja remover: '))

                    del contatos[list(contatos)[contato_remover - 1]]
                    cursor.execute(f"DELETE FROM contatos WHERE nome = {contatos[list(contatos)[contato_remover - 1]]}")

                    break

                except ValueError:
                    print(f'\nOpção Inválida! Tente novamente.')

    else:
        break



