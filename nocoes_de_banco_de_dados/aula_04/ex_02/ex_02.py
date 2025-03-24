import sqlite3

conexao = sqlite3.connect('nocoes_de_banco_de_dados/aula_04/ex_02/Escola.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Alunos (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        DataNascimento TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cursos (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Duracao TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Matriculas (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        AlunoID INTEGER,
        CursoID INTEGER,
        DataMatricula TEXT NOT NULL,
        FOREIGN KEY (AlunoID) REFERENCES Alunos(ID),
        FOREIGN KEY (CursoID) REFERENCES Cursos(ID)             
    )
''')

cursor.execute(f"INSERT INTO Alunos (Nome, DataNascimento) VALUES ('Pedro', '01/02/2006'), ('Mateus', '01/01/1111'), ('Giovana', '25/01/2006')")

cursor.execute(f"INSERT INTO Cursos (Nome, Duracao) VALUES ('Python', '450 Horas'), ('TI', '300 Horas'), ('SQL', '100 Horas')")

cursor.execute(f"INSERT INTO Matriculas (AlunoID, CursoID, DataMatricula) VALUES (1, 1, '29/11/2024'), (2, 2, '09/01/2024'), (3, 1, '12/11/2024'), (3, 3, '12/11/2024')")

conexao.commit()