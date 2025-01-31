from rich.console import Console
import ex1_funcoes as fun

console = Console()

while True:

        fun.menu_principal()

        escolha = fun.escolher_opcao(1, 2)

        if escolha == 1:
            login = console.input(f'\n[bold]Digite seu Login: ')
        
            if login in fun.perfis.keys():
                senha = console.input(f'\n[bold]Digite sua Senha: ')

                if fun.verifica_login_senha(login, senha):
                    break

                else:
                    console.print(f'\n[bold red underline]Senha inválida')
                    
            else:
                console.print(f'\n[bold red underline]Esse usuário não está cadastrado!')

        elif escolha == 2:
            fun.registrar_perfil()