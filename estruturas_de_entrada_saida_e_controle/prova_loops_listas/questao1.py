# QUESTAO 1
def calcula_media(notas):
    qnt = len(notas)
    maior = max(notas)
    menor = min(notas)
    notas.remove(maior)
    notas.remove(menor)
    media = sum(notas)/len(notas)
    if media >= 8.5:
        return "Classificado"
    else:
        return "Não Classificado"



        
        

 

    

