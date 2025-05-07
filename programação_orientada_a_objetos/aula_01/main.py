# EX 01

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá me chamo {self.nome}, e eu tenho {self.idade} anos"

from math import pi    
from math import sqrt    
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
        
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, x2, y2):
        return sqrt((x2 - self.x)**2 + (y2 - self.y)** 2)

class Carro:
    def __init__(self, nome, velocidade, aceleração):
        self.nome = nome
        self.velocidade = float(velocidade)
        self.aceleração = float(aceleração)
        self.poder = self.velocidade * (1 + (self.aceleração/100))
    
    def aumentar_velocidade(self, valor):
        if valor > 0:
            self.velocidade += valor
    
    def aumentar_aceleração(self, valor):
        if valor > 0:
            self.aceleração += valor
            
class Pista:
    def __init__(self, carros_possiveis, distancia, carros_na_pista):
        self.carros_possiveis = int(carros_possiveis)
        self.distancia = float(distancia)
        self.carros_na_pista = carros_na_pista
        
    def verifica_disponibilidade(self):
        return len(self.carros_na_pista) < self.carros_possiveis
    
    def adicionar_carro(self, Carro):
        if self.verifica_disponibilidade():
            self.carros_na_pista.append(Carro)
             
class Corrida:
    def __init__(self, local, Pista, premio):
        self.local = local
        self.pista = Pista
        self.premio = float(premio)
 
    def rodar_corrida(self):
        maior_poder = 0
        for carro in self.pista.carros_na_pista:
            if carro.poder > maior_poder:
                maior_poder = carro.poder
                carro_ganhando = carro
        return carro_ganhando
            
        
            
    
            
        
        
        
 