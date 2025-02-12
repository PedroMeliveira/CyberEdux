# 7763859912:AAEyPAs38QQaF84wY0-n4fb3jmpHc5mcXRk
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Função para responder ao comando /start

comandos = ['/start', '/hello', '/help', '/foto']

async def start(update: Update, context) -> None:
    await update.message.reply_text("Olá! Eu sou um bot simples. Envie-me uma mensagem e eu a repetirei.")

async def hello(update: Update, context) -> None:
    await update.message.reply_text("Olá, mundo!")

async def help(update: Update, context) -> None:
    await update.message.reply_text(f'Os comandos disponíveis são: ')
    for comando in comandos:
        await update.message.reply_text(f'{comando}')

async def foto(update: Update, context) -> None:
    await update.message.reply_photo('aula_12-02/macaco.jpg')

async def echo(update: Update, context) -> None:
    user_message = update.message.text

    if user_message.lower() == 'oi':
        await update.message.reply_text("Como você está? ")
    else:
        await update.message.reply_text(f"Você disse: {user_message}")

    


# Configuração e execução do bot

def main():
    token = "7763859912:AAEyPAs38QQaF84wY0-n4fb3jmpHc5mcXRk" 
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start)) 
    application.add_handler(CommandHandler("hello", hello)) 
    application.add_handler(CommandHandler("help", help)) 
    application.add_handler(CommandHandler("foto", foto)) 
    application.add_handler(MessageHandler(filters.TEXT, echo)) 

    print("Bot está rodando...")

    application.run_polling()

main()

