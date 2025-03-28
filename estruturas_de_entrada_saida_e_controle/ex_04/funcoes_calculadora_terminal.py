
def print_menu():
    print('------------------------------------------------------------------')
    print(' ')
    print("Calculadora de Terminal em Python")
    print(' ')
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Calcula raízes da função quadrada")
    print("6 - Expressão Matemática")
    print("7 - Sair")
    print(' ')
    print('------------------------------------------------------------------')

def verifica_num(num):
    while num < 1 or num > 6:
        num = int(input("Digite um número válido: "))

def soma(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def formula_bhaskara(a, b, c):
    return [(-b + (b * b - 4 * a * c) ** 0.5)/(2 * a), (-b - (b * b - 4 * a * c) ** 0.5)/(2 * a)]

def print_equações():
    print('--------------------------------------------------------------------------------------------')
    print('')
    print('INSTRUÇÕES')
    print('')
    print('1 - Soma use o sinal +')
    print('2 - Substração use o sinal -')
    print('3 - Multiplicação use o sinal *')
    print('4 - Divisão use o sinal /')
    print("5 - Potência use **")
    print("6 - Radiação use **, usando frações, por exemplo raiz quadrada use x**(1/2) ou apenas x**0.5")
    print('')
    print('--------------------------------------------------------------------------------------------')

