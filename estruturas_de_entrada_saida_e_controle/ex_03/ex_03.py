# def calcula_area_retangulo():
#     comprimento = float(input("Qual o comprimento do seu retângulo? "))
#     largura = float(input("Qual a largura do seu retângulo? "))
#     return comprimento * largura

# print(calcula_area_retangulo())

# def convert_celsius_for_fahrenheit():
#     celsius = float(input("Qual a temperatura em celsius? "))
#     fahrenheit = celsius * (9/5) + 32
#     return fahrenheit

# print(convert_celsius_for_fahrenheit())

# nome = input("Qual seu nome? ")
# horario = float(input("Que horas são? "))

# def saudacao_horario(nome, horario):
#     if horario < 12:
#         print(f'Bom dia {nome}!')
#     elif horario < 19:
#         print(f'Boa tarde {nome}!')
#     else:
#         print(f'Boa noite {nome}!')

# saudacao_horario(nome, horario)

# def contar_letras(string):
#     qnt_vog = 0
#     qnt_cos = 0
#     string_contagem = string.upper()
#     for i in range(0, len(string)):
#         if string_contagem[i] == "A" or string_contagem[i] == "E" or string_contagem[i] == "I" or string_contagem[i] == "O" or string_contagem[i] == "U":
#             qnt_vog += 1
#         else:
#             qnt_cos += 1
#     return qnt_cos, qnt_vog

# def converter_notas(notas, qnt_notas):
#     for i in range(0, qnt_notas - 1):
#         notas_num = []
#         if notas[i] == 'A':
#             notas_num.append(10)
#         elif notas[i] == 'B':
#             notas_num.append(8)
#         elif notas[i] == 'C':
#             notas_num.append(6)
#         elif notas[i] == 'D':
#             notas_num.append(4)
#         elif notas[i] == 'F':
#             notas_num.append(2)
#     return notas_num

# def converter_data(data):
#     datas = data.split('/')
#     if datas[1] == "01":
#         datas[1] = "de Janeiro de "
#     elif datas[1] == "02":
#         datas[1] = "de Fevereiro de "
#     elif datas[1] == "03":
#         datas[1]  = "de Março de "
#     elif datas[1] == "04":
#         datas[1] = "de Abril de "
#     elif datas[1] == "05":
#         datas[1] = "de Maio de "
#     elif datas[1] == "06":
#         datas[1] = "de Junho de "
#     elif datas[1] == "07":
#         datas[1] = "de Julho de "
#     elif datas[1] == "08":
#         datas[1] = "de Agosto de "
#     elif datas[1] == "09":
#         datas[1] = "de Setembro de "
#     elif datas[1] == "10":
#         datas[1] = "de Outubro de "
#     elif datas[1] == "11":
#         datas[1] = "de Novembro de "
#     elif datas[1] == "12":
#         datas[1] = "de Dezembro de "
#     return(f'{datas[0]} {datas[1]}{datas[2]}')

# def contar_palavras(frase):
#     contador = len(frase.split())
#     return contador

# def soma_dos_quadrados(n):
#     soma = 0
#     for i in range (1, n + 1):
#         soma += i*i
#     return soma

# def primo(num):
#     div = 0
#     for i in range(1, num + 1):
#         if (num % i) == 0:
#             div += 1
#     if div == 2:
#         return True
#     else:
#         return False

# def contar_caracteres(string, car):
#     contador = 0
#     for i in range(0, len(string)):
#         if string[i] == car:
#             contador += 1
#     return contador

# def converter_temperatura(celsius):
#     fahrenheit = celsius * 1.8 + 32
#     kelvin = celsius + 273.15
#     return fahrenheit, kelvin

# def converter_notas(real, taxa_cambio_dolar, taxa_cambio_euro):
#     dolar = real * taxa_cambio_dolar
#     euro = real * taxa_cambio_euro
#     return dolar, euro

# def contar_digitos(num):
#     contador = 0
#     if num < 0:
#         num = -num
#     if num == 0:
#         contador = 1
#     while num != 0:
#         contador += 1
#         num = num // 10
#     return contador

# def eh_palindromo(palavra):
#     palavra_aux = palavra.upper()
#     invertido = palavra_aux[::-1] 
#     if invertido == palavra_aux:
#         return True
#     else:
#         return False

# def par_ou_impar(num):
#     if num % 2 == 0:
#         return "Par"
#     else:
#         return "Impar"

# def maior_de_tres(num1, num2, num3):
#     maior = num1
#     if num2 > maior:
#         maior = num2
#     if num3 > maior:
#         maior = num3
#     if num1 == maior:
#         return num1
#     elif num2 == maior:
#         return num2
#     elif num3 == maior:
#         return num3

# def calcula_preco_final(preco, qnt, frete):
#     valor_final = (preco*qnt) + frete
#     return valor_final

# def potencia(base, expoente):
#     num = 1
#     for i in range(1, expoente + 1):
#         num = num * base
#     return num

# def remover_espacos(frase):
#     frase_nova = ''
#     n = 1
#     for i in range(0, len(frase)):
#         if frase[i] != " ":
#             frase_nova = frase_nova + frase[i]
#             n += 1
#     return frase_nova

# def converter_para_12h(horas):
#     aux = int(horas[:2])
#     if aux >= 13:
#         return f'{aux - 12}h PM'
#     else:
#         return f'{aux}h AM'

# def velocidade_media(dist, tempo):
#     return dist / tempo

# def pedra_papel_tesoura(play1, play2):
#     if (play1 - play2 == 1) or (play1 - play2 == -2):
#         return f'Vitória do Jogador 1'
#     elif play2 == play1:
#         return f'Empate'
#     else:
#         return f'Vitória Jogador 2'
    
# def jogar_dados():
#     import random
#     dado1 = random.randint(1, 6)
#     dado2 = random.randint(1, 6)
#     return dado1 + dado2

# def caca_niquel():
#     import random
#     niquel1 = random.randint(1, 5)
#     niquel2 = random.randint(1, 5)
#     niquel3 = random.randint(1, 5)
#     premio = "R$0,00"
#     if niquel3 == niquel1 and niquel1 == niquel2:
#         premio = "R$10000000,00"
#     return f'Seu prêmio são incriveis, {premio}!'



