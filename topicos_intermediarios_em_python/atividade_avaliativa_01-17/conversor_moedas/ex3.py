from ex3_funcoes import * 
while True:
    print(f'\nBem vindo ao seu conversor de moedas!\n')

    escolha = (f'Deseja converter sua moeda? (S/N)').lower()[0]

    if escolha == 's':
        print(f'Trabalhamos com as seguintes moedas: \n')

        i = 1
        for moeda in moedas.keys():
            print(f'{i} - {moeda}')
            i += 1

        while True:
            try:
                moeda_escolha1 = int(input(f'\nDigite a opção da moeda atual: '))

                while moeda_escolha1 < 1 or moeda_escolha1 > 6:
                    print(f'\nOpção INVÁLIDA!')
                    moeda_escolha1 = int(input(f'Digite a opção da moeda atual: '))
                break
            except ValueError:
                print(f'\nOpção INVÁLIDA!')

        for moeda_atual in moedas.values():
            if moeda_atual["id"] == moeda_escolha1 - 1:
                break

        while True:
            try:
                valor_anterior = int(input(f'\nDigite o valor que será convertido: '))
                break
            except ValueError:
                print(f'Valor INVÁLIDO. Tente novamente.')


        if moeda_atual != 'real':
            for moeda in moedas.values():
                if moeda_atual == moeda:
                    break
            valor_real = round(moeda['para_real'] * valor_anterior, 2)

        i = 1

        print()
        for moeda in moedas.keys():
            print(f'{i} - {moeda}')
            i += 1

        while True:
            try:
                moeda_escolha2 = int(input(f'\nDigite a opção da nova moeda: '))

                while moeda_escolha2 < 1 or moeda_escolha2 > 6:
                    print(f'\nOpção INVÁLIDA!')
                    moeda_escolha2 = int(input(f'Digite a opção da nova moeda: '))
                break
            except ValueError:
                print(f'\nOpção INVÁLIDA!')

        for moeda_nova in moedas.values():
            if moeda_nova["id"] == moeda_escolha2 - 1:
                break

        if moeda_nova != 'real':
            for moeda in moedas.values():
                if moeda_nova == moeda:
                    break
            valor_novo = round(moeda['real_para'] * valor_real, 2)

        print(f'\nValor inicial era {valor_anterior}, o Valor final é {valor_novo}')
    
    elif escolha == 'n':
        break

    else:
        print(f'Escolha INVÁLIDA. Tente novamente.')