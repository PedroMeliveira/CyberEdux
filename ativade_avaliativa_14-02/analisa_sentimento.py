import re


def verifica_não(lista, index):
    try:
        if lista[index - 1][0].lower() == 'n':
            return True
        
        return False
    
    except IndexError:
        return False


def testa_sentimento(frase):

    pontos = 0

    palavras_positivas = ['feliz', 'gostei', 'amei', 'ótimo', 'bom', 'maravilhoso', 'perfeito', 'adorei', 'rápido', 'eficiente', 'adequado', 'satisfeito']
    palavras_negativas = ['odiei', 'péssimo', 'ruim', 'horrível', 'triste', 'detestei', 'decepcionante', 'insatisfeito', 'lento', 'inadequado']
    
    frase = frase.lower().split()

    for i in range(len(frase)):

        palavra = frase[i]
        for caracter in palavra:
            pattern = '[a-zà-ú]'
            if not re.search(pattern, caracter):
                frase[i] = palavra.replace(caracter, '')
            
        if frase[i] in palavras_positivas:
            
            if verifica_não(frase, i):
                pontos -= 1
            else:
                pontos += 1

        if frase[i] in palavras_negativas:

            if verifica_não(frase, i):
                pontos += 1
            else:
                pontos -= 1

    if pontos > 0:
        return 'positivo'
    
    elif pontos < 0:
        return 'negativo'
    
    else:
        return 'neutro'