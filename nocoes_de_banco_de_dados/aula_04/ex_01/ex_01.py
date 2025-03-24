import sqlite3

conexao = sqlite3.connect('nocoes_de_banco_de_dados/aula_04/biblioteca.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS autores (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL 
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS livroautor (
        livroID INTEGER,
        autorID INTEGER,
        FOREIGN KEY (autorID) REFERENCES autores(ID),
        FOREIGN KEY (livroID) REFERENCES livros(ID)  
    )
''')


cursor.execute(f"INSERT INTO autores (ID, nome) VALUES (1, 'Machado de Assis'), (2, 'Clarice Lispector'), (3, 'J.K. Rowling'), (4, 'George Orwell');")

cursor.execute(f"INSERT INTO livros (ID, titulo) VALUES (1, 'Dom Casmurro'), (2, 'A Hora da Estrela'), (3, 'Harry Potter e a Pedra Filosofal'), (4, '1984'), (6, 'Quincas Borba'), (7, 'O Menino no Espelho'), (8, 'Harry Potter e o Prisioneiro de Azkaban'), (9, 'Revolução dos Bichos');")

cursor.execute(f"INSERT INTO livroautor (livroID, autorID) VALUES (1, 1), (2, 2), (3, 3), (4, 4), (6, 1), (7, 2), (8, 3), (9, 4);")

conexao.commit()