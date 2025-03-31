import sqlite3
import re

def menu_out():
    print('========================================\n')
    print("Bem vindo ao seu Restaurante Favorito")
    print("(1) - Login")
    print("(2) - Registrar")
    print("(0) - Sair\n")
    print('========================================\n')

def menu_cliente():
    print('========================================\n')
    print('Bem vindo ao seu Restaurante Favorito')
    print('1 - Cardápio')
    print('2 - Fazer Pedido')
    print('3 - Status do Pedido')
    print('0 - Sair\n')
    print('========================================\n')

def menu_admin():
    print('========================================\n')
    print('1 - Adicionar Prato')
    print('2 - Remover Prato')
    print('3 - Gerenciar Pedidos')
    print('0 - Sair/Gerar Relatório Diário')
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

def validar_senha(senha):
    valido =  True
    if len(senha) < 8:
        valido = False
        print(f'\nA senha possui menos de 8 caracteres!')
        
    pattern = '[\d]'
    if not re.search(pattern, senha):  
        valido = False
        print(f'\nFalta um digito!')
        
    pattern = '[a-z]'
    if not re.search(pattern, senha):   
        valido = False
        print(f'\nFalta uma letra minúscula')
        
    pattern = '[A-Z]'
    if not re.search(pattern, senha):  
        valido = False
        print(f'\nFalta uma letra maiúscula!')
        
    pattern = '[\W_]'
    if not re.search(pattern, senha):   
        valido = False
        print(f'\nFalta um caracter especial!')
        
    return valido




# ===========================================================================================

conexao = sqlite3.connect('nocoes_de_banco_de_dados/atividade_avaliativa_03-21/dados.db')
cursor = conexao.cursor()


def registrar():
    opcao_sair()

    nome_cliente = input(f'\nNome: ')

    if nome_cliente.lower() != 'sair':
        print("\nNome adicionado com sucesso!")

        while True:
            login_cliente = input(f'\nLogin: ')

            cursor.execute("SELECT Login FROM Clientes")
            
            logins = cursor.fetchall()

            if len(logins) > 0:
                tem_igual = False
                for login in logins:
                    if login == login_cliente:
                        print("\nLogin já está em uso, tente outro!")
                        tem_igual = True
                        break
                if not tem_igual:
                    break
        
        print("\nLogin adicionado com sucesso!")            

        senha = input(f'\nDigite uma senha: ')
            
        while True:
            if validar_senha(senha):
                print(f'\nSenha válida!')
                break

            else:
                senha = input(f'\nSenha inválida, tente novamente: ')

        cursor.execute(f"INSERT INTO Clientes (Nome, Login, Senha) VALUES ('{nome_cliente}', '{login_cliente}', '{senha}')")

        conexao.commit()

        print(f"\nConta criada com sucesso, use a opção login para entrar nela!")

    else:
        print("\nSaindo...")

def login():
    opcao_sair()

    cursor.execute(f"SELECT Login, Senha FROM Clientes")
    clientes = cursor.fetchall()

    login = input(f'\nLogin: ')

    encontrou = False

    if login.lower() != 'sair':
        while True and login.lower() != 'sair':
            for cliente in clientes:
                if login == cliente[0]:
                    encontrou = True
                    senha_correta = cliente[1]
                    break 
            if encontrou:
                break
            else:
                login = input("\nLogin não encontrado, tente novamente: ")
        
        if login.lower() != 'sair':
            senha = input(f'\nSenha: ')

            while senha != senha_correta:
                print(f'\nSenha incorreta, tente novamente: ')           
                senha = input(f'\nSenha: ')

            cursor.execute(f"SELECT ID FROM Clientes WHERE Login = '{login}'")
            id_cliente = cursor.fetchone()

            print(f'\nLogin realizado com sucesso!')

            return id_cliente[0]

        else:
            print("\nSaindo...")
    else:
        id_cliente = 'sair'
        print("\nSaindo...")
        return id_cliente
        
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
            Login TEXT NOT NULL,
            Senha TEXT NOT NULL   
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Pedidos (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Cliente_ID INTEGER,
            Status TEXT NOT NULL,
            Endereço TEXT NOT NULL, 
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
            Vendas FLOAT              
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Prato_Pedido (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Prato_ID INTEGER,
            Pedido_ID INTEGER,
            FOREIGN KEY (Prato_ID) REFERENCES Pratos(ID),
            FOREIGN KEY (Pedido_ID) REFERENCES Pedidos(ID)
        )
    ''')

    conexao.commit()

def insert_admin():
    cursor.execute(f'SELECT * FROM Clientes')

    clientes = cursor.fetchall()

    if len(clientes) == 0: 
        cursor.execute(f"INSERT INTO Clientes (ID, Nome, Login, senha) VALUES ('0','admin', 'admin', '123123')")
        conexao.commit()

def insert_cardapio_fixo():
    
    cursor.execute(f'SELECT * FROM Pratos')

    pratos = cursor.fetchall()
    
    if len(pratos) == 0:
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

    print(f'\n===========================================\n')
    print(f'Cardápio\n'.center(40))
    for i, prato in enumerate(pratos):
        print(f'({i + 1}) - {prato[1]}')
    print(f'\n===========================================')




def fazer_pedido(id_cliente):
    opcao_sair()

    endereço = input(f'\nLocal para entrega: ')

    if endereço.lower() != 'sair':
        cursor.execute(f"INSERT INTO Pedidos (Cliente_ID, Status, Endereço) VALUES ('{id_cliente}', 'Realizado', '{endereço}')")
        conexao.commit()

        cursor.execute("SELECT last_insert_rowid()")
        id_pedido = cursor.fetchall()

        cursor.execute(f'SELECT ID, Nome, Valor FROM Pratos')

        pratos = cursor.fetchall()

        pedido = []

        opcao_cardapio()

        while True:
            print(f'\nDigite o número do prato que deseja adicionar')
            escolha_prato = escolha(1, len(pratos))

            for i, prato in enumerate(pratos):
                if i == escolha_prato:
                    pedido.append(prato[0])
                    cursor.execute(f"INSERT INTO Relatorios (Vendas) VALUES ('{prato[2]}')")
                    conexao.commit()

            continua = input(f"\nDeseja adicionar mais pratos ao pedido? (S/N)").lower()[0]
            while continua != 'n' and continua != 's':
                continua = input(f"\nEntrada inválida! Tente novamente, (S/N): ")
            if continua == 'n':
                for id_prato in pedido:
                    cursor.execute(f"INSERT INTO Prato_Pedido (Prato_ID, Pedido_ID) VALUES ('{id_prato}', '{id_pedido}')")
                conexao.commit()
                print(f"\nPedido feito com sucesso! Em breve, ele chegará! ")
                break
                
                
        
def gerenciar_pedidos():
    cursor.execute(f"SELECT * FROM Pedidos")
    pedidos = cursor.fetchall()
    print("\n====ID/Cliente_ID/Status/Endereço=====\n")
    for pedido in pedidos:
        print(f"{pedido[0]} / {pedido[1]} / {pedido[2]} / {pedido[3]}")
    print("\n======================================\n")
    opcao = input("Deseja fazer alguma alteração nos pedidos? (S/N)").lower()[0]
    if opcao == 's':
        while True:
            id_pedido = input("\nDigite o ID do pedido que deseja alterar: ")
            achou = False
            cursor.execute(f"SELECT * FROM Pedidos")
            pedidos = cursor.fetchall()
            for pedido in pedidos:
                if str(id_pedido) == str(pedido[0]):
                    achou = True
            if achou:
                break
            print("\nID não econtrado!")

        novo_status = input("Qual o novo status do pedido? ")

        cursor.execute(f"UPDATE Pedidos SET Status = '{novo_status}' WHERE ID = '{id_pedido}'")
        conexao.commit()

def gerar_relatorio():
    print(f"\nRelatório do dia :")
    cursor.execute(f"SELECT Vendas FROM Relatorios")
    vendas = cursor.fetchall()
    print(vendas)
    print(f"Lucro: {sum(vendas)}")
    print(f"\nSaindo...")

def verificar_status(id_cliente):
    cursor.execute(f"SELECT ID, Status FROM Pedidos WHERE Cliente_ID = '{id_cliente}'")
    status = list(cursor.fetchall())
    for statu in status:
        print(f"\nStatus do Pedido {statu[0]} : {statu[1]}")