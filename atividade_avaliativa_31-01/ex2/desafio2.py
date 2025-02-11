import json

def função_escolha(min, max):
    while True:
        try:
            escolha = int(input(f'\nDigite a opção que deseja executar: '))

            while escolha < min or escolha > max:
                print(f'\nEscolha uma opção entre {min} e {max}!')
                escolha = int(input('\nDigite a opção que deseja: '))

            return escolha
        
        except:
            print(f'\nOpção Inválida!')

def adicionar_contatos(qnt):

    for i in range(qnt):
        nome = input(f'\nDigite o nome do {i + 1}º contato: ')
        while nome in contatos:
            print(f'\nEsse nome já está registrado! Tente outro.')
            nome = input(f'\nDigite o nome do {i + 1}º contato: ')

        telefone = input(f'\nDigite o telefone do {i + 1}º contato: ')
        while telefone in contatos.values():
            print(f'\nEsse telefone já está registrado! Tente outro.')
            nome = input(f'\nDigite o nome do {i + 1}º contato: ')

        contatos[nome] = telefone

contatos = {}



while True:
    print(f'\nBem vindo a sua Agenda de contatos!\n')
    print(f'1 - Listar Contatos')
    print(f'2 - Adicionar Contato')
    print(f'3 - Remover Contato')
    print(f'0 - Sair')

    escolha = função_escolha(0, 3)

    if escolha == 1:
        if len(contatos) == 0:
            print(f'\nVocê não possui nenhum contato em sua lista.')
        
        else:
            i = 1
            print(f'\n{'='*5}LISTA DE CONTATOS{'='*5}\n')
            for nome, telefone in contatos.items():
                print(f'{i} - {nome}: {telefone}')
                i += 1

    elif escolha == 2:
        while True:
            try:
                qnt = int(input(f'\nQuantos contatos você deseja adicinoar? '))
                adicionar_contatos(qnt)
                break

            except ValueError:
                print(f'\nEntrada inválida! Tente novamente.')
        with open('atividade_avaliativa_31-01/ex2/contatos.json', 'w') as arquivo:
            json.dump(contatos, arquivo)

    elif escolha == 3:
        if len(contatos) == 0:
            print(f'\nVocê não possui nenhum contato em sua lista.')
        
        else:
            i = 1
            print(f'\n{'='*5}LISTA DE CONTATOS{'='*5}')
            for nome, telefone in contatos.items():
                print(f'{i} - {nome}: {telefone}')
                i += 1
            while True:
                try:
                    contato_remover = int(input('\nDigite a opção do contato que deseja remover: '))
                    while contato_remover < 1 or contato_remover > len(contatos):
                        print(f'\nNão existe nenhum contato registrado com essa opção! Tente novamente.')
                        contato_remover = int(input('\nDigite a opção do contato que deseja remover: '))

                    del contatos[list(contatos)[contato_remover - 1]]
                
                except ValueError:
                    print(f'Opção Inválida! Tente novamente.')




