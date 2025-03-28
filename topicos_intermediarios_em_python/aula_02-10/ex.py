# Método SMTP

# import smtplib
# zozt npry nlfh cgfp

# servidor = smtplib.SMTP('smtp.gmail.com', 587)
# servidor.starttls()
# servidor.login('pedro.melchiordeoliveira@gmail.com', 'zozt npry nlfh cgfp')
# mensagem = "Subject: Teste\n\nOla, este e um teste."
# servidor.sendmail('pedro.melchiordeoliveira@gmail.com', 'pedro.melchiordeoliveira@gmail.com', mensagem)
# servidor.quit()

# Método Módulo Email

# import smtplib

# servidor = smtplib.SMTP('smtp.gmail.com', 587)
# servidor.starttls()
# servidor.login('pedro.melchiordeoliveira@gmail.com', 'zozt npry nlfh cgfp')


# from email.message import EmailMessage

# msg = EmailMessage()
# msg['Subject'] = 'Teste'
# msg['From'] = 'pedro.melchiordeoliveira@gmail.com'
# msg['To'] = 'pedro.melchiordeoliveira@gmail.com'
# msg.set_content('Olá, este é um teste!')
# servidor.send_message(msg)

# # Email com anexos

# import smtplib

# servidor = smtplib.SMTP('smtp.gmail.com', 587)
# servidor.starttls()
# servidor.login('pedro.melchiordeoliveira@gmail.com', 'zozt npry nlfh cgfp')


# from email.message import EmailMessage


# msg = EmailMessage()
# msg['Subject'] = 'Relatório Semanal'
# msg['From'] = 'pedro.melchiordeoliveira@gmail.com'
# msg['To'] = 'pedro.melchiordeoliveira@gmail.com'
# msg.set_content('Segue em anexo o relatório semanal.')


# with open('topico_intermediarios_em_python/aula_02-10/teste.txt', 'rb') as arquivo:
#     conteudo = arquivo.read()
#     msg.add_attachment(conteudo, maintype='application', subtype='txt', filename='teste.txt')

# servidor.send_message(msg)

# Enviando email com formatação HTML contendo cabeçalho e um parágrafo

# import smtplib

# servidor = smtplib.SMTP('smtp.gmail.com', 587)
# servidor.starttls()
# servidor.login('pedro.melchiordeoliveira@gmail.com', 'zozt npry nlfh cgfp')

# from email.message import EmailMessage

# msg = EmailMessage()
# msg['Subject'] = 'Relatório Semanal'
# msg['From'] = 'pedro.melchiordeoliveira@gmail.com'
# msg['To'] = 'pedro.melchiordeoliveira@gmail.com'
# msg.set_content('Email com formatação HTML')

# msg.add_alternative("""
# <html>
#     <body>
#     <h1>Relatório Semanal</h1>
#     <p>Confira os resultados no anexo.</p>
#     </body>
# </html>
# """, subtype='html')

# servidor.send_message(msg)

# Função para enviar emails para uma lista de destinatários com mensagens personalizadas.

# import smtplib
# from email.message import EmailMessage


# servidor = smtplib.SMTP('smtp.gmail.com', 587)
# servidor.starttls()
# servidor.login('pedro.melchiordeoliveira@gmail.com', 'zozt npry nlfh cgfp')



# lista_destinatarios = ['pedro.melchiordeoliveira@gmail.com', 'pedro.oliveira10@sou.ufmt.br', 'pedrinpmo879@gmail.com']

# def enviar_email(lista):

#     servidor = smtplib.SMTP('smtp.gmail.com', 587)
#     servidor.starttls()
#     servidor.login('pedro.melchiordeoliveira@gmail.com', 'zozt npry nlfh cgfp')

#     for destinatario in lista:
#         msg = EmailMessage()
#         msg['Subject'] = 'Relatório Semanal'
#         msg['From'] = 'pedro.melchiordeoliveira@gmail.com'
#         msg['To'] = destinatario
#         msg.set_content(f'Olá {destinatario[:destinatario.find('@')]}')
#         servidor.send_message(msg)

# enviar_email(lista_destinatarios)

# Script que leia um arquivo csv com uma lista de destinatários e suas mensagens e envie os emails

# import csv
import smtplib
from email.message import EmailMessage

# with open('topico_intermediarios_em_python/aula_02-10/emails_msg.csv', 'r') as arquivo:
#     conteudo = csv.reader(arquivo)

#     for linha in conteudo:
#         email = linha[0]
#         mensagem = linha[1]

#         servidor = smtplib.SMTP('smtp.gmail.com', 587)
#         servidor.starttls()
#         servidor.login('pedro.melchiordeoliveira@gmail.com', 'zozt npry nlfh cgfp')
#         msg = EmailMessage()
#         msg['Subject'] = 'Felicidade'
#         msg['From'] = 'pedro.melchiordeoliveira@gmail.com'
#         msg['To'] = email
#         msg.set_content(mensagem)
#         servidor.send_message(msg)

# Envie um relatório em pdf diariamente às 9h para uma lista de emails

import schedule
import time
def enviar_email(email):
    msg = EmailMessage()
    msg['Subject'] = 'Relatório Semanal'
    msg['From'] = 'pedro.melchiordeoliveira@mgial.com'
    msg['To'] = email
    msg.set_content('Segue em anexo o relatório semanal.')
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login('pedro.melchiordeoliveira@gmail.com', 'zozt npry nlfh cgfp')
    servidor.send_message(msg)
    print("E-mail enviado!")

schedule.every().day.at("09:00").do(enviar_email('pedro.oliveira10@sou.ufmt.br'))
while True:
    schedule.run_pending()
    time.sleep(1)



