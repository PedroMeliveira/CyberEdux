# EX 01

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá me chamo {self.nome}, e eu tenho {self.idade} anos"

from math import pi    
class Circulo:
    def __init__(self, raio):
        self.raio = float(raio)
    
    def area(self):
        return pi * self.raio ** 2    

    def circunferencia(self):
        return pi * self.raio * 2
    
class Cachorro:
    def __init__(self, nome, raça):
        self.nome = nome
        self.raça = raça
    
    def latir(self):
        print(f"{self.nome}: AU AUA AUAAUAUAU")
        
        
        
class Calculadora:
    def __init__(self, num_inicial):
        self.num_inicial = num_inicial

    def somar(self, num):
        return self.num_inicial + num

    def subtrair(self, num):
        return self.num_inicial - num
    
    def multiplicar(self, num):
        return self.num_inicial * num
    
    def dividir(self, num):
        if num != 0:
            return self.num_inicial / num
        return f"Entrada inválida"

class ContaBancaria:
    def __init__(self, saldo, titular):
        self.saldo = float(saldo)
        self.titular = titular
    
    def depositar(self, valor):
        self.saldo += valor
        return f"Novo saldo: {self.saldo}"
    
    def sacar(self, valor):
        if valor > self.saldo:
            return f"Você não possui esse valor na sua conta"
        self.saldo -= valor
        return f"Novo saldo: {self.saldo}"

class Livro:
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor

    def detalhes(self):
        return f"{self.nome} de {self.autor}"
    
class Biblioteca:
    def __init__(self, estoque):
        self.estoque = estoque

    def adicionar(self, livro):
        self.estoque.append(livro)

    def remover(self, livro):
        self.estoque.remove(livro) 

    def listar(self):
        for livro in self.estoque:
            print(livro.autor)

# canids = Biblioteca([])
# livro1 = Livro('Harry Potter', 'Jake Role')
# livro2 = Livro('Percy Jackson', 'Rick Riordao')
# canids.adicionar(livro1)
# canids.adicionar(livro2)
# canids.listar()
# canids.remover(livro1)
# canids.listar()
        
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
        
        
