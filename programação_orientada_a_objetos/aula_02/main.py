class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        
    def envelhecer(self, valor):
        self.idade += valor
    
    @staticmethod
    def eh_adulto(idade):
        return idade >= 18
    
class ContaCorrente:
    def __init__(self, saldo):
        self.__saldo = saldo
        
    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, deposito):
        if deposito > 0:
            self.__saldo += deposito
        else:
            print("Deposito não pode ser negativo!")
            
class ListaDeCompras:
    def __init__(self, itens):
        self.__itens = itens
        
    def adicionar_item(self, item):
        if item != "":
            if item not in self.__itens:
                self.__itens.append(item)
                
    def remover_item(self, item):
        if item in self.__itens:
            self.__itens.remove(item)
        else:
            return False
        
    def mostrar_itens(self):
        for i, item in enumerate(self.__itens):
            print(f"{i + 1} - {item}")
    


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        return f"{self.titulo} de {self.autor}"
    
class Biblioteca:
    def __init__(self, estoque):
        self.__estoque = estoque
        self.__livros_emprestados = {}

    def set_adicionar_livro(self, livro):
        if livro not in self.__estoque:
            self.__estoque.append(livro)    
        else:
            print("Esse livro já está no estoque!\n")
            
    def set_remover(self, livro):
        if livro in self.__estoque:
            self.__estoque.remove(livro) 
        else:
            print("Livro não encontrado!\n")
            
    def listar_livros(self):
        for i, livro in enumerate(self.__estoque):
            print(f"{i + 1} - {livro.titulo} / {livro.autor}")
            
    def buscar_livro(self, titulo):
        for livro in self.__estoque:
            print(livro.titulo, titulo)
            if livro.titulo == titulo:
                return livro
        return None
    
# b = Biblioteca([]) 
# livro1 = Livro('Percy Jackson', 'Rick')
# b.set_adicionar_livro(livro1)
# b.listar_livros()
# l3 = b.buscar_livro('Percy Jackson')
# print(l3.autor)   
    
    
    def emprestar_livro(self, titulo, nome_pessoa):
        achou = False
        for livro in self.__estoque:
            print(livro.titulo, titulo)
            if livro.titulo == titulo:
                achou = True
                break
    
        if titulo in self.__livros_emprestados:
            print("Esse livro não está disponível!\n")

        if achou and titulo not in self.__livros_emprestados:
            self.__livros_emprestados[titulo] = nome_pessoa
            
        if not achou:
            print("Livro não encontrad!\n")
            