from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import analisa_sentimento as sentimento
import enviar_email as email

# Função para responder ao comando /start
async def start(update: Update, context) -> None:
    await update.message.reply_text(f'Olá, eu sou o BOT de Atendimento ao Cliente da empresa X!\nDigite /ajuda caso precisar de instruções de uso.')

# Variáveis globais
insatisfeito = False
recebeu_cupom = False

# Função para repetir mensagens de texto
async def analisa_sentimento(update: Update, context) -> None:
    user_message = update.message.text
    
    sentimento_resultado = sentimento.testa_sentimento(user_message)

    if sentimento_resultado == 'positivo':
        await update.message.reply_text(f'Que bom que você está satisfeito! Agradecemos pelo seu feedback')
        email.envia_relatorio(sentimento_resultado)    

    elif sentimento_resultado == 'negativo':
        await update.message.reply_text(f'Peço desculpas pela instafisfação, use o comando /email (seu email) para que possamos enviar um cupom de desconto')

        global insatisfeito
        insatisfeito = True

        email.envia_relatorio(sentimento_resultado)

    else:
        await update.message.reply_text("""
Seja bem-vindo(a) ao Atendimento ao Cliente da empresa X! Segue uma lista de comandos disponíveis:

/comando1 - Descrição comando1
/comando2 - Descrição comando2
""")
    
    # enviar log

async def pedido_desculpa(update: Update, context) -> None:
    global insatisfeito
    global recebeu_cupom

    if insatisfeito and not recebeu_cupom:
        email.enviar_cupom(context.args[0])

        await update.message.reply_text(f'Um cupom de desconto foi enviado para o email {context.args[0]}')

        insatisfeito = False
        recebeu_cupom = True

    elif not insatisfeito and recebeu_cupom:
        await update.message.reply_text(f'Você não está válido para receber um cupom de desconto')

    # salva email no log

async def ajuda(update: Update, context) -> None:

    funcionamento = """
Digite uma mensagem de feedback para nos ajudar a melhorar nosso serviço de atendimento!
    """

    await update.message.reply_text(f'{funcionamento}')

# Configuração e execução do bot
def main():

# Insira o token do seu bot aqui
    token = '7599043583:AAEJ6zzdoecDfhLhqLYyBb3r3LdVMeoWaCI'

# Cria a aplicação
    application = Application.builder().token(token).build()

# Registra os handlers
    application.add_handler(CommandHandler("start", start)) # Responde ao /start
    application.add_handler(CommandHandler("ajuda", ajuda))
    application.add_handler(CommandHandler("email", pedido_desculpa))

    application.add_handler(MessageHandler(filters.TEXT, analisa_sentimento))

# Inicia o bot
    print("Bot está rodando...")
    application.run_polling()



main()