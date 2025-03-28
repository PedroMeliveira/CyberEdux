import funcoes_gestao_orçamento as fun

saldo = receita_total = despesa_total = alimentação = transporte = lazer = outros = despesa = receita = 0
historico = []
while True:
    fun.menu(saldo)
    operação = int(input("Digite o número da ação que deseja realizar: "))

    if operação == 1:
        despesa = float(input("Qual valor da sua despesa: "))
        saldo = fun.adicionar_despesa_saldo(despesa, saldo)
        despesa_total = fun.adicionar_despesa_total(despesa, despesa_total)
        fun.menu_despesa()
        fun.adicionar_historico(-despesa, historico)
        operação_1 = int(input('Digite o número da categoria da despesa: '))
        if operação_1 == 1:
            alimentação = fun.adicionar_despesa_categoria(despesa, alimentação)
            print(f'Despesa de R${despesa}, adicionada com sucesso na categoria Alimentação!')
        elif operação_1 == 2:
            transporte = fun.adicionar_despesa_categoria(despesa, transporte)
            print(f'Despesa de R${despesa}, adicionada com sucesso na categoria Transporte!')
        elif operação_1 == 3:
            lazer = fun.adicionar_despesa_categoria(despesa, lazer)
            print(f'Despesa de R${despesa}, adicionada com sucesso na categoria Lazer!')
        elif operação_1 == 4:
            outros = fun.adicionar_despesa_categoria(despesa, outros)
            print(f'Despesa de R${despesa}, adicionada com sucesso na categoria Outros!')
        else:
            print('Opção inválida, tente novamente.')

    elif operação == 2:
        receita = float(input("Digite o valor da sua receita: "))
        saldo = fun.adicionar_receita_saldo(receita, saldo)
        receita_total = fun.adicionar_receita_total(receita, receita_total)
        fun.adicionar_historico(receita, historico)
        print(f'Receita de R${receita}, adicionada com sucesso!')
    
    elif operação == 3:
        fun.relatorio(saldo, despesa_total, alimentação, transporte, lazer, outros, receita_total)

    elif operação == 4:
        fun.print_historico(historico)

    elif operação == 0:
        break

    else:
        print('Opção Inválida! Tente novamente.')
