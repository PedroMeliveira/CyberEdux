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

    def set_saldo(self, deposito)
        if deposito > 0:
            self.__saldo += deposito
        else:
            print("Deposito não pode ser negativo!")
            