import sqlite3

def menu():
    print('========================================\n')
    print('Bem vindo ao seu Restaurante Favorito')
    print('1 - Adicionar Prato')
    print('2 - Remover Prato')
    print('3 - Gerenciar Pedidos')
    print('4 - Cardápio')
    print('5 - Fazer Pedido')
    print('0 - Sair/Gerar Relatório Diário\n')
    print('========================================\n')

def escolha(min, max):
    while True:
        try:
            escolha = int(input(f"\nDigite um número entre {min} e {max}: "))
            if max < escolha or escolha < min:
                print(f'\nEntre {min} e {max}...')
            else:
                return escolha
        except:
            print(f'\nEntrada inválida, tente novamente!')

def try_float_positivo(msg):
    while True:
        try:
            num_float = float(input(f'\n{msg}'))
            if 0 > num_float:
                print(f'\nDigite um valor positivo!')
            else:
                return num_float
        except:
            print(f'\nEntrada inválida, tente novamente!')

def try_int_positivo(msg):
    while True:
        try:
            num_int = int(input(f'\n{msg}'))
            if 0 > num_int:
                print(f'\nDigite um valor positivo!')
            else:
                return num_int
        except:
            print(f'\nEntrada inválida, tente novamente!')

# ===========================================================================================

conexao = sqlite3.connect('nocoes_de_banco_de_dados/atividade_avaliativa_21-03/dados.db')
cursor = conexao.cursor()

def cria_tabelas_sql():

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pratos (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Valor FLOAT,
        Tempo_Espera INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Clientes (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT NOT NULL,
            Email TEXT NOT NULL       
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Pedidos (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Cliente_ID INTEGER,
            Endereço TEXT NOT NULL,
            Valor FLOAT,
            Status TEXT NOT NULL,
            Tempo_Entrega INTEGER,
            FOREIGN KEY (Cliente_ID) REFERENCES Clientes(ID)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Avaliacoes (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Pedido_ID INTEGER,
            Nota FLOAT,
            FOREIGN KEY (Pedido_ID) REFERENCES Pedidos(ID)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Relatorios (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Vendas FLOAT,
            Data TEXT NOT NULL           
            FOREIGN KEY (Admin_ID) REFERENCES Admin(ID)   
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Prato_Pedido (
            ID INTEGER PRIMAY KEY AUTOINCREMENT,
            Prato_ID INTEGER,
            Pedido_ID INTEGER
        )
    ''')

    conexao.commit()



def adicionar_prato():
    nome = input(f'\nNome do prato: ')

    valor = try_float_positivo('Preço do prato: ') 

    tempo_espera = try_int_positivo('Tempo de espera: ')

