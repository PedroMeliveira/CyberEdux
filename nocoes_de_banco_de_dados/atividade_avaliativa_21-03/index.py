import sqlite3
from funcoes import *
conexao = sqlite3.connect('nocoes_de_banco_de_dados/atividade_avaliativa_21-03/dados.db')
cursor = conexao.cursor()

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



while True:
    menu()