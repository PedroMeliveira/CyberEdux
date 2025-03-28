import re

def validar(funçao, validado):

    if funçao == 'email':
        pattern = "[\w]+@[\w]+[\.com]" #FORMATO -> xxxxxxxx@xxxxx.com
        if re.search(pattern, validado):
            return True
        else:
            return False

    if funçao == 'cpf':
        pattern = "[\d]{3}[.][\d]{3}[.][\d]{3}[-][\d]{2}" #FORMATO -> 000.000.000-00
        if re.search(pattern, validado):
            return True
        else: 
            return False
        
    if funçao == 'telefone':
        pattern = "[\(][1-9]{2}[\)][ ][9][ ][\d]{4}[-][\d]{4}" #FORMATO -> (00) 9 0000-0000
        if re.search(pattern, validado):
            return True
        else:
            return False
        
    if funçao == 'data':
        pattern = "[\d]{2}[/][\d]{2}[/][\d]{4}"  #FORMATO -> 00/00/0000
        if re.search(pattern, validado):
            return True
        else:
            return False
        
    if funçao == 'senha':
        valido =  True
        if len(validado) < 8:
            valido = False
        pattern = '[\d]'
        if not re.search(pattern, validado):   #Verifica se tem digito
            valido = False
        pattern = '[a-z]'
        if not re.search(pattern, validado):   #Verifica se tem letra minuscula
            valido = False
        pattern = '[A-Z]'
        if not re.search(pattern, validado):   #Verifica se tem letra maiuscula
            valido = False
        pattern = '[\W]'
        if not re.search(pattern, validado):   #Verifica se tem caracteres especiais, ou seja nao letra e nao digito e nao "_"
            valido = False
        return valido
        
    

