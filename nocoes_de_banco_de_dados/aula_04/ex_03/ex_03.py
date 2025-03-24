import sqlite3

conexao = sqlite3.connect('nocoes_de_banco_de_dados/aula_04/ex_03/loja.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clientes (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL
        )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Produtos (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Preco FLOAT
        )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pedidos (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        ClienteID INTEGER,
        Data_do_Pedido TEXT NOT NULL,
        FOREIGN KEY (ClienteID) REFERENCES Clientes(ID)
        )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS PedidoProdutos (
        PedidoID INTEGER,
        ProdutoID INTEGER,
        FOREIGN KEY (PedidoID) REFERENCES Pedidos(ID),
        FOREIGN KEY (ProdutoID) REFERENCES Produtos(ID)
        )
''')

cursor.execute(f"INSERT INTO Clientes (Nome) VALUES ('Pedro'), ('Mateus'), ('Giovana'), ('Brendo')")

cursor.execute(f"INSERT INTO Pedidos (ClienteID, Data_do_Pedido) VALUES (1, '01/02/2022'), (3, '12/12/1212'), (2, '13/11/1222'), (4, '11/11/1111')")

cursor.execute(f"INSERT INTO Produtos (Nome, Preco) VALUES ('Agua', 100.5), ('Coca-COLAAA', 133.33)")

cursor.execute(f"INSERT INTO PedidoProdutos (PedidoID, ProdutoID) VALUES (1, 2), (1, 1), (2, 2), (2, 2), (2, 2)")

conexao.commit()