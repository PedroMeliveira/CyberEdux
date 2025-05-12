import random
import sqlite3

class Livro:
    def __init__(self, titulo, autor, ano, categoria):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.__isbn = random.randint(1000000000000, 9999999999999)
        self.__disponivel = True
        self.categoria = categoria
    
    def get_disponibilidade(self):
        return self.__disponivel
    
    def set_disponibilidade(self, boolean):
        self.__disponivel = boolean
    
    def get_isbn(self):
        return self.__isbn
    
    
    def emprestar(self):
        if self.__disponivel == True:
            self.__disponivel = False
            print("Livro emprestado com sucesso!\n")
        else:
            print("Livro indisponível!")    
    
    def devolver(self):
        if self.__disponivel == True:
            print("Esse livro já estava no estoque!\n")
        else:
            self.__disponivel = True
            print("Livro devolvido com sucesso!\n")
            
    def detalhes(self):
        print(f"{self.titulo} - {self.autor} - {self.ano} - {self.categoria}")
        


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.id = random.randint(1, 100000000000)
        self.__livros_emprestados = []
        self.__limite = 0
        
    def get_livros_emprestados(self):
        return self.__livros_emprestados
    
    def get_limite(self):
        return self.__limite
    
    def pegar_emprestado(self, livro, biblioteca):
        if livro in biblioteca.get_livros():
            if livro.get_disponibilidade() and self.__limite < 3:
                self.__livros_emprestados.append(livro)
                self.__limite += 1
                livro.set_disponibilidade(False)
                biblioteca.set_historico([livro, self])
                print("Livro emprestado com sucesso!\n")
                
            elif not livro.get_disponibilidade():
                print("Livro não disponível!\n")
            
            else:
                print("Limite de empréstimo superado!\n")
       
        else:
            print("Esse livro não está registrado na biblioteca!\n")     
            
    def devolver_livro(self, livro):
        if livro in self.__livros_emprestados:
            self.__livros_emprestados.remove(livro)
            self.__limite -= 1
            livro.set_disponibilidade(True)
            print("Livro devolvido com sucesso!\n")
        
        else:
            print("Livro não esta na sua lista de livros emprestados!\n")

            
class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.__livros = []
        self.__usuarios = []
        self.__historico = []
    
    def get_livros(self):
        return self.__livros
    
    def get_usuarios(self):
        return self.__usuarios
    
    def get_historico(self):
        return self.__historico
    
    def set_historico(self, livro):
        self.__historico.append(livro)
    
    def adicionar_livro(self, livro):
        unico = True
        for liv in self.__livros:
            if livro.get_isbn() == liv.get_isbn():
                unico = False
                print("Não foi possível adicionar, pois ja existe esse livro na biblioteca!\n")
                break
        
        if unico:
            self.__livros.append(livro)
            print(f"Livro adicionado ({livro.titulo}) com sucesso!\n")
            
    def buscar_livro(self, termo):
        for livro in self.__livros:
            if termo == livro.titulo or termo == livro.get_isbn() or termo == livro.autor:
                return livro
        return None
            
    def registrar_usuario(self, usuario):
        if usuario not in self.__usuarios:
            self.__usuarios.append(usuario)
            print("Usuario registrado com sucesso!\n")
        else:
            print("Esse usuário já está registrado!\n")    
    
        
    def criar_dados(self):
        conexao = sqlite3.connect('programação_orientada_a_objetos/atividade_avaliativa_01/dados.db')
        cursor = conexao.cursor()


        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Usuarios (
                ID INTEGER,
                Nome TEXT NOT NULL,
                Limite INTEGER
                )
        ''')
        conexao.commit()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Livros (
                ISBN INTEGER,
                Titulo TEXT NOT NULL,
                Autor TEXT NOT NULL,
                Ano INTEGER,
                Categoria TEXT NOT NULL,
                Disponibilidade INTEGER
                )
            ''')
        conexao.commit()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Historico (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Livro_ISBN INTEGER,
                Usuario_ID INTEGER,
                FOREIGN KEY (Usuario_ID) REFERENCES Usuarios(ID),
                FOREIGN KEY (Livro_ISBN) REFERENCES Livros(ISBN)
                )
            ''')

        conexao.commit()
    
    def salvar_dados(self):
        conexao = sqlite3.connect('programação_orientada_a_objetos/atividade_avaliativa_01/dados.db')
        cursor = conexao.cursor()
        
        for item in self.get_historico():
            cursor.execute(f'INSERT INTO Historico (Livro_ISBN, Usuario_ID) VALUES ({item[0].get_isbn()}, {item[1].id})')
        
        for livro in self.get_livros():
            if livro.get_disponibilidade():
                cursor.execute('INSERT INTO Livros (ISBN, Titulo, Autor, Ano, Categoria, Disponibilidade) VALUES (?, ?, ?, ?, ?, 1)', (livro.get_isbn(), livro.titulo, livro.autor, livro.ano, livro.categoria))
            else:
                cursor.execute('INSERT INTO Livros (ISBN, Titulo, Autor, Ano, Categoria, Disponibilidade) VALUES (?, ?, ?, ?, ?, 0)', (livro.get_isbn(), livro.titulo, livro.autor, livro.ano, livro.categoria))

        for usuario in self.get_usuarios():
            cursor.execute("INSERT INTO Usuarios (ID, Nome, Limite) VALUES (?, ?, ?)", (usuario.id, usuario.nome, usuario.get_limite()))
        
        conexao.commit()
        
    def carregar_dados(self):
        
        
bib_01 = Biblioteca('Cyber Edux')

usuario_01 = Usuario('Pedro')         
usuario_02 = Usuario('Mateus')    
     
livro_01 = Livro('Harry Potter', 'Jack Rowling', 2008, 'Ficção')
livro_02 = Livro('Percy Jackson 1', 'Rick Riordan', 2010, 'Ficção')
livro_03 = Livro('Percy Jackson 2', 'Rick Riordan', 2011, 'Ficção')
livro_04 = Livro('Percy Jackson 3', 'Rick Riordan', 2012, 'Ficção')

bib_01.adicionar_livro(livro_01)
bib_01.adicionar_livro(livro_02)
bib_01.adicionar_livro(livro_03)
bib_01.adicionar_livro(livro_04)

bib_01.registrar_usuario(usuario_01)
bib_01.registrar_usuario(usuario_02)

usuario_01.pegar_emprestado(livro_01, bib_01)
usuario_01.pegar_emprestado(livro_02, bib_01)
usuario_01.pegar_emprestado(livro_03, bib_01)
usuario_02.pegar_emprestado(livro_04, bib_01)

bib_01.criar_dados()
bib_01.salvar_dados()