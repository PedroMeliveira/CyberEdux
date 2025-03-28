
from funcoes_calculadora_terminal import *

while True:
    print_menu()
    operação = int(input("Digite o número da operação que deseja realizar: "))
    verifica_num(operação)
    if operação >= 1 and operação < 5:
        num_1 = float(input("Digite o primeiro número que será utilizado na operação: "))
        num_2 = float(input("Digite o segundo número que será utilizado na operação: "))
        if operação == 1:
            print(soma(num_1, num_2))
        if operação == 2:
            print(sub(num_1, num_2))
        if operação == 3:
            print(mult(num_1, num_2))
        if operação == 4:
            print(div(num_1, num_2))
    elif operação == 5:
        a = float(input("Digite seu coeficiente quadrático, (o número que multiplica o x²): "))
        b = float(input("Digite seu coeficiente linear, (o número que multiplica o x): "))
        c = float(input("Digite seu coeficiente constante, (o número que aparece se nenhum x): "))
        print(formula_bhaskara(a, b, c))
    elif operação == 6:
        print_equações()
        eq = input("Digite a equação desejada: ")
        print(eval(eq))
    else:
        break
 
