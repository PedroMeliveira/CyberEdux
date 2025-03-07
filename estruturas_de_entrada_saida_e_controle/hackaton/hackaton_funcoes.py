from rich.console import Console
from rich.panel import Panel
import re


console = Console()


############################################### Funções de escolha


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
    

def confirmacao_s_ou_n():
    confirmacao = console.input(f'[bold]Deseja confirmar? [magenta](S/N): ').lower()

    while confirmacao != 's' and confirmacao != 'n':
        console.print(f'[bold][red]Opção INVÁLIDA!')
        confirmacao = console.input(f'\n[bold]Deseja confirmar? [magenta](S/N): ').lower()

    return confirmacao


def filtra_valor():
    while True:
        try:
            valor = float(console.input(f''))

            while valor <= 0:
                console.print(f'\n[bold][red]Quantia Inválida!')
                valor = float(console.input(f'\n[bold]Digite uma nova quantia válida: '))

            return valor

        except ValueError:
            console.print(f'\n[bold][red]Opção INVÁLIDA!')
            console.print(f'\n[bold]Digite uma nova quantia válida:', end=' ')   


def filtra_valor_int():
    while True:
        try:
            valor = int(console.input(f''))

            while valor <= 0:
                valor = int(console.input(f'\n[bold][red]Digite um valor válido: '))

            return valor

        except ValueError:
            console.print(f'\n[bold][red]Opção INVÁLIDA!')
            console.print(f'[bold]Digite um valor válido:', end=' ') 


############################################### Validadores de usuário


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
            "financeiro":{
                "moeda_atual": "Real Brasileiro",
                "simbolo": "R$",
                "para_real": 1,
                "saldo": 0, 
                "transferencias": [], 
                "despesas": {
                    "Alimentação": 0, 
                    "Lazer": 0, 
                    "Transporte": 0, 
                    "Outros": 0, 
                    "Total": 0
                    }
                }
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
    
def verifica_login_senha(login, senha):
    if login.lower() == 'sair':
        return False
    
    if perfis[login]["senha"] == senha:
        return True
    else:
        return False


############################################### Ações Admin


def info_cliente():
    while True:
        cliente = console.input(f'\n[bold]Deseja ver as informações de qual cliente? ')
        tentativas = 5
        while cliente not in perfis or cliente == 'admin':
            cliente = console.input(f'\n[bold red]Esse cliente não está cadastrado como um cliente [magenta underline]Noob Bank[/], tente outro: ')
            tentativas -= 1
            if tentativas == 0:
                break
        
        if tentativas != 0:
            console.print('\n')

            titulo = (f'[bold magenta] Informações do cliente: [cyan]{cliente}[/]')
            l_1 = (f'\nSenha: [cyan]{perfis[cliente]["senha"]}[/]\n')
            l_2 = (f'CPF: [cyan]{perfis[cliente]["cpf"]}[/]\n')
            l_3 = (f'Telefone: [cyan]{perfis[cliente]["telefone"]}[/]\n')
            l_4 = (f'Data de Nascimento: [cyan]{perfis[cliente]["data_nascimento"]}[/]\n')
            l_5 = (f'Moeda atual: [cyan]{perfis[cliente]["financeiro"]["moeda_atual"]}[/]\n')
            l_6 = (f'Saldo: [cyan]{perfis[cliente]["financeiro"]["simbolo"]}{perfis[cliente]["financeiro"]["saldo"]}[/]\n')

            console.print(Panel((f'{l_1}{l_2}{l_3}{l_4}{l_5}{l_6}'), style="bold", title=(f'{titulo}'), width=80))

        break


############################################### Ações Usuário


def deposito(login):
    while True:
        console.print(f'\n[bold]Digite a quantia que deseja adicionar ao seu saldo:', end=' ')

        deposito = filtra_valor()

        console.print(f'\n[bold]Valor a depositar: [magenta]{perfis[login]["financeiro"]["simbolo"]}{deposito}[/]')
        confirmacao = confirmacao_s_ou_n()

        if confirmacao == 's':
            perfis[login]["financeiro"]["saldo"] += deposito
            perfis[login]["financeiro"]["transferencias"].append(deposito)

        break

def saque(login):
    while True:
        console.print(f'\n[bold]Digite a quantia que deseja retirar do seu saldo:', end=' ')

        saque = filtra_valor()
        
        console.print(f'\n[bold]Valor a sacar: [magenta]{perfis[login]["financeiro"]["simbolo"]}{saque}[/]')
        confirmacao = confirmacao_s_ou_n()

        if confirmacao == 's':
            perfis[login]["financeiro"]["saldo"] -= saque
            perfis[login]["financeiro"]["transferencias"].append(-saque)

        break

def registrar_gasto(login):
    while True:
        console.print(f'\n[bold]Digite a quantia que deseja registrar como gasto:', end=' ')

        gasto = filtra_valor()

        console.print(f'\n{" " * 3}[bold cyan underline]Categorias disponíveis:')
        categorias = ['Alimentação', 'Transporte', 'Lazer', 'Outros']

        for i in range(len(categorias)):
            console.print(f'\n{" " * 3}[bold]([cyan]{i + 1}[/])- {categorias[i]}')

        categoria = escolher_opcao(1, 4)

        console.print(f'\n[bold]Valor inserido: [magenta]{perfis[login]["financeiro"]["simbolo"]}{gasto}')
        console.print(f'[bold]Categoria selecionada: [cyan]{categorias[categoria - 1]}')

        confirmacao = confirmacao_s_ou_n()

        if confirmacao == 's':
            perfis[login]["financeiro"]["transferencias"].append(-gasto)
            perfis[login]["financeiro"]["saldo"] -= gasto
            perfis[login]["financeiro"]["despesas"][categorias[categoria - 1]] += gasto
            perfis[login]["financeiro"]["despesas"]["Total"] += gasto

        break

def relatorio_gasto(login):
    if perfis[login]["financeiro"]["despesas"]["Total"] == 0: 
        console.print(f'\n[bold red]Você ainda não registrou nenhum gasto!')

    else:
        
        console.print(f'\n[bold cyan underline]Relatório de gastos\n')
        for chave, valor in perfis[login]["financeiro"]["despesas"].items():

            if chave != "Total":
                console.print(f'{" " * 3}[bold]{chave}: [cyan]{perfis[login]["financeiro"]["simbolo"]}{valor}[/]')
            
                if perfis[login]["financeiro"]["despesas"]["Total"] != 0:
                    console.print(f'{" " * 3}[bold]>>>   [magenta]|{'|' * int((valor/perfis[login]["financeiro"]["despesas"]["Total"] * 50))} {round(valor/perfis[login]["financeiro"]["despesas"]["Total"] * 100, 2)}%\n')
                else:
                    console.print(f'{" " * 3}| 0%')

        console.print(f'{" " * 3}[bold][underline]Total[/]: [cyan]{perfis[login]["financeiro"]["simbolo"]}{perfis[login]["financeiro"]["despesas"]["Total"]}')


def transferencia(login):
    while True:
        destino = console.input(f'\n[bold]Digite o nome do usuário para quem deseja transferir seu dinheiro: ')

        tentativas = 5
        while destino not in perfis or destino == login or destino == 'admin':
            destino = console.input(f'\n[bold red]Esse usuário ou não pode receber transferências da sua conta ou ele não é um cliente [bold magenta underline]Noob Bank[/], tente outro: ')
            tentativas -= 1

            if tentativas == 0:
                break
        
        if tentativas != 0:
            console.print(f'\n[bold]Digite o valor da transferência:', end=' ')
            quantia = filtra_valor()

            console.print(f'\n[bold]Você está enviando [magenta]{perfis[login]["financeiro"]["simbolo"]}{quantia}[/] para [cyan]{destino}')
            confirmacao = confirmacao_s_ou_n()

            if confirmacao == 's':
                def converte_quantia_transferencia(login, moedas, quantia):

                    quantia = quantia * perfis[login]["financeiro"]["para_real"]
                    moeda_destino = perfis[destino]["financeiro"]["moeda_atual"]
                    real_para_destino = moedas[moeda_destino]["real_para"]
                    quantia = round(quantia * real_para_destino, 2)
                    return quantia

                perfis[login]["financeiro"]["saldo"] -= quantia
                perfis[login]["financeiro"]["transferencias"].append(-quantia)
                quantia = converte_quantia_transferencia(login, moedas, quantia)
                perfis[destino]["financeiro"]["saldo"] += quantia
                perfis[destino]["financeiro"]["transferencias"].append(quantia)

                console.print(f'\n[bold magenta underline]Transferência realizada com sucesso!')

        break 


def extrato_periodo(login):
    if len(perfis[login]["financeiro"]["transferencias"]) == 0:
        console.print(f'\n[bold red]Você ainda não tem nenhuma ação monetária registrada como extrato!\n')

    else: 

        qntd_acoes = int(console.input(f'\n[bold]Digite a quantidade de extratos que deseja ver: '))

        while qntd_acoes < 1:
            console.print(f'\n[bold red]Valor [underline]INVÁLIDO[/]!\n')
            qntd_acoes = int(console.input(f'[bold]Insira um novo valor: '))

        console.print(f'\n[bold cyan underline]Extratos:\n')

        i = qntd_acoes
        while i > 0:
        
            if qntd_acoes > len(perfis[login]["financeiro"]["transferencias"]):
                qntd_acoes = len(perfis[login]["financeiro"]["transferencias"])
                i = qntd_acoes

            if perfis[login]["financeiro"]["transferencias"][-i] > 0:
                console.print(f'{" " * 3}[bold green][underline]Receita[/] de [magenta]{perfis[login]["financeiro"]["simbolo"]}{perfis[login]["financeiro"]["transferencias"][-i]}')

            else:
                console.print(f'{" " * 3}[bold red][underline]Despesa[/] de [magenta]{perfis[login]["financeiro"]["simbolo"]}{-perfis[login]["financeiro"]["transferencias"][-i]}')
            i -= 1


def alterar_moeda_padrao(login):
    while True:
        
        titulo = (f'[bold magenta]Alterar moeda padrão')
        l_1 = (f'\n{" " * 3}Moeda atual: [cyan]{perfis[login]["financeiro"]["moeda_atual"]}[/]\n')
        l_2 = (f'\n{" " * 3}([cyan]1[/])- Dólar Americano\n')
        l_3 = (f'{" " * 3}([cyan]2[/])- Euro\n')
        l_4 = (f'{" " * 3}([cyan]3[/])- Iene Japonês\n')
        l_5 = (f'{" " * 3}([cyan]4[/])- Rúpia Indiana\n')
        l_6 = (f'{" " * 3}([cyan]5[/])- Won Coreano\n')
        l_7 = (f'{" " * 3}([cyan]6[/])- Real Brasileiro\n')
        l_8 = (f'{" " * 3}([cyan]7[/])- Voltar\n')

        console.print(Panel((f'{l_1}{l_2}{l_3}{l_4}{l_5}{l_6}{l_7}{l_8}'), style="bold", title=(f'{titulo}'), width=80))
        
        moeda_escolha = escolher_opcao(1, 7)

        if moeda_escolha == 7:
            break

        for moeda_atual in moedas.values():
            if moeda_atual["id"] == moeda_escolha - 1:
                break

        console.print(f'\n[bold]Moeda escolhida: [cyan]{moeda_atual["nome"]}')
        console.print(f'[bold]Símbolo monetário: [cyan]{moeda_atual["simbolo"]}')

        confirmacao = confirmacao_s_ou_n()

        if confirmacao == 's':
            perfis[login]["financeiro"]["moeda_atual"] = moeda_atual["nome"]
            perfis[login]["financeiro"]["simbolo"] = moeda_atual["simbolo"]
            perfis[login]["financeiro"]["saldo"] = perfis[login]["financeiro"]["saldo"] * perfis[login]["financeiro"]["para_real"]
            perfis[login]["financeiro"]["saldo"] = round(perfis[login]["financeiro"]["saldo"] * moeda_atual["real_para"], 2)

            for categoria in perfis[login]["financeiro"]["despesas"].keys():
                perfis[login]["financeiro"]["despesas"][categoria] = perfis[login]["financeiro"]["despesas"][categoria] * perfis[login]["financeiro"]["para_real"]
                perfis[login]["financeiro"]["despesas"][categoria] = round(perfis[login]["financeiro"]["despesas"][categoria] * moeda_atual["real_para"], 2)

            perfis[login]["financeiro"]["para_real"] = moeda_atual["para_real"]

        break

def simulador_investimento(login):
    while True:

        menu_investimento()
        escolha = escolher_opcao(1, 3)

        if escolha == 3:
            break

        console.print(f'\n[bold]Digite o valor do investimento inicial:', end=' ')

        valor = filtra_valor()

        console.print(f'\n[bold]Digite a taxa de rendimento em porcentagem, ([cyan underline]Ex: 5.5%, digite apenas o número 5.5[/]):', end=' ')

        taxa = filtra_valor()/100

        def simulador_rendimento(valor, taxa, tempo):
            valor_bruto = valor + (1 + taxa) ** tempo
            valor_juros = valor_bruto - valor
            valor_imposto = valor_juros * 0.15
            valor_liquido = valor_bruto - valor_imposto
            return valor_bruto, valor_juros, valor_imposto, valor_liquido

        def print_relatorio_investimento(valor, valor_bruto, valor_juros, valor_imposto, valor_liquido):

            titulo = (f'[bold]Relatório de Investimentos [magenta underline]Noob Bank[/]\n')
            l_1 = (f'\n{" " * 3}Valor inicial investido: [magenta]{perfis[login]["financeiro"]["simbolo"]}{valor}[/]\n')
            l_2 = (f'{" " * 3}Valor total bruto: [magenta]{perfis[login]["financeiro"]["simbolo"]}{round(valor_bruto, 2)}[/]\n')
            l_3 = (f'{" " * 3}Valor em juros: [magenta]{perfis[login]["financeiro"]["simbolo"]}{round(valor_juros, 2)}[/]\n')
            l_4 = (f'{" " * 3}Valor pago em imposto de renda: [magenta]{perfis[login]["financeiro"]["simbolo"]}{round(valor_imposto, 2)}[/]\n')
            l_5 = (f'{" " * 3}Valor total líquido: [magenta]{perfis[login]["financeiro"]["simbolo"]}{round(valor_liquido, 2)}[/]\n')

            console.print(Panel((f'\n{l_1}{l_2}{l_3}{l_4}{l_5}'), title=(f'{titulo}'), style="bold", width=80))

        if escolha == 1:
            while True:
                console.print(f'\n[bold cyan underline]Opções de tempo disponíveis:')
                console.print(f'\n{" " * 3}[bold]([cyan]1[/])- Simulação de 1 meses')
                console.print(f'{" " * 3}[bold]([cyan]2[/])- Simulação de 3 meses')
                console.print(f'{" " * 3}[bold]([cyan]3[/])- Simulação de 6 meses')
                console.print(f'{" " * 3}[bold]([cyan]4[/])- Simulação de tempo personalizado')
                console.print(f'{" " * 3}[bold]([cyan]5[/])- Voltar')

                opcao_tempo = escolher_opcao(1, 5)

                if opcao_tempo == 1:
                    valor_bruto, valor_juros, valor_imposto, valor_liquido = simulador_rendimento(valor, taxa, 1)
                    print_relatorio_investimento(valor, valor_bruto, valor_juros, valor_imposto, valor_liquido)

                elif opcao_tempo == 2:
                    valor_bruto, valor_juros, valor_imposto, valor_liquido = simulador_rendimento(valor, taxa, 3)
                    print_relatorio_investimento(valor, valor_bruto, valor_juros, valor_imposto, valor_liquido)

                elif opcao_tempo == 3:
                    valor_bruto, valor_juros, valor_imposto, valor_liquido = simulador_rendimento(valor, taxa, 6)
                    print_relatorio_investimento(valor, valor_bruto, valor_juros, valor_imposto, valor_liquido)

                elif opcao_tempo == 4:
                    console.print(f'[bold]Digite o período em que sua taxa funciona, ([cyan underline]Ex: 4 Meses, digite apenas o número 4[/]):', end=' ')

                    tempo = filtra_valor_int()
                    
                    valor_bruto, valor_juros, valor_imposto, valor_liquido = simulador_rendimento(valor, taxa, tempo)
                    print_relatorio_investimento(valor, valor_bruto, valor_juros, valor_imposto, valor_liquido)

                elif opcao_tempo == 5:
                    break
                
                break

        if escolha == 2:
            while True:
                console.print(f'\n[bold cyan underline]Opções de tempo disponíveis:')
                console.print(f'\n{" " * 3}[bold]([cyan]1[/])- Simulação de 1 ano')
                console.print(f'{" " * 3}[bold]([cyan]2[/])- Simulação de 5 anos')
                console.print(f'{" " * 3}[bold]([cyan]3[/])- Simulação de 10 anos')
                console.print(f'{" " * 3}[bold]([cyan]4[/])- Simulação de tempo personalizado')
                console.print(f'{" " * 3}[bold]([cyan]5[/])- Voltar')

                opcao_tempo = escolher_opcao(1, 5)

                if opcao_tempo == 1:
                    valor_bruto, valor_juros, valor_imposto, valor_liquido = simulador_rendimento(valor, taxa, 1)
                    print_relatorio_investimento(valor, valor_bruto, valor_juros, valor_imposto, valor_liquido)

                elif opcao_tempo == 2:
                    valor_bruto, valor_juros, valor_imposto, valor_liquido = simulador_rendimento(valor, taxa, 5)
                    print_relatorio_investimento(valor, valor_bruto, valor_juros, valor_imposto, valor_liquido)

                elif opcao_tempo == 3:
                    valor_bruto, valor_juros, valor_imposto, valor_liquido = simulador_rendimento(valor, taxa, 10)
                    print_relatorio_investimento(valor, valor_bruto, valor_juros, valor_imposto, valor_liquido)

                elif opcao_tempo == 4:
                    console.print(f'[bold]Digite o período em que sua taxa funciona, ([cyan underline]Ex: 4 Anos, digite apenas o número 4[/]):', end=' ')

                    tempo = filtra_valor_int()
  
                    valor_bruto, valor_juros, valor_imposto, valor_liquido = simulador_rendimento(valor, taxa, tempo)
                    print_relatorio_investimento(valor, valor_bruto, valor_juros, valor_imposto, valor_liquido)
                
                elif opcao_tempo == 5:
                    break
                
                break


############################################### Menus


def menu_principal():
    console.print('\n')

    titulo = (f'[bold]Bem-Vindo ao Banco [magenta underline]Noob Bank')
    logar = (f'\n{" " * 3}([cyan]1[/])- Entrar em uma conta\n')
    registrar = (f'{" " * 3}([cyan]2[/])- Registrar uma conta\n')

    console.print(Panel((f'{logar}{registrar}'), title=(f'{titulo}'), style="bold", width=80))


def menu_admin():
    console.print('\n')

    titulo = (f'[bold]Painel de Administrador [magenta underline]Noob Bank')
    l_1 = (f'\n{" " * 3}([cyan]1[/])- Consultar informações de um cliente específico\n')
    l_2 = (f'{" " * 3}([cyan]2[/])- Sair da conta\n')
    l_3 = (f'{" " * 3}[red]([cyan]3[/])- Desligar a máquina\n')

    console.print(Panel((f'{l_1}{l_2}{l_3}'), title=(f'{titulo}'), style="bold", width=80))


def menu_cliente(login):
    console.print('\n')

    if perfis[login]["financeiro"]["saldo"] >= 0:
        l_1 = (f'\n{" " * 3}Saldo atual: [green]{perfis[login]["financeiro"]["simbolo"]}{perfis[login]["financeiro"]["saldo"]}[/]\n')

    else:
        l_1 = (f'\n{" " * 3}Saldo atual: [red]{perfis[login]["financeiro"]["simbolo"]}{perfis[login]["financeiro"]["saldo"]}[/]\n')

    titulo = (f'[bold]Gerenciador Financeiro [magenta underline]Noob Bank')
    l_2 = (f'\n{" " * 3}([cyan]1[/])- Depósito\n')
    l_3 = (f'{" " * 3}([cyan]2[/])- Saque\n')
    l_4 = (f'{" " * 3}([cyan]3[/])- Transferência para outro cliente Noob Bank\n')
    l_5 = (f'{" " * 3}([cyan]4[/])- Extrato com filtros por período\n')
    l_6 = (f'{" " * 3}([cyan]5[/])- Simulação de investimento com rendimento fixo\n')
    l_7 = (f'{" " * 3}([cyan]6[/])- Registrar gasto\n')
    l_8 = (f'{" " * 3}([cyan]7[/])- Relatório de gasto\n')
    l_9 = (f'{" " * 3}([cyan]8[/])- Alterar moeda padrão\n')
    l_10 = (f'{" " * 3}([cyan]9[/])- Sair da conta\n')

    console.print(Panel((f'{l_1}{l_2}{l_3}{l_4}{l_5}{l_6}{l_7}{l_8}{l_9}{l_10}'), title=(f'{titulo}'), style="bold", width=80))


def menu_investimento():
    console.print('\n')

    titulo = (f'[bold]Simulador de investimentos [magenta underline]Noob Bank[/]')
    l_1 = (f'\n{" " * 3}Escolha a forma como deseja simular seu Rendimento:\n')
    l_2 = (f'\n{" " * 3}([cyan]1[/])- Rendimento Mensal\n')
    l_3 = (f'{" " * 3}([cyan]2[/])- Rendimento Anual\n')
    l_4 = (f'{" " * 3}([cyan]3[/])- Voltar\n')

    console.print(Panel((f'{l_1}{l_2}{l_3}{l_4}'), title=(f'{titulo}'), style="bold", width=80))



############################################### Dicionários


perfis = {
    "admin": {
        "senha": "123",
        "cpf": "0"
        },
    "mateus": {
        "senha": "Mateus12!",
        "cpf": "123.123.123-12", 
        "telefone": "(65) 91010-1010", 
        "data_nascimento": "12/12/2002", 
        "financeiro":{
            "moeda_atual": "Real Brasileiro",
            "simbolo": "R$",
            "para_real": 1,
            "saldo": 0, 
            "transferencias": [], 
            "despesas": {
                "Alimentação": 0, 
                "Lazer": 0, 
                "Transporte": 0, 
                "Outros": 0, 
                "Total": 0
                }
            }
        },
        "pedro":{
            "senha": "Pedro12!",
            "cpf": "123.123.143-12", 
            "telefone": "(65) 91010-1310", 
            "data_nascimento": "12/12/2001", 
            "financeiro":{
                "moeda_atual": "Real Brasileiro",
                "simbolo": "R$",
                "para_real": 1,
                "saldo": 0, 
                "transferencias": [], 
                "despesas": {
                    "Alimentação": 0, 
                    "Lazer": 0, 
                    "Transporte": 0, 
                    "Outros": 0, 
                    "Total": 0
                }
            }
        }           
    }


moedas = {
    "Dólar Americano": {
        "id": 0,
        "nome": "Dólar Americano",
        "simbolo": '$',
        "para_real": 6.1273,
        "real_para": 0.1632
    },
    "Euro": {
        "id": 1,
        "nome": "Euro",
        "simbolo": '€',
        "para_real": 6.43,
        "real_para": 0.15555
    },
    "Iene Japonês": {
        "id": 2,
        "nome": "Iene Japonês",
        "simbolo": '¥',
        "para_real": 0.039773,
        "real_para": 25.1423
    },
    "Rúpia Indiana": {
        "id": 3,
        "nome": "Rúpia Indiana",
        "simbolo": '₹',
        "para_real": 0.07198,
        "real_para": 13.8954
    },
    "Won Coreano": {
        "id": 4,
        "nome": "Won Coreano",
        "simbolo": '₩',
        "para_real": 0.0042551,
        "real_para": 234.5465
    },
    "Real Brasileiro": {
        "id": 5,
        "nome": "Real Brasileiro",
        "simbolo": 'R$',
        "para_real": 1,
        "real_para": 1
    }
}