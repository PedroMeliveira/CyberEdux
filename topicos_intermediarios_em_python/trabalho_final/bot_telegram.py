from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import email_funcoes as e
import json
from random import randint


CARDAPIO = "cardapio.json"
PEDIDOS = "pedidos.json"
AVALIACOES = "avaliacoes.json"


# Dicionário temporário para armazenar pedidos em andamento
usuarios_pedindo = {}


# Função para carregar o cardápio
def carregar_cardapio():
    try:
        with open(CARDAPIO, "r") as arquivos:
            return json.load(arquivos)
    except FileNotFoundError:
        return {}


# Função para carregar pedidos
def carregar_pedidos():
    try:
        with open(PEDIDOS, "r") as arquivos:
            return json.load(arquivos)
    except FileNotFoundError:
        return {}


# Função para salvar pedidos
def salvar_pedidos(pedidos):
    with open(PEDIDOS, "w") as arquivos:
        json.dump(pedidos, arquivos, indent=4)


# Comando /start
async def start(update: Update, context) -> None:

    await update.message.reply_text(f'Olá ☺! Bem-vindo ao nosso restaurante. Use  /cardapio para ver o menu e /fazerpedido para pedir.')


# Comando /cardapio
async def cardapio(update: Update, context: CallbackContext) -> None:
    cardapio = carregar_cardapio()

    if not cardapio:
        update.message.reply_text(f'O cardápio está vazio no momento 😥.')
        return
    
    mensagem = '📜 *Cardápio:*\n'
    numero_prato = 1
    for categoria, pratos in cardapio.items():
        mensagem += f'\n*{categoria.capitalize()}:*\n'
        for prato, preco in pratos.items():
            mensagem += f'🍽️ ({numero_prato}) {prato} - R$ {preco[0]:.2f}\n'
            numero_prato += 1
    
    await update.message.reply_text(mensagem, parse_mode="Markdown")


# Comando /fazerpedido
async def fazer_pedido(update: Update, context: CallbackContext) -> None:
    user_id = str(update.message.chat_id)
    usuarios_pedindo[user_id] = {"etapa": "prato"}

    await update.message.reply_text(f'Certo, comece digitando o *número do prato* que deseja pedir:', parse_mode="Markdown")



# Função para verificar a etapa do pedido
async def verificar_etapa(update: Update, context: CallbackContext) -> None:
    user_id = str(update.message.chat_id)

    if user_id in usuarios_pedindo:
        etapa = usuarios_pedindo[user_id].get("etapa")
        if etapa == "endereco":
            await receber_endereco(update, context)
        elif etapa == "email":
            await receber_email(update, context)
        elif etapa == "nome":
            await receber_nome(update, context)
        elif etapa == "resposta_pedido":
            await resposta_pedido(update, context)
        elif etapa == "resposta_cupom":
            await resposta_cupom(update, context)
        elif etapa == "validar_cupom":
            await validar_cupom(update, context)
        else:
            await receber_pedido(update, context)


# Receber nome do prato
async def receber_pedido(update: Update, context: CallbackContext) -> None:
    user_id = str(update.message.chat_id)

    existe_info = False
    for chave in usuarios_pedindo[user_id].keys():
        if chave == "prato":
            existe_info = existe_info or True

    if not existe_info:
        usuarios_pedindo[user_id]["prato"] = []


    pedido = update.message.text
    cardapio = carregar_cardapio()
    
    # Checar prato correspondente ao número digitado
    try:
        pedido = int(pedido)
        numero_valido = True
    except ValueError:    
        numero_valido = False

    if numero_valido:
        prato_encontrado = False
        i = 1
        for categoria in cardapio.values():
            for prato in categoria.keys():
                if i == pedido:
                    pedido = prato
                    prato_encontrado = True
                i += 1
    
    else:
        await update.message.reply_text(f'Erro ❌! Digite um número válido!')
        return

    if prato_encontrado:
        usuarios_pedindo[user_id]["prato"].append(pedido)
        usuarios_pedindo[user_id]["multiplicador_cupom"] = 1
        usuarios_pedindo[user_id]["etapa"] = "resposta_pedido"
        await update.message.reply_text(f'Item adicionado ✅! Deseja adicionar mais algo? (S/N)')

    else:   
        await update.message.reply_text(f'Desculpe, esse prato não está no cardápio ❌\nTente outro:')


# Receber resposta se quer adicionar mais itens
async def resposta_pedido(update: Update, context: CallbackContext) -> None:
    user_id = str(update.message.chat_id)
    continuar = update.message.text.lower()[0]

    if continuar != 's' and continuar != 'n':

        await update.message.reply_text(f'Opção inválida, digite novamente: ')
        return
    
    elif continuar == 's':
        usuarios_pedindo[user_id]["etapa"] = "pedido"
        await update.message.reply_text(f'Certo, digite o número do prato para adiciona-lo:')

    else:

        usuarios_pedindo[user_id]["etapa"] = "resposta_cupom"
        await update.message.reply_text(f'Deseja utilizar um cupom de desconto? (S/N)', parse_mode="Markdown")


# Resposta se quer usar cupom
async def resposta_cupom(update: Update, context: CallbackContext) -> None:
    user_id = str(update.message.chat_id)
    resposta = update.message.text.lower()[0]
    
    if resposta != 's' and resposta != 'n':

        await update.message.reply_text(f'Opção inválida, digite novamente: ')
        return

    elif resposta == 's':
        usuarios_pedindo[user_id]["etapa"] = "validar_cupom"
        await update.message.reply_text(f'Certo, digite o *cupom de desconto* para validá-lo:', parse_mode="Markdown")

    else:

        usuarios_pedindo[user_id]["etapa"] = "endereco"
        await update.message.reply_text(f'Certo, agora digite o *endereço* de entrega:', parse_mode="Markdown")


# Validar cupom
async def validar_cupom(update: Update, context: CallbackContext) -> None:
    user_id = str(update.message.chat_id)
    cupom = update.message.text

    if cupom == 'SAIR':

        usuarios_pedindo[user_id]["etapa"] = "endereco"
        await update.message.reply_text(f'Agora, digite o *endereço* de entrega:', parse_mode="Markdown")
        
    elif cupom != 'CUPOM15':

        await update.message.reply_text(f'Cupom inválido ❌! Digite *SAIR* caso queira cancelar o processo de validação', parse_mode="Markdown")

    elif cupom == 'CUPOM15':
        usuarios_pedindo[user_id]["multiplicador_cupom"] = 0.75
        usuarios_pedindo[user_id]["etapa"] = "endereco"
        await update.message.reply_text(f'Você aplicou um *cupom de desconto* no seu pedido 😊✅\n\nAgora, digite o *endereço* de entrega:', parse_mode="Markdown")



# Receber endereço
async def receber_endereco(update: Update, context: CallbackContext) -> None:
    user_id = str(update.message.chat_id)
    usuarios_pedindo[user_id]["endereco"] = update.message.text
    usuarios_pedindo[user_id]["etapa"] = "nome"
    
    await update.message.reply_text(f'Informe o *nome* para ser colocado no pedido:', parse_mode="Markdown")


#Receber nome
async def receber_nome(update: Update, context: CallbackContext) -> None:
    user_id = str(update.message.chat_id)
    usuarios_pedindo[user_id]["nome"] = update.message.text
    usuarios_pedindo[user_id]["etapa"] = "email"

    await update.message.reply_text(f'Agora, digite seu *email* para enviarmos um resumo de como ficou o pedido:', parse_mode="Markdown")


# Receber email e finalizar pedido
async def receber_email(update: Update, context: CallbackContext) -> None:
    user_id = str(update.message.chat_id)
    email = update.message.text
    if not e.validador_email(email):
        await update.message.reply_text(f'Email inválido, tente novamente: ')
        return

    usuarios_pedindo[user_id]["etapa"] = "Pedido feito"
    usuarios_pedindo[user_id]["email"] = email
    usuarios_pedindo[user_id]["status"] = "Em preparo"
    
    pedidos = carregar_pedidos()
    
    # Gera código do pedido e verifica se não tem outro igual
    mesmo_codigo = False
    while True: 
        codigo = randint(1000,9999)

        if not pedidos:
            break

        for info in pedidos.values():
            if info["codigo"] == codigo:
                mesmo_codigo = True
        
        if not mesmo_codigo:
            break
    
    cardapio = carregar_cardapio()
    preco = 0
    tempo_de_espera = 0
    for pedido in usuarios_pedindo[user_id]["prato"]:
        for pratos in cardapio.values():
            for prato, info in pratos.items():
                if prato == pedido:
                    preco += info[0]
                    tempo_de_espera += info[1]

    # Salva as informações do pedido do usuário
    pedidos[user_id] = usuarios_pedindo[user_id]
    pedidos[user_id]["codigo"] = str(codigo)
    pedidos[user_id]["preco"] = round(preco * usuarios_pedindo[user_id]["multiplicador_cupom"], 2)
    
    del usuarios_pedindo[user_id]["multiplicador_cupom"]
    
    pedidos[user_id]["tempo_de_espera"] = tempo_de_espera
    pedidos[user_id]["pode_avaliar"] = "NO"


    salvar_pedidos(pedidos)
    

    pratos = ""
    for i in range(len(usuarios_pedindo[user_id]["prato"])):
        if i + 1 == len(usuarios_pedindo[user_id]["prato"]):
            pratos += f'{usuarios_pedindo[user_id]["prato"][i]}'
            break
        pratos += f'{usuarios_pedindo[user_id]["prato"][i]}, '

    # Envia a confirmação por e-mail
    e.enviar_confirmacao_email(
        usuarios_pedindo[user_id]["email"], 
        usuarios_pedindo[user_id]["nome"],
        pratos,
        tempo_de_espera,
        usuarios_pedindo[user_id]["endereco"],
        "Em preparo"
    )


    await update.message.reply_text(
        text=f'Pedido confirmado ✅!\n\n' 
        f'*{pratos}* será entregue em *{usuarios_pedindo[user_id]["endereco"]}* para *{usuarios_pedindo[user_id]["nome"]}*!\nPrazo de entrega: *{tempo_de_espera} minutos*\nStatus: *Em preparo*\n\n'
        f'Acompanhe a stituação do seu pedido utilizando o comando */status*',
        parse_mode="Markdown"
        )
    
    del usuarios_pedindo[user_id]


# Função que sempre verifica o status do pedido, assim que o pedido for concluído, falar pra usar o /avaliar (voto) para avaliar
async def status(update: Update, context: CallbackContext) -> None:
    user_id = str(update.message.chat_id)
    pedidos = carregar_pedidos()

    if pedidos[user_id]:
        if pedidos[user_id]["status"] == "Em preparo":
            await update.message.reply_text(
                text=f'Seu pedido está sendo preparado! Tempo estimado: *{pedidos[user_id]["tempo_de_espera"]} minutos*',
                parse_mode="Markdown"
                )
            
        elif pedidos[user_id]["status"] == "Saiu para entrega":
            await update.message.reply_text(
                text=f'Seu pedido saiu para entrega 😊! Aguarde em *{pedidos[user_id]["endereco"]}* para recebê-lo 😁',
                parse_mode="Markdown",
            )

        elif pedidos[user_id]["status"] == "Entregue":
            pedidos[user_id]["pode_avaliar"] = "YES"
            salvar_pedidos(pedidos)
            
            await update.message.reply_text(f'🎉 Seu pedido foi entregue em *{pedidos[user_id]["endereco"]}*!\n\n'
                f'Gostaríamos que você avaliasse nosso serviço usando o comando: */avaliar (sua avaliação)* 😁',
                parse_mode="Markdown",
            )

    else:
        await update.message.reply_text(f'Você ainda não fez um pedido para verificar o status dele 😢')


# Avalia serviço
async def avaliar(update: Update, context: CallbackContext) -> None:
    user_id = str(update.message.chat_id)
    pedidos = carregar_pedidos()

    if pedidos[user_id]["pode_avaliar"] == "YES":
        args = update.message.text.split()[1:]
        if args:
            if len(args) == 1:
                if args[0] == '1' or args[0] == '2':
                    pedidos[user_id]["pode_avaliar"] = "NO"
                    salvar_pedidos(pedidos)
                    await update.message.reply_text(f'Sentimos muito que você não tenha gostado do nosso serviço 😥')

                elif args[0] == '3' or args[0] == '4':
                    pedidos[user_id]["pode_avaliar"] = "NO"
                    salvar_pedidos(pedidos)
                    await update.message.reply_text(f'Agradecemos pela sua avaliação 😁!')

                elif args[0] == '5':
                    e.enviar_promocao(pedidos[user_id]["email"])
                    pedidos[user_id]["pode_avaliar"] = "NO"
                    salvar_pedidos(pedidos)
                    await update.message.reply_text(f'Obrigado pelo feedback. Utilize o *cupom de desconto* enviado no email informado ao fazer pedido na sua próxima compra conosco 😎', parse_mode="Markdown")

                else:
                    await update.message.reply_text(f'Envie apenas uma avaliação de 1 a 5, sendo 1 péssimo e 5 ótimo.')

            else:
                await update.message.reply_text(f'Digite apenas uma avaliação numérica de 1 a 5 após o comando!')

        else:
            await update.message.reply_text(f'Por favor insira a sua avaliação de 1 a 5 após o comando /avaliar.\nExemplo: /avaliar (sua avaliação)')

    else:
        await update.message.reply_text(f'Você não pode avaliar 😓.\nEspere o seu pedido ser entregue para conseguir nos avaliar 😁')


# Configuração do bot

token = ("7784605439:AAHps8PumTSAqnldM7G85nad9YfnG7ujZrc")

application = Application.builder().token(token).build()

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("cardapio", cardapio))
application.add_handler(CommandHandler("fazerpedido", fazer_pedido))
application.add_handler(CommandHandler("avaliar", avaliar))
application.add_handler(CommandHandler("status", status))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, verificar_etapa))

application.run_polling()