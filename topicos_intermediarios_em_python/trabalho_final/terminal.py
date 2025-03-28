from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from email_funcoes import enviar_relatorio_diario
import json


console = Console()


CARDAPIO = "topicos_intermediarios_em_python/trabalho_final/cardapio.json"
PEDIDOS = "topicos_intermediarios_em_python/trabalho_final/pedidos.json"


def carregar_cardapio():
    try:
        with open(CARDAPIO, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}


def salvar_cardapio(cardapio):
    with open(CARDAPIO, "w") as arquivo:
        json.dump(cardapio, arquivo, indent=2)


def carregar_pedidos():
    try:
        with open(PEDIDOS, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}


def salvar_pedidos(pedidos):
    with open(PEDIDOS, "w") as arquivo:
        json.dump(pedidos, arquivo, indent=4)


def listar_cardapio():
    cardapio = carregar_cardapio()
    table = Table(title="[bold]Cardápio")
    table.add_column("Prato", style="cyan")
    table.add_column("Preço", style="green")
    table.add_column("Tempo de Preparo", style="yellow")
    
    numero_prato = 1
    for categoria in cardapio.values():

        for prato, info in categoria.items():
            table.add_row(f'({numero_prato}) {prato}', f'R$ {info[0]:.2f}', f'{info[1]} minutos')
            numero_prato += 1
    
    console.print('\n')
    console.print(table)


def adicionar_prato():
    cardapio = carregar_cardapio()
    nome = console.input(f'\n[bold]Digite o nome do prato: ')
    preco = funcao_try_float(f'Digite o preço do prato: ', f'Digite um preço válido!')
    tempo = funcao_try_int(f'Digite o tempo para o preparo do prato: ', f'Digite um tempo válido!')
    categoria = ["entradas", "principais", "sobremesas", "bebidas"]

    console.print(f'\n[bold]Escolha a categoria que deseja adicionar esse prato:')
    for opcao, item in enumerate(categoria):
        console.print(f'({opcao + 1}) {item.capitalize()}')

    escolha = funcao_try_escolha(f'Digite a sua escolha: ', f'Insira uma escolha válida!',1, 4)

    cardapio[categoria[escolha - 1]][nome] = [preco, tempo]
    salvar_cardapio(cardapio)
    console.print(f'\n[bold green]Prato [yellow]{nome}[/] adicionado com sucesso!')


def modificar_preco():
    cardapio = carregar_cardapio()
    listar_cardapio()
    numero_prato = funcao_try_int(f'Digite o número do prato para modificar o seu preço: ', f'Digite um número válido!')

    prato_encontrado = False
    i = 1
    for categoria, pratos in cardapio.items():
        for prato in pratos:
            if i == numero_prato:
                novo_preco = funcao_try_float(f'Digite o novo preço do prato: ', f'Digite um preço válido!')
                cardapio[categoria][prato][0] = novo_preco
                salvar_cardapio(cardapio)
                console.print(f'\n[bold green]Preço do prato [yellow]{prato}[/] atualizado para [yellow]R$ {novo_preco:.2f}[/]!')
                prato_encontrado = True
            i += 1
    
    if not prato_encontrado:
        console.print(f'\n[bold red]Prato não encontrado!')


def gerenciar_pedidos():
    pedidos = carregar_pedidos()
    if not pedidos:
        console.print(f'\n[bold red]Nenhum pedido encontrado!')
        return
    
    table = Table(title="[bold]Pedidos")
    table.add_column("Nome", style="cyan")
    table.add_column("Endereço", style="green")
    table.add_column("Código", style="yellow")
    table.add_column("Status", style="magenta")
    
    for pedido in pedidos.values():
        table.add_row(pedido["nome"], pedido["endereco"], pedido["codigo"], pedido["status"])
    
    console.print('\n')
    console.print(table)

    pedido_codigo = str(funcao_try_escolha(f'Informe o código do pedido a ser atualizado: ', f'Informe um código válido entre 1000 e 9999!', 1000, 9999))

    achou_pedido = False
    for user_id, info in pedidos.items():
        
        if pedido_codigo == info["codigo"]:
            if info["status"] != 'Entregue':
                status = (
                    "\n[bold]([red]1[/]) Em preparo\n"
                    "[bold]([red]2[/]) Saiu para entrega\n"
                    "[bold]([red]3[/]) Entregue"
                )

                console.print(status)
                escolha = funcao_try_escolha(f'Escolha o novo status do pedido: ', f'Insira uma opção válida!',1, 3)
                status = ["Em preparo", "Saiu para entrega", "Entregue"]
                novo_status = status[escolha - 1]

                pedidos[user_id]["status"] = novo_status
                
                salvar_pedidos(pedidos)
                console.print(f'\n[bold green]Status do pedido [yellow]{info["codigo"]}[/] atualizado para [yellow]{novo_status}[/]!')

                achou_pedido = True
            
            else:
                achou_pedido = True
                console.print(f'\n[bold red]Esse pedido já foi concluído e não pode mais ser modificado!')
    
    if not achou_pedido: 
        console.print(f'\n[bold red]Pedido não encontrado!')


def funcao_try_float(msg, error_message):
    while True:
        try:
            var = float(console.input(f'\n[bold]{msg}'))
            if var <= 0:
                raise ValueError
            return var
        
        except ValueError:
            console.print(f'\n[bold red]{error_message}')


def funcao_try_int(msg, error_message):
    while True:
        try:
            var = int(console.input(f'\n[bold]{msg}'))
            if var <= 0:
                raise ValueError
            return var
        
        except ValueError:
            console.print(f'\n[bold red]{error_message}')


def funcao_try_escolha(msg, error_message, min, max):
    while True:
        try:
            var = int(console.input(f'\n[bold]{msg}'))

            if var >= min and var <= max:
                return var
            else:
                raise ValueError
            
        except ValueError:
            console.print(f'\n[bold red]{error_message}')


while True:

    menu = (
        "\n([red]1[/]) Listar Cardápio\n"
        "([red]2[/]) Adicionar Prato\n"
        "([red]3[/]) Modificar Preço de um Prato\n"
        "([red]4[/]) Gerenciar Pedidos\n"
        "([red]5[/]) Sair [yellow](Enviar relatório diário)[/]\n"
    )

    console.print('\n')
    console.print(Panel.fit(menu, title="[bold]Gestão do Restaurante"))

    opcao = funcao_try_escolha(f'Digite sua escolha: ', f'Insira uma opção válida!', 1, 5)
    
    if opcao == 1:
        listar_cardapio()
    elif opcao == 2:
        adicionar_prato()
    elif opcao == 3:
        modificar_preco()
    elif opcao == 4:
        gerenciar_pedidos()
    elif opcao == 5:
        pedidos = carregar_pedidos()
        enviar_relatorio_diario(pedidos)
        console.print(f'\n\n\n[bold magenta]Relatório enviado para o gerente do restaurante, desligando o sistema...\n\n\n')
        pedidos = {}
        salvar_pedidos(pedidos)
        break