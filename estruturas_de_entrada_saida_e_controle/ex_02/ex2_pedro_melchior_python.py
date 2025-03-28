# CALCULADORA

# print("1 - Adição")
# print("2 - Subtração")
# print("3 - Multiplicação")
# print("4 - Divisão")
# print("5 - Calcula raízes da função quadrada")
# operação = int(input("Digite o número da operação que deseja realizar: "))
# while operação < 1 or operação > 5:
#     operação = int(input("Digite um número válido: "))
# if operação >= 1 and operação <= 4:
#     num_1 = float(input("Digite o primeiro número que será utilizado na operação: "))
#     num_2 = float(input("Digite o segundo número que será utilizado na operação: "))
#     if operação == 1:
#         print(num_1 + num_2)
#     elif operação == 2:
#         print(num_1 - num_2)
#     elif operação == 3:
#         print(num_1 * num_2)
#     elif operação == 4:
#         print(num_1 / num_2)
# else:
#     a = float(input("Digite seu coeficiente quadrático, (o número que multiplica o x²): "))
#     b = float(input("Digite seu coeficiente linear, (o número que multiplica o x): "))
#     c = float(input("Digite seu coeficiente constante, (o número que aparece se nenhum x): "))
#     delta = b * b - 4 * a * c
#     x1 = (-b + delta ** 0.5)/(2 * a)
#     x2 = (-b - delta ** 0.5)/(2 * a)
#     print("As raízes da função quadratica são: ", x1, "e", x2)

# JOGO PEDRA PAPEL TESOURA

# import random
# jogar =  1
# win = 0
# lose = 0
# draw = 0
# while jogar == 1:
#     print("1 - Pedra,  2 - Papel, 3 - Tesoura: ")
#     escolha = int(input("Digite o número da sua escolha: "))
#     while escolha < 1 and escolha > 3:
#         escolha = int(input("Digite um número entre 1 e 3: "))
#     n = random.randint(1,3)
#     if (escolha - n) == 0:
#         draw += 1
#         print("Empate.")
#         print(f' Vitórias: {win}\n Empates: {draw}\n Derrotas : {lose}')
#         jogar = int(input("Deseja jogar novamente? 1 - Sim, 2 - Não: "))
#         while jogar < 1 and jogar > 2:
#             jogar = int(input("Digite um número entre 1 e 2, (1 - Sim, 2 - Não): "))
#     elif (escolha - n) == -1:
#         lose += 1
#         print("Derrota.")
#         print(f' Vitórias: {win}\n Empates: {draw}\n Derrotas : {lose}')
#         jogar = int(input("Deseja jogar novamente? 1 - Sim, 2 - Não: "))
#         while jogar < 1 and jogar > 2:
#             jogar = int(input("Digite um número entre 1 e 2, (1 - Sim, 2 - Não): "))
#     elif (escolha - n) == 1:
#         win += 1
#         print("Vitória!!!")
#         print(f' Vitórias: {win}\n Empates: {draw}\n Derrotas : {lose}')
#         jogar = int(input("Deseja jogar novamente? 1 - Sim, 2 - Não: "))
#         while jogar < 1 and jogar > 2:
#             jogar = int(input("Digite um número entre 1 e 2, (1 - Sim, 2 - Não): "))
        
# SIMULADOR DE CAIXA ELETRÔNICA

# print("Bem vindo ao seu Caixa Eletrônico")
# senha = input("Digite sua senha: ")
# continuar = 1
# while senha != "12345":
#     senha = input("Senha incorreta! Digite novamente: ")
# saldo = 0.00
# while continuar == 1:
#     print(f'1 - Consultar Saldo \n2 - Depositar\n3 - Sacar')
#     operação = int(input(f'Digite o número da operação que deseja realizar: '))
#     while operação < 1 and operação > 3:
#         operação = int(input(f'Digite um número entre 1 e 3, (1 - Consultar Saldo, 2 - Depositar, 3 - Sacar): '))
#     if operação == 1:
#         print(f'Seu saldo: {saldo}')
#     elif operação == 2:
#         deposito = float(input("Digite o valor a ser depositado: "))
#         saldo = saldo + deposito
#     elif operação == 3:
#         saque = float(f'Digite o valor a ser sacado: ')
#         if saque > saldo:
#             print(f'Você não possui essa quantia, seu saldo atual: {saldo}')
#         else:
#             saldo = saldo - saque
#     print(f'Deseja realizar alguma outra operação?\n1 - Sim\n2 - Não')
#     continuar = int(input())
#     while continuar < 1 and continuar > 2:
#         continuar = int(input(f'Digite um número válido, (1 - Sim, 2 - Não)'))


    


