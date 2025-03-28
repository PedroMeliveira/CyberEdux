import smtplib
from email.message import EmailMessage
from datetime import datetime
import re


def validador_email(email):
    pattern = '^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False


def enviar_confirmacao_email(email_cliente, nome, pedido, tempo, endereco, status):
    msg = EmailMessage()

    msg['Subject'] = "Confirmação de Pedido"
    msg['From'] = "zinumateus@gmail.com"
    msg['To'] = email_cliente
    msg.set_content(f'Seu pedido foi confirmado, {nome}!\n\nPrato: {pedido}\nEndereço de entrega: {endereco}\nPrazo de entrega: {tempo} minutos\nStatus do pedido: {status}\n\n')

    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login('zinumateus@gmail.com', 'rpfe tskv xzsq enru')
    servidor.send_message(msg)
    servidor.quit()


def enviar_relatorio_diario(pedidos):
    relatorio =f'Relatório de vendas do dia {datetime.now().strftime("%d/%m/%Y")}\n\n'
    
    total_vendas = 0
    for user_id, pedido in pedidos.items():
        pratos = ""
        for i in range(len(pedido["prato"])):
            if i + 1 == len(pedido["prato"]):
                pratos += f'{pedido["prato"][i]}'
                break
            pratos += f'{pedido["prato"][i]}, '
        relatorio += f'{'=' * 30}\nID do usuário: {user_id}\nPrato: {pratos}\nStatus: {pedido['status']}\nCódigo: {pedido['codigo']}\n'
        total_vendas += pedido["preco"]

    relatorio += f'\nTotal de Vendas: R$ {total_vendas:.2f}'

    msg = EmailMessage()
    msg.set_content(relatorio)
    
    msg['Subject'] = "Relatório de Vendas"
    msg['From'] = "zinumateus@gmail.com"
    msg['To'] = "zinumateus@gmail.com"

    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login('zinumateus@gmail.com', 'rpfe tskv xzsq enru')
    servidor.send_message(msg)
    servidor.quit()


def enviar_promocao(email_cliente):
    msg = EmailMessage()
    msg.set_content(f'Obrigado pelo seu feedback!\n\nAqui está um cupom de desconto para utilizar em próximas compras:\n\nCumpo: CUPOM15')

    msg['Subject'] = "Promoção Especial - Restaurante"
    msg['From'] = "zinumateus@gmail.com"
    msg['To'] = email_cliente

    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login('zinumateus@gmail.com', 'rpfe tskv xzsq enru')
    servidor.send_message(msg)
    servidor.quit()