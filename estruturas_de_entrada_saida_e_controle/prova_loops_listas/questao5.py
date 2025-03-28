# QUESTAO 5

def relatorio(notas, media, nota_final, qnt_abaixo7):
    print()
    print('='*42)
    print()
    print('             Relatório Final\n')
    print(f'As suas notas foram as seguintes: {notas}')
    print(f'- Sua nota final foi: {nota_final}')
    print(f'- Sua média foi: {media}')
    print(f'- Número de notas abaixo de 7.0 foi: {qnt_abaixo7}\n')
    print('='*42)

def adiciona_notas():
    notas = []
    while True:
        notas.append(float(input('Digite sua nota: ')))
        continuar = input('Deseja continuar adicionando notas? (S/N)').upper().strip()[0]
        if continuar == 'N':
            break
    return notas

def calcula_media(notas):
    soma = sum(notas)
    media = soma/(len(notas))
    return media

def conta_notas_abaixo7(notas):
    qnt_abaixo7 = 0
    for nota in notas:
        if nota < 7:
            qnt_abaixo7 += 1
    return qnt_abaixo7

def conceito_final(media):
    if media >= 9:
        return 'A'
    elif media >= 8 and media < 9:
        return 'B'
    elif media >= 7 and media < 8:
        return 'C'
    else:
        return 'D'

print('='*42)
print()
print('Sistema de análise de desempenho acadêmico')
print()
print('='*42)   

notas = adiciona_notas()

media = calcula_media(notas)

qnt_abaixo7 = conta_notas_abaixo7(notas)

nota_final = conceito_final(media)

print(relatorio(notas, media, nota_final, qnt_abaixo7))