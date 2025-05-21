from modulo import *

menu()

trans = cria_pagamento()

if trans.metodo == 'Crédito':
    credito = cria_credito()

if trans.metodo == 'Paypal':
    paypal = cria_paypal()