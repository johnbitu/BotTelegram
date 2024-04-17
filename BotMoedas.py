import telebot
import schedule
import time

CHAVE_API = "6737603177:AAGz3AlDfFQzxmrHFo9-UWT6xH5SrHpaH3Q"

bot = telebot.TeleBot(CHAVE_API)

def enviar_mensagem():
    mensagem = """Fala meu chapa! Hora de ganhar dinheiro!!!

Já fez as missões da $PARAM?
https://paramgaming.com/?referCode=7A7CB49635#/signup

Já fez as missões da $KNRY?
https://zealy.io/cw/kanarylastsession"""
    bot.send_message("-4150847080", mensagem)

# Agendar o envio da mensagem de hora em hora
schedule.every().day.at("10:26").do(enviar_mensagem)
schedule.every().day.at("16:10").do(enviar_mensagem)
schedule.every().day.at("21:30").do(enviar_mensagem)

# Loop para executar o bot
while True:
    # Verificar se há tarefas agendadas
    schedule.run_pending()
    # Esperar um pouco antes de verificar novamente
    time.sleep(10)  # Ajuste o tempo de espera conforme necessário

# Iniciar o bot para responder a mensagens de entrada
@bot.message_handler(func=lambda message: True)
def responder(mensagem):
    bot.reply_to(mensagem, "Fala meu chapa!!!")
    bot.polling(none_stop=True, timeout=60)

# Se você preferir que o bot execute apenas uma vez e depois pare, pode usar bot.polling() em vez do loop while acima.
# bot.polling()
