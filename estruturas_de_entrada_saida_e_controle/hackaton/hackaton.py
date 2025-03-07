from rich.console import Console
import hackaton_funcoes as hf
 
console = Console()

while True:
    while True:

        hf.menu_principal()

        escolha = hf.escolher_opcao(1, 2)

        if escolha == 1:
            console.print(f'\n[red underline]Digite "SAIR" para voltar.')
            login = console.input(f'\n[bold]Digite seu Login: ')
            
            if login.lower() != 'sair':

                if login in hf.perfis.keys():
                    senha = console.input(f'\n[bold]Digite sua Senha: ')

                    if hf.verifica_login_senha(login, senha):
                        break

                    else:
                        console.print(f'\n[bold red underline]Senha inválida')
                        
                else:
                    console.print(f'\n[bold red underline]Esse usuário não está cadastrado!')

        elif escolha == 2:
            hf.registrar_perfil()


    # Sessão de Administrador

    if login == "admin":
        while True:

            hf.menu_admin()

            escolha = hf.escolher_opcao(1, 3)

            if escolha == 1: # Informacoes de cliente específico
                hf.info_cliente()

            elif escolha == 2: # Sair da conta de Administrador
                console.print(f'\n\n[bold magenta underline]Saindo da conta de administrador...\n')
                break
            
            elif escolha == 3: # Desligar máquinao
                console.print(f'\n\n[bold magenta underline]Desligando a máquina...\n\n')
                exit()
        
    else: 

    # Sessão do Cliente

        while True:

            hf.menu_cliente(login)

            escolha = hf.escolher_opcao(1, 9)

            if escolha == 1: # Depósito
                hf.deposito(login)

            elif escolha == 2: # Saque
                hf.saque(login)

            elif escolha == 3: # Transferência para cliente Noob Bank
                hf.transferencia(login)
                
            elif escolha == 4: # Extrato com filtro de período
                hf.extrato_periodo(login)

            elif escolha == 5: # Simulação de investimento
                hf.simulador_investimento(login)

            elif escolha == 6: # Registrar gasto
                hf.registrar_gasto(login)

            elif escolha == 7: # Relatório de gasto
                hf.relatorio_gasto(login)

            elif escolha == 8: # Alterar moeda padrão
                hf.alterar_moeda_padrao(login)

            elif escolha == 9: # Sair da conta
                console.print(f'\n[bold magenta underline]\nSaindo da sua conta...\n')
                break