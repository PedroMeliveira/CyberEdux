
import sqlite3

conexao = sqlite3.connect('nocoes_de_banco_de_dados/aula_01/agenda_contatos.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
        
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS telefones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        contato_id INTEGER REFERENCES contatos(id),
        numero TEXT NOT NULL
        
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

def adicionar_contatos():
    nome = input(f'\nDigite o nome do contato: ')
    cursor.execute(f"INSERT INTO contatos (nome) VALUES ('{nome}')")
    conexao.commit()
    cursor.execute(f"SELECT id FROM contatos WHERE nome='{nome}'")
    contato_id = int(cursor.fetchone()[0])

    while True:
        telefone = input(f'\nDigite o telefone do contato: ')
        cursor.execute(f"INSERT INTO telefones (contato_id, numero) VALUES ('{contato_id}', '{telefone}')")
        resposta = input(f'Deseja adicionar mais telefones? (S/N)').lower()[0]
        if resposta == 'n':

            break
        conexao.commit()



while True:
    print(f'\nBem vindo a sua Agenda de contatos!\n')
    print(f'1 - Listar Contatos')
    print(f'2 - Adicionar Contato')
    print(f'3 - Remover Contato')
    print(f'0 - Sair')

    escolha = função_escolha(0, 3)

    if escolha == 1:
        i = 1
        print(f'\n====== LISTA DE CONTATOS ======\n')
        cursor.execute(f'SELECT * FROM contatos')
        contatos = cursor.fetchall()
        for contato in contatos:
            print(f'{contato[1]}')
            cursor.execute(f"SELECT numero FROM telefones WHERE id='{contato[0]}'")
            numeros = cursor.fetchall()
            print(f'Telefone(s): |', end='')
            for numero in numeros:
                print(f' {numero} |', end='')
            print(f'\n==========================')

    elif escolha == 2:
        adicionar_contatos()

    elif escolha == 3:
        contato_id = int(input(f'Digite o ID do contato que deseja apagar: '))
        cursor.execute(f"DELETE FROM contatos WHERE id ='{contato_id}'")

    else:
        break

cursor.execute(f'SELECT * FROM telefones')
contatos = cursor.fetchall()    
print(contatos)        


