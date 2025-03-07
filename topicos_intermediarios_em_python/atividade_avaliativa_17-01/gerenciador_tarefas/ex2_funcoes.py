def escolher_opcao(min, max):
    while True:
        try:
            escolha = int(input(f'Digite a opção que deseja escolher: '))

            while escolha < min or escolha > max:
                print(f'Opção INVÁLIDA!')
                escolha = int(input(f'Digite a opção que deseja escolher: '))

            return escolha

        except ValueError:
            print(f'Opção INVÁLIDA!')

def print_tarefas_prioridade(tarefas):
    i = 1
    for tarefa in tarefas:
        for nome_tarefa in tarefa.keys():
            for prioridade in tarefa.values():
                if prioridade:
                    print(f'{i} - {nome_tarefa} (PRIORIDADE)')
                    i += 1
    for tarefa in tarefas:
        for nome_tarefa in tarefa.keys():
            for prioridade in tarefa.values():
                if not prioridade:
                    print(f'{i} - {nome_tarefa}')
                    i += 1

def print_tarefas(tarefas):
    i = 1
    for tarefa in tarefas:
        for nome_tarefa in tarefas.keys():
            print(f'{i} - {nome_tarefa}')
            i += 1