import ex2_funcoes as fun


print(f'Bem vindo ao seu Gerenciador de tarefas! ')

print(f'1 - Ver tarefas')
print(f'2 - Adicionar tarefa')
print(f'3 - Remover tarefa')
print(f'0 - Sair')

tarefas = {}

escolha = fun.escolher_opcao(0,3)

if escolha == 1:
    if len(tarefas) > 0:
        fun.print_tarefas(tarefas)
    else: 
        print(f'Você não possui tarefas ainda.')

elif escolha == 2:
    while True:
        try:
            qntd_tarefas = int(input(f'Deseja adicionar quantas tarefas? '))
            
            while qntd_tarefas <= 0:
                print(f'Digite um número válido!')
                qntd_tarefas = int(input(f'Deseja adicionar quantas tarefas? '))
            break 
        except ValueError:   
            print(f'Digite uma quantidade válida! ')
    for i in range(qntd_tarefas):
        tarefa = input(f'Digite o nome da tarefa {i + 1}: ')
        while True:
                prioridade = input(f'Essa tarefa deve ser destacada com prioridade? (S/N)').lower()[0]
                if prioridade == 's':
                    prioridade = True
                    break
                elif prioridade == 'n':
                    prioridade = False
                    break
                print(f'Opção inválda! ')
        tarefas[tarefa] ={'prioridade': prioridade}
    











# tarefas = {"tarefa1": {'prioridade': True}}
# tarefas['tarefa2']= {'prioridade': False}
# print(tarefas)