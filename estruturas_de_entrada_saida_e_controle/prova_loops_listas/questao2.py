# QUESTAO 2

vendas = []

while True:
    vendas.append(float(input("Digite valor da venda: ")))
    escolha = input("Deseja continuar adicionando vendas? (S/N)").upper().strip()[0]
    if escolha == 'N':
        break
vendas_maior_1000 = []
maior = max(vendas)
for venda in vendas:
    if venda > 1000:
        vendas_maior_1000.append(venda)

media = sum(vendas)/len(vendas)

print(f'A soma das vendas foi {sum(vendas)}')
print(f'A quantidade de vendas que foram maior que a média foi {len(vendas_maior_1000)} vendas')
print(f'A maior venda foi {maior}')
print(f'Lista das vendas que foram maior que 1000 reais: {vendas_maior_1000}')