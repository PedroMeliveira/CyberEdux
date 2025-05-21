from modulo import *

menu()
cria_tabela()

trans = cria_trans()

if trans.metodo == 'Crédito':
    pagamento, validado = cria_credito()
    st.markdown('---')
    if validado:
        if st.button("Confirmar pagamento"):
            pag_id = insert_pagamento_retorna_id(trans)
            insert_credito(pagamento, pag_id)
            st.write("✅ Pagamento Confirmado e Salvo!")
    
elif trans.metodo == 'Paypal':
    pagamento, validado = cria_paypal()
    st.markdown('---')
    if validado:
        if st.button("Confirmar pagamento"):
            pag_id = insert_pagamento_retorna_id(trans)
            insert_paypal(pagamento, pag_id)
            st.write("✅ Pagamento Confirmado e Salvo!")
    
elif trans.metodo == 'Transferência Bancária':
    pagamento, validado = cria_bancaria()
    st.markdown('---')
    if validado:
        if st.button("Confirmar pagamento"):
            pag_id = insert_pagamento_retorna_id(trans)
            insert_trans_bancaria(pagamento, pag_id)
            st.write("✅ Pagamento Confirmado e Salvo!")
