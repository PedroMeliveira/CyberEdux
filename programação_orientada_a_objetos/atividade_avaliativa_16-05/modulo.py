class Pagamento:
    def __init__(self, metodo, valor, data):
        self.metodo = metodo
        self.valor = valor
        self.data = data
        self.status = 'Pendente'
        
    def set_status(self, status):
        self.status = status

def cria_pagamento():
    valor = float(input("Qual o valor do seu pagamento? \n"))
    
    data = input("Qual a data do seu pagamento? \n")
    
    metodo = input("Qual o método do seu pagamento? \n")
    
    return Pagamento(metodo, valor, data)

class Credito():
    def __init__(self, numero, nome, validade, cvv):
        self.numero = numero
        self.nome = nome
        self.validade = validade
        self.cvv = cvv

def cria_credito():
    numero = input("Qual o número do seu cartão? \n")
    
    nome = input("Qual o nome do titular? \n")
    
    validade = input("Qual a data de validade? \n")
    
    cvv = input("Qual o CVV? \n")
    
    return Credito(numero, nome, validade, cvv)
    

class Paypal():
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha
        
    def get_senha(self):
        return self.__senha
    
def cria_paypal():
    email = input("Qual o email? \n")
    
    senha = input("Qual a senha? \n")
    
    return Paypal(email, senha)
    
    
class Bancaria():
    def __init__(self, codigo, origem, destino):
        self.codigo = codigo
        self.origem = origem
        self.destino = destino
        
def cria_bancaria():
    codigo = input("Qual o código do banco? \n")
    
    origem = input("Qual a conta de origem? \n")
    
    destino = input("Qual a conta de destino? \n")
    
    return Credito(codigo, origem, destino)
    
def menu():
    print("=======================================\n")
    print("BEM VINDO AO SISTEMA DE PAGAMENTO\n")
    print("=======================================\n")



    
    
    
    
    
        