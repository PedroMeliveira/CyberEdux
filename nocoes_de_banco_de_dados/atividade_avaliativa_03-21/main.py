from funcoes import *

cria_tabelas_sql()
insert_admin()
insert_cardapio_fixo()

while True:
    menu_out()

    opcao = escolha(0, 2)

    if opcao == 1:

        id_cliente = login()

        while True and id_cliente != 'sair' and id_cliente != 0:
            menu_cliente()

            opcao = escolha(0, 3)

            if opcao == 1:
                opcao_cardapio()

            elif opcao == 2:
                fazer_pedido(id_cliente)
            elif opcao == 3:
                verificar_status(id_cliente)
            else:
                print(f"Saindo...")
                break
        
        if id_cliente == 0:
            while True:
                menu_admin()

                opcao = escolha(0, 3)

                if opcao == 1:
                    adicionar_prato()
                
                elif opcao == 2:
                    remover_prato()
                
                elif opcao == 3:
                    gerenciar_pedidos()

                elif opcao == 0:
                    gerar_relatorio()
                    break
    elif opcao == 2:
        registrar()
    else:
        print(f"Saindo...")
        break