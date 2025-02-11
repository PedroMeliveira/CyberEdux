
import json

def função_escolha(min, max):
    while True:
        try:
            escolha = int(input('\nDigite a opção que deseja: '))
            while escolha < min or escolha > max:
                print(f'\nEscolha uma opção entre {min} e {max}!')
                escolha = int(input('\nDigite a opção que deseja: '))
            return escolha
        except:
            print(f'\nOpção Inválida!')

# Desafio 1


informacoes = {
    "Versao" : "1.23.2",
    "Tema" : "preto",
    "Idioma" : "PT-BR",
    "Permissoes" : "audio"
}

with open('atividade_avaliativa_31-01/ex2/config.json', 'w') as arquivo:
    json.dump(informacoes, arquivo)


while True:
    print(f'Qual configuração você deseja alterar? ')
    i = 1
    for config in informacoes.keys():
        print(f'{i} - {config}')
        i += 1
    print(f'0 - Sair')

    escolha = função_escolha(0, 4)

    if escolha == 0:
        break

    nova_config = input(f'\nDigite a nova configuração: ')

    informacoes[list(informacoes)[escolha-1]] = nova_config 

    with open('atividade_avaliativa_31-01/ex2/config.json', 'w') as arquivo:
        json.dump(informacoes, arquivo)
