import random
import csv   
class Livro:
    def __init__(self, titulo, autor, ano, categoria):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.__isbn = random.randint(1000000000000, 9999999999999)
        self.__disponivel = True
        self.categoria = categoria
    
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
        
    def pegar_emprestado(self, livro, biblioteca):
        if livro in biblioteca.__livros:
            if livro.__disponivel and self.__limite < 3:
                self.__livros_emprestados.append(livro)
                self.__limite += 1
                livro.__disponivel = False
                biblioteca.__historico.append(livro)
                print("Livro emprestado com sucesso!\n")
                
            elif not livro.__disponivel:
                print("Livro não disponível!\n")
            
            else:
                print("Limite de empréstimo superado!\n")
       
        else:
            print("Esse livro não está registrado na biblioteca!\n")     
            
    def devolver_livro(self, livro):
        if livro in self.__livros_emprestados:
            self.__livros_emprestados.remove(livro)
            self.__limite -= 1
            livro.__disponivel = True
            print("Livro devolvido com sucesso!\n")
        
        else:
            print("Livro não esta na sua lista de livros emprestados!\n")
            
            
class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.__livros = []
        self.__usuarios = []
        self.__historico = []
        
    def adicionar_livro(self, livro):
        unico = True
        for liv in self.__livros:
            if livro.__isbn == liv.__isbn:
                unico = False
                print("Não foi possível adicionar, pois ja existe esse livro na biblioteca!\n")
                break
        
        if unico:
            self.__livros.append(livro)
            print("Livro adicionado com sucesso!\n")
            
    def buscar_livro(self, termo):
        for livro in self.__livros:
            if termo == livro.titulo or termo == livro.__isbn or termo == livro.autor:
                return livro
        return None
            
    def registrar_usuario(self, usuario):
        if usuario not in self.__usuarios:
            self.__usuarios.append(usuario)
            print("Usuario registrado com sucesso!\n")
        else:
            print("Esse usuário já está registrado!\n")    

             
    def salvar_dados(self):
        with open('biblioteca_dados.csv', 'w') as csvfile:
            