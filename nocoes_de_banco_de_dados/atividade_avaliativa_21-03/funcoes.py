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
            num_int = input(f'\n{msg}')

            if num_int.lower() == 'sair':
                return num_int.lower()
            
            else:
                num_int = int(num_int)

                if 0 > num_int:
                    print(f'\nDigite um valor positivo!')
                else:

                    return num_int
        except:
            print(f'\nEntrada inválida, tente novamente!')

def opcao_sair():
    print(f"\nDigite 'Sair' para voltar.")

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
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Prato_Pedido (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Prato_ID INTEGER,
            Pedido_ID INTEGER
        )
    ''')

    conexao.commit()


def insert_cardapio_fixo():
    cursor.execute(f"INSERT INTO Pratos (Nome, Valor, Tempo_Espera) VALUES ('Hambúrguer Artesanal', '25.90', '15')")
    cursor.execute(f"INSERT INTO Pratos (Nome, Valor, Tempo_Espera) VALUES ('Pizza Marguerita', '39.90', '20')")
    cursor.execute(f"INSERT INTO Pratos (Nome, Valor, Tempo_Espera) VALUES ('Lasanha à Bolonhesa', '34.50', '25')")
    cursor.execute(f"INSERT INTO Pratos (Nome, Valor, Tempo_Espera) VALUES ('Frango Grelhado com Legumes', '28.00', '20')")
    cursor.execute(f"INSERT INTO Pratos (Nome, Valor, Tempo_Espera) VALUES ('Risoto de Cogumelos', '32.00', '30')")
    cursor.execute(f"INSERT INTO Pratos (Nome, Valor, Tempo_Espera) VALUES ('Refrigerante (Coca-Cola)', '6.00', '0')")
    cursor.execute(f"INSERT INTO Pratos (Nome, Valor, Tempo_Espera) VALUES ('Suco Natural de Laranja', '8.00', '0')")
    cursor.execute(f"INSERT INTO Pratos (Nome, Valor, Tempo_Espera) VALUES ('Água Mineral (500ml)', '3.50', '0')")
    cursor.execute(f"INSERT INTO Pratos (Nome, Valor, Tempo_Espera) VALUES ('Sorvete de Chocolate', '12.00', '5')")
    cursor.execute(f"INSERT INTO Pratos (Nome, Valor, Tempo_Espera) VALUES ('Pudim de Leite Condensado', '10.00', '10')")

    conexao.commit()

def adicionar_prato():
    opcao_sair()
    
    nome = input(f'\nNome do prato: ')
    
    if nome.lower() != 'sair':

        valor = try_float_positivo('Preço do prato: ') 

        tempo_espera = try_int_positivo('Tempo de espera: ')

        cursor.execute(f"INSERT INTO Pratos (Nome, Valor, Tempo_Espera) VALUES ('{nome}', '{valor}', '{tempo_espera}')")

        conexao.commit()

        print(f'\nPrato adicionado com sucesso! ')

def remover_prato():
    while True:
        opcao_sair()

        id = try_int_positivo(f'ID do prato a ser removido: ')

        if str(id) == 'sair':
            break

        cursor.execute(f'SELECT ID, Nome FROM Pratos')

        pratos = cursor.fetchall()

        achou_prato = False

        for prato in pratos:
            if id == prato[0]:
                while True:
                    escolha = try_int_positivo(f'Deseja remover o Prato: {prato[0]} - {prato[1]}? [(1) - Sim, (2) - Não]: ')
                    
                    if escolha == 1:
                        cursor.execute(f"DELETE FROM Pratos WHERE ID = {id}")

                        conexao.commit()
                        
                        print(f'\nPrato removido com sucesso! ') 

                        break
                    
                    elif escolha == 2:
                        print(f'\nOk, prato NÃO foi removido. \n')

                        break

                    else:
                        print(f'\nDigite uma opção válida. ')
            
            achou_prato = True

        if not achou_prato:
            print(f'\nEsse ID não está nos registros de pratos. Tente novamente! ')
        
        else:
            break

def opcao_cardapio():
    cursor.execute(f'SELECT ID, Nome FROM Pratos')

    pratos = cursor.fetchall()

    print(f'\n===========================================')
    for i, prato in enumerate(pratos):
        print(f'({i + 1}) - {prato}')
    print(f'\n===========================================')


def fazer_pedido():
    opcao_sair()

    nome_cliente = input(f'\nNome: ')
    
    if nome_cliente.lower() != 'sair':
        email = input(f'\nEmail: ')

        endereço = input(f'\nLocal para entrega: ')

        while True:
            opcao_cardapio()

            cursor.execute(f'SELECT ID, Nome FROM Pratos')

            pratos = cursor.fetchall()
            
            prato = escolha(1, len(pratos))