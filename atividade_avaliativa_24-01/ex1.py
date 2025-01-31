from ex1_funcoes import *


try:               
    with open("alunos.txt", "r") as arquivo:
        conteudo = arquivo.readlines()
except FileNotFoundError:
    with open("alunos.txt", "a") as arquivo:
        nome, matricula, idade, curso = registrar_aluno()
        arquivo.write(f'{nome},{matricula},{idade},{curso}\n')

while True:
    print(f'\nMENU')
    print(f'\n(1) - Listar todos os alunos')
    print(f'(2) - Buscar aluno por nome ou matrícula')
    print(f'(3) - Editar dados de um aluno')
    print(f'(4) - Adicionar um aluno')
    print(f'(5) - Remover um aluno')
    print(f'(0) - Sair')

    with open("alunos.txt", "r") as arquivo:
        conteudo = arquivo.readlines()
        
    dados = []                  

    for aluno in conteudo:
        dados.append(aluno.split(','))

    escolha = verifica_escolha(0,5)

    if escolha == 1:
        print(f'\nLista de Alunos:')
        i = 1
        for aluno in dados:
            print(f'({i})- {aluno[0]}: {aluno[2]} anos, {aluno[3]}')
            i += 1

    if escolha == 2:
        print(f'\nBuscar por:')
        print(f'(1)- Nome')
        print(f'(2)- Matrícula')
        opcao = verifica_escolha(1,2)
        
        if opcao == 1:
            nome = verifica_dado('nome')
            
            for aluno in dados:
                achou = False
                if nome == aluno[0]:
                    print(f'Nome: {aluno[0]}')
                    print(f'Matrícula: {aluno[1]}')
                    print(f'Idade: {aluno[2]}')
                    print(f'Curso: {aluno[3]}')
                    achou = True
                    break

            if not achou:
                print(f'Aluno não encontrado!')                        
                
        else:
            matricula = verifica_dado('matricula')

            for aluno in dados:
                achou = False
                if matricula == aluno[1]:
                    print(f'Nome: {aluno[0]}')
                    print(f'Matrícula: {aluno[1]}')
                    print(f'Idade: {aluno[2]}')
                    print(f'Curso: {aluno[3]}')
                    achou = True
            if not achou:
                print(f'Aluno não encontrado!')      

    
    
    
    if escolha == 3:
        print(f'\nTodos os alunos registrados:')
        i = 1
        for aluno in dados:
            print(f'({i})- {aluno[0]}')
            i += 1
        opcao = verifica_escolha(1, i - 1)


        print(f'\nO que deseja modificar nesse aluno?')
        print(f'(1)- Nome')
        print(f'(2)- Matrícula')
        print(f'(3)- Idade')
        print(f'(4)- Curso')

        categoria = verifica_escolha(1, 4)
        if categoria == 1:
            novo_dado = verifica_dado('nome')

        if categoria == 2:
            novo_dado = verifica_dado('matricula')

        if categoria == 3:
            novo_dado = verifica_dado('idade')

        if categoria == 4:
            novo_dado = verifica_dado('curso')

        dados = conteudo[opcao - 1].split(',')
        
        dados[categoria - 1] = novo_dado

        conteudo[opcao - 1] = ','.join(dados)

        with open("alunos.txt", "w") as arquivo:
            arquivo.writelines(conteudo)

    if escolha == 4:
        with open("alunos.txt", "a") as arquivo:
            nome, matricula, idade, curso = registrar_aluno()
            arquivo.write(f'{nome},{matricula},{idade},{curso}\n')

    if escolha == 5:
        print(f'\nEscolha um aluno para ter seus dados deletados:')
        i = 1
        for aluno in dados:
            print(f'({i})- {aluno[0]}')
            i += 1
        opcao = verifica_escolha(1, i - 1)
        print(f'Deletando os dados de {dados[opcao - 1][0]}...')

        del conteudo[opcao - 1]
        with open("alunos.txt", "w") as arquivo:
            arquivo.writelines(conteudo)
    
    if escolha == 0:
        break


          