# SISTEMA DE LOGIN
from rich.console import Console
from rich.panel import Panel
import re

perfis = {}

console = Console()

def registrar_perfil():
    while True:    
        console.print(f'\n[red underline]Digite "SAIR" para voltar.')
        login = console.input(f'\n[bold]Digite o seu nome de usuário que será usado como login: ')
        
        while login in perfis:
            login = console.input(f'\n[bold red]Esse nome de usuário já está sendo usado, tente outro nome: ')

        if login.lower() == 'sair':    
            break

        console.print(f'\n[bold green underline]Login válido')

        titulo = (f'[bold]Requisitos [red underline]obrigatórios[/] para criar sua senha:')
        l_1 = (f'\n{" " * 3}[bold]- 8 ou mais caracteres\n')
        l_2 = (f'{" " * 3}[bold]- 1 ou mais números\n')
        l_3 = (f'{" " * 3}[bold]- 1 ou mais letras maiusculas\n')
        l_4 = (f'{" " * 3}[bold]- 1 ou mais letras minusculas\n')
        l_5 = (f'{" " * 3}[bold]- 1 ou mais caracteres especiais\n')
        
        console.print(Panel((f'{l_1}{l_2}{l_3}{l_4}{l_5}'), title=(f'{titulo}'), style="bold", width=80))

        senha = console.input(f'\n[bold]Digite uma senha: ')
        
        while True:
            if validar_senha(senha):
                console.print(f'\n[bold green underline]Senha válida!')
                break

            else:
                senha = console.input(f'\n[bold red]Senha inválida, tente novamente: ')
                
        cpf = console.input(f'\n[bold]Digite o seu CPF, usando o formato [cyan]XXX.XXX.XXX-XX[/]: ')
        
        while True:
            if validar_cpf(cpf):

                if cpf_unico_na_lista(cpf):
                    console.print(f'\n[bold green underline]CPF válido!')
                    break

                else: 
                    cpf = console.input(f'\n[bold red]Esse CPF já possui uma conta existente, tente outro: ')

            else:
                cpf = console.input(f'\n[bold red]CPF inválido, tente novamente: ')

        data = console.input(f'\n[bold]Digite sua data de nascimento, usando o formato [cyan]DD/MM/AAAA[/]: ')
        
        while True:
            if validar_data(data):
                console.print(f'\n[bold green underline]Data de nascimento válida!')
                break

            else:
                data = console.input(f'\n[bold red]Data de nascimento inválida, tente novamente: ')
                
        telefone = console.input(f'\n[bold]Digite um telefone, usando o formato [cyan](XX) 9XXXX-XXXX[/]: ')
        
        while True:
            if validar_telefone(telefone):
                console.print(f'\n[bold green underline]Telefone válido!')
                break

            else: 
                telefone = console.input(f'\n[bold][red]Telefone inválido, tente novamente: ')


        console.print(f'\n[bold][magenta underline]\n\nCadastro realizado!\n\n')

        perfis[login] = {
            "senha": senha,
            "cpf": cpf, 
            "telefone": telefone, 
            "data_nascimento": data, 
            }
        
        break

def validar_senha(senha):
    valido =  True
    if len(senha) < 8:
        valido = False
        console.print(f'\n[bold red underline]A senha possui menos de 8 caracteres!')
        
    pattern = '[\d]'
    if not re.search(pattern, senha):  
        valido = False
        console.print(f'\n[bold red underline]Falta um digito!')
        
    pattern = '[a-z]'
    if not re.search(pattern, senha):   
        valido = False
        console.print(f'\n[bold red underline]Falta uma letra minúscula')
        
    pattern = '[A-Z]'
    if not re.search(pattern, senha):  
        valido = False
        console.print(f'\n[bold red underline]Falta uma letra maiúscula!')
        
    pattern = '[\W_]'
    if not re.search(pattern, senha):   
        valido = False
        console.print(f'\n[bold red underline]Falta um caracter especial!')
        
    return valido

def validar_cpf(cpf):
    pattern = "[\d]{3}[.][\d]{3}[.][\d]{3}[-][\d]{2}"

    if re.search(pattern, cpf):
        return True

    else: 
        return False

def cpf_unico_na_lista(cpf):
    valida = True

    for info in perfis.values():

        if info["cpf"] == cpf:
            valida = False

    return valida

def validar_data(data):
    pattern = "(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19[5-9][0-9]|200[0-6])"

    if re.search(pattern, data):
        return True
    else:
        return False

def validar_telefone(telefone):
    pattern = "[\(][1-9]{2}[\)][ ][9][\d]{4}[-][\d]{4}"

    if re.search(pattern, telefone):
        return True
    else:
        return False
    

def menu_principal():
    console.print('\n')

    titulo = (f'[bold]Bem-Vindo ao Sistema de Login')
    logar = (f'\n{" " * 3}([cyan]1[/])- Entrar em uma conta\n')
    registrar = (f'{" " * 3}([cyan]2[/])- Registrar uma conta\n')

    console.print(Panel((f'{logar}{registrar}'), title=(f'{titulo}'), style="bold", width=80))

def escolher_opcao(min, max):
    while True:
        try:
            escolha = int(console.input(f'\n[bold]Digite a opção que deseja escolher: '))

            while escolha < min or escolha > max:
                console.print(f'\n[bold][red]Opção INVÁLIDA!')
                escolha = int(console.input(f'\n[bold]Digite a opção que deseja escolher: '))

            return escolha

        except ValueError:
            console.print(f'\n[bold][red]Opção INVÁLIDA!')

def verifica_login_senha(login, senha):
    if login.lower() == 'sair':
        return False
    
    if perfis[login]["senha"] == senha:
        return True
    else:
        return False