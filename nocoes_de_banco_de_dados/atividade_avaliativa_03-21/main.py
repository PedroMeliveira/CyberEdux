from funcoes import *

cria_tabelas_sql()
insert_admin()
insert_cardapio_fixo()

while True:
    menu_out()

    opcao = escolha(0, 2)

    if opcao == 1:

        id_cliente = login()

        while True and id_cliente != '' and id_cliente != 0:
            menu_cliente()

            opcao = escolha(0, 2)

            if opcao == 1:
                opcao_cardapio()

            elif opcao == 2:
                fazer_pedido(id_cliente)
            else:
                break
        
        if id_cliente == '0':
            menu_admin()

            opcao = escolha(0, 3)

            if opcao == 1:
                adicionar_prato()
            
            elif opcao == 2:
                remover_prato()
            
            elif opcao == 3:
                

