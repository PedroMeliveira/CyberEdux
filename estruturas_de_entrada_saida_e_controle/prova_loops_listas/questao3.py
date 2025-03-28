# QUESTAO 3

def validar_idades(lista_idades):
    idades_val = []
    qnt_inv = qnt_val = soma = 0
    for idade in lista_idades:
        if idade < 0 or idade > 120:
            qnt_inv += 1
        else: 
            qnt_val += 1
            soma += idade
            idades_val.append(idade)
    media = soma/qnt_val
    print(f'A média das idades é: {media}')
    print(f'A quantidade de idades inválidas foram: {qnt_inv}')
    return idades_val
