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

def print_tarefas(tarefas):
    i = 1
    for tarefa in tarefas.keys():
        if tarefas[tarefa]['prioridade']:
            print(f'{i} - {tarefa} (PRIORIDADE).')
            i += 1
    for tarefa in tarefas.keys():
        if not tarefas[tarefa]['prioridade']:
            print(f'{i} - {tarefa}.')
            i += 1
            