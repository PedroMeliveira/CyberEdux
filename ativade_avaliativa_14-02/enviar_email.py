import smtplib
from email.message import EmailMessage
import json

def envia_relatorio(sentimento):

    msg = EmailMessage()
    msg['Subject'] = 'Relatório Feedback'
    msg['From'] = 'pedro.melchiordeoliveira@gmail.com'
    msg['To'] = 'pedro.melchiordeoliveira@gmail.com'
    msg.set_content('Segue o relatório do feedback dos clientes')

    try:

        with open('feedback.json', 'r') as arquivo:
            conteudo = json.load(arquivo)
            conteudo[sentimento] += 1
        
        with open('feedback.json', 'w') as arquivo:
            json.dump(conteudo, arquivo)

    except FileNotFoundError:

        with open('feedback.json', 'w') as arquivo:
            arquivo_base = {
                "positivo": 0,
                "negativo": 0
            }

            json.dump(arquivo_base, arquivo)
        
        with open('feedback.json', 'r') as arquivo:
            conteudo = json.load(arquivo)
            conteudo[sentimento] += 1
        
        with open('feedback.json', 'w') as arquivo:
            json.dump(conteudo, arquivo)
            
    total = sum(conteudo.values())
    msg.set_content(f"""
Sentimentos positivos: {conteudo["positivo"]}       ||      {conteudo["positivo"] / total * 100}%
Sentimentos Negativos: {conteudo["negativo"]}       ||      {conteudo["negativo"] / total * 100}%
""")

    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login('pedro.melchiordeoliveira@gmail.com', 'zozt npry nlfh cgfp')
    servidor.send_message(msg)
    servidor.quit()


def enviar_cupom(email):

    msg = EmailMessage()
    msg['Subject'] = 'Cupom de Desconto'
    msg['From'] = 'zinumateus@gmail.com'
    msg['To'] = email
    msg.set_content('Pedimos perdão pela insatisfação, aqui está um cupom de desconto: XXXX-XXXX-XXXX')

    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login('zinumateus@gmail.com', 'rpfe tskv xzsq enru')
    servidor.send_message(msg)
    servidor.quit()