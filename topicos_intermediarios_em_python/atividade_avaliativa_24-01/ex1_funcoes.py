def verifica_dado(dado):
    if dado == 'nome':
        while True:           
            nome = input(f'Digite o nome do aluno: ') 
                    
            if any(chr.isdigit() for chr in nome):
                print(f'Nome inválido. Tente novamente.')
            else:
                return nome
            
    elif dado == 'matricula':
        while True:           
            matricula = input(f'Digite a matricula do aluno: ') 

            if any(chr.isalpha() for chr in matricula):
                print(f'Matricula inválida. Tente novamente.')
            else:
                return matricula
            
    elif dado == 'idade':
        while True:
            try:
                idade = input(f'Digite a idade desse aluno: ')
                return idade
            except ValueError:
                print(f'Idade inválida. Tente novamente.')

    elif dado == 'curso':
        while True:           
            curso = input(f'Digite o nome do curso: ') 
                    
            if any(chr.isdigit() for chr in curso):
                print(f'Curso inválido. Tente novamente.')
            else:
                return curso
            
def registrar_aluno():
    nome = verifica_dado('nome')
    matricula = verifica_dado('matricula')
    idade = verifica_dado('idade')
    curso = verifica_dado('curso')
    
    return nome, matricula, idade, curso

def verifica_escolha(min, max):
    while True:
        try:
            escolha = int(input(f'\nEscolha uma opção: '))
            if escolha < min or escolha > max:
                raise ValueError
            break
        except ValueError:
            print(f'\nInsira um valor válido!')
    return escolha