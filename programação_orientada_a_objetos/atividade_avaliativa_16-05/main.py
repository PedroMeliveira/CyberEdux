from modulo import *

menu()
cria_tabela()

clicou = False
trans = cria_trans()
pag_id = insert_pagamento_retorna_id(trans)



if trans.metodo == 'Crédito':
    pagamento = cria_credito()
    st.markdown('---')
    if st.button("Confirmar pagamento"):
        insert_credito(pagamento, pag_id)
        st.write("✅ Pagamento Confirmado e Salvo!")
    
elif trans.metodo == 'Paypal':
    pagamento = cria_paypal()
    st.markdown('---')
    if st.button("Confirmar pagamento"):
        insert_paypal(pagamento, pag_id)
        st.write("✅ Pagamento Confirmado e Salvo!")
    
elif trans.metodo == 'Transferência Bancária':
    pagamento = cria_bancaria()
    st.markdown('---')
    if st.button("Confirmar pagamento"):
        insert_trans_bancaria(pagamento, pag_id)
        st.write("✅ Pagamento Confirmado e Salvo!")
