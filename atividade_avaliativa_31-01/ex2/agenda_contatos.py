import csv
import json


# Desafio 1


informacoes = {
    "versao" : "1.23.2",
    "tema" : "blue",
    "idioma" : "pt-BR",
    "permissoes" : "audio"
}

with open("config.json", "w") as arquivo:
    json.dump(informacoes,arquivo)

with open("config.json", "r") as arquivo:
    dados = json.load(arquivo)

print(f'Escolha uma configuração para alterar:')
i = 1
for config in dados.keys():
    print(f'({i})- {config.capitalize()}')
    i += 1

# escolha = filtra_escolha(1, 4)

# dados = list(dados.keys())
# informacoes[dados[escolha - 1]] = input(f'Insira a alteração que deseja fazer em {dados[escolha - 1].capitalize()}: ')

# with open("config.json", "w") as arquivo:
#     json.dump(informacoes, arquivo)


# # Desafio 2

# def ler_dados():
#     try:
#         with open("contatos.json", "r") as arquivo:
#             dados = json.load(arquivo)
#         return dados
#     except FileNotFoundError:
#         dados = []
#         with open("contatos.json", "w") as arquivo:
#             json.dump(dados, arquivo)
#         return dados

# while True:
#     print(f'Escolha o que deseja fazer na sua lista de contatos:')
#     print(f'(1)- Adicionar Contato')
#     print(f'(2)- Editar Contato')
#     print(f'(3)- Remover Contato')
#     print(f'(4)- Ver todos os Contatos')
#     print(f'(5)- Sair')

#     escolha = filtra_escolha(1, 5)


#     if escolha == 1:
#         contatos_dic = {}
#         contato_nome = input(f'Insira o nome do Contato que deseja salvar: ')
#         contato_idade = int(input(f'Digite a idade do Contato que deseja salvar: '))
#         contatos_dic["nome"] = contato_nome
#         contatos_dic["idade"] = contato_idade

#         dados = ler_dados()
#         dados.append(contatos_dic)
#         with open("contatos.json", "w") as arquivo:
#             json.dump(dados, arquivo)


#     if escolha == 2:
#         dados = ler_dados()
#         print(f'Escolha o contato que deseja alterar:')
#         for i, dado in enumerate(dados):
#             print(f'({i + 1})- {dado["nome"]}')

#         escolha_aux = filtra_escolha(1, len(dados))

#         print(f'O que deseja alterar no contato de {dados[escolha_aux - 1]["nome"]}:')
#         print(f'(1)- Nome')
#         print(f'(2)- Idade')

#         escolha_aux_b = filtra_escolha(1, 2)

#         if escolha_aux_b == 1:
#             dados[escolha_aux - 1]["nome"] = input(f'Digite um novo nome para esse contato: ')
        
#         else:
#             dados[escolha_aux - 1]["idade"] = int(input(f'Digite uma nova idade para esse contato: '))

#         with open("contatos.json", "w") as arquivo:
#             json.dump(dados, arquivo)

#     if escolha == 3:
#         dados = ler_dados()
#         print(f'Escolha o contato que deseja remover:')
#         for i, dado in enumerate(dados):
#             print(f'({i + 1})- {dado["nome"]}')

#         escolha_aux = filtra_escolha(1, len(dados))

#         del dados[escolha_aux - 1]

#         with open("contatos.json", "w") as arquivo:
#             json.dump(dados, arquivo)

#     if escolha == 4:
#         dados = ler_dados()
#         print(f'    {'Nome'.ljust(15)} |    Idade')
#         for i, dado in enumerate(dados):
#             print(f'({i + 1})- {dado["nome"].ljust(20)} {dado["idade"]}')
    
#     if escolha == 5:
#         break