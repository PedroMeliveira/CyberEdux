# 7763859912:AAEyPAs38QQaF84wY0-n4fb3jmpHc5mcXRk
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import csv

# Função para responder ao comando /start

comandos = ['/start', '/hello', '/help', '/foto', '/votar', '/resultado']

async def start(update: Update, context) -> None:
    await update.message.reply_text("Olá! Eu sou um bot simples. Envie-me uma mensagem e eu a repetirei.")

async def hello(update: Update, context) -> None:
    await update.message.reply_text("Olá, mundo!")

async def help(update: Update, context) -> None:
    await update.message.reply_text(f'Os comandos disponíveis são: ')
    for comando in comandos:
        await update.message.reply_text(f'{comando}')

async def foto(update: Update, context) -> None:
    await update.message.reply_photo('topicos_intermediarios_em_python/aula_02-12/macaco.jpg')

async def votar(update: Update, context) -> None:
    with open('aula_12-02/votar.csv', 'r') as arquivo:
        conteudo = csv.reader(arquivo)
        dados = []
        for dado in conteudo:
            dados.append(dado)
        await update.message.reply_text(f'O Homem-Aranha é o melhor super-herói? Responda o usando o comando /votar (sim ou não).')
        if context.args[0].lower()[0] == 's':
            dados[0][0] += 1
            await update.message.reply_text(f'Você votou Sim!')
        elif context.args[0].lower()[0] == 'n':
            dados[0][1] += 1
            await update.message.reply_text(f'Você votou Não!')
    with open('topicos_intermediarios_em_python/aula_02-12/votar.csv', 'w') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(dados)

async def resultado(update: Update, context) -> None:
    with open('topicos_intermediarios_em_python/aula_02-12/votar.csv', 'r') as arquivo:
        conteudo = csv.reader(arquivo)
        dados = []
        for dado in conteudo:
            dados.append(dado)
        await update.message.reply_text(f'{dados[0][0]} - Votaram SIM\n{dados[0][1]} - Votaram NÃO')

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
    application.add_handler(CommandHandler("resultado", resultado)) 
    application.add_handler(CommandHandler("votar", votar)) 
    application.add_handler(CommandHandler("foto", foto)) 
    application.add_handler(MessageHandler(filters.TEXT, echo)) 

    print("Bot está rodando...")

    application.run_polling()

main()

