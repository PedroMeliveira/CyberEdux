
def menu(saldo):
    print("="*50)
    print("Bem vindo ao seu Sistema de Gestão de Orçamento")
    print("Saldo: ", saldo)
    print("1 - Adicionar despesa")
    print("2 - Adicionar receita")
    print("3 - Relatório de transação")
    print("4 - Histórico de transação")
    print("0 - Sair")
    print("="*50)

def menu_despesa():
    print('='*50)
    print("1 - Alimentação")
    print("2 - Transporte")
    print("3 - Lazer")
    print("4 - Outros")
    print('='*50)

def adicionar_despesa_saldo(despesa, saldo):
    saldo -= despesa
    return saldo

def adicionar_historico(valor, lista_valor):
    lista_valor.append(valor)


def adicionar_despesa_total(despesa, despesa_total):
    despesa_total += despesa
    return despesa_total

def adicionar_despesa_categoria(despesa, categoria):
    categoria += despesa
    return categoria

def adicionar_receita_saldo(receita, saldo):
    saldo += receita
    return saldo

def adicionar_receita_total(receita, receita_total):
    receita_total += receita
    return receita_total

def print_historico(historico):
    print('='*20)
    print('Histórico de Transação:')
    print('')
    for i in range(0, len(historico)):
        if historico[i] < 0:
            print(f'{i + 1} - Despesa - R${-historico[i]}')
        else:
            print(f'{i + 1} - Receita - R${historico[i]}')
    print('')
    print('='*20)

def relatorio(saldo, despesa_total, alimento, transporte, lazer, outros, receita_total):
    print("=====================================================")
    print("Relatório de Despesa e Receita")
    print(" ")
    print("Seu saldo: ", saldo)
    print(" ")
    print("Receita Total: ", receita_total)
    print(" ")
    print("Despesa Total: ", despesa_total)
    print(" ")
    if alimento != 0:
        print(f'Despesa de Alimentação: {alimento}, {round({despesa_total/alimento}, 2)}% do Total')
    else:
        print(f'Despesa de Alimentação: {alimento}, 0% do Total')
    print(" ")
    if transporte != 0:
        print(f'Despesa de Transporte: {transporte}, {round({despesa_total/transporte}, 2)}% do Total')
    else:
        print(f'Despesa de Transporte: {transporte}, 0% do Total')
    print(" ")
    if lazer != 0:
        print(f'Despesa de Lazer: {lazer}, {round({despesa_total/lazer}, 2)}% do Total')
    else:
        print(f'Despesa de Lazer: {lazer}, 0% do Total')
    print(" ")
    if outros != 0:
        print(f'Despesa de Outros: {outros}, {round({despesa_total/outros}, 2)}% do Total')
    else:
        print(f'Despesa de Outros: {outros}, 0% do Total')
    print('')
    print("=====================================================")