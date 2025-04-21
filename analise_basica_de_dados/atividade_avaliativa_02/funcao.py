import sqlite3

DADOS = 'dados.db'

conexao = sqlite3.connect(DADOS, check_same_thread=False)
cursor = conexao.cursor()

def criar_tabelas_sql():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clientes (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Email TEXT NOT NULL,
        Senha TEXT NOT NULL
        )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Despesas (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Valor FLOAT,
        Data TEXT NOT NULL,
        Categoria TEXT NOT NULL,
        ID_Cliente INTEGER,
        FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID)
        )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Receitas (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Valor FLOAT,
        Data TEXT NOT NULL,
        Categoria TEXT NOT NULL,
        ID_Cliente INTEGER,
        FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID)
        )
    ''')

    conexao.commit()

def insere_perfil():
    cursor.execute(f"INSERT INTO Clientes (ID, Nome, Email, Senha) VALUES ('1', 'Teste', 'teste@gmail.com', '123123')")
    conexao.commit()