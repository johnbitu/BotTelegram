import telebot
import schedule
import time

CHAVE_API = "6737603177:AAGz3AlDfFQzxmrHFo9-UWT6xH5SrHpaH3Q"

bot = telebot.TeleBot(CHAVE_API)

def enviar_mensagem():
    # Aqui você pode personalizar a mensagem que deseja enviar
    mensagem = (""""Fala meu chapa! Hora de ganhar dinheiro!!!"
                  
 Já fez as missões da $PARAM?
              
 https://paramgaming.com/?referCode=7A7CB49635#/signup
              
 Já fez as missões da $KNRY?
                
 https://zealy.io/cw/kanarylastsession
    """)
    # Enviar a mensagem para todos os usuários (ou chat) que deseja
    # Você pode substituir "123456789" pelo ID do chat para onde deseja enviar a mensagem
    bot.send_message("-4150847080", mensagem)

# Agendar o envio da mensagem de hora em hora
schedule.every().day.at("10:26").do(enviar_mensagem)
schedule.every().day.at("15:30").do(enviar_mensagem)
schedule.every().day.at("21:30").do(enviar_mensagem)

# Função para permitir que o bot responda a mensagens de entrada
def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.reply_to(mensagem, "Fala meu chapa!!!")

# Loop para executar o bot
while True:
    # Verificar se há tarefas agendadas
    schedule.run_pending()
    # Esperar um pouco antes de verificar novamente
    
    bot.polling(none_stop=True, timeout=60, host='0.0.0.0')

# Se você preferir que o bot execute apenas uma vez e depois pare, pode usar bot.polling() em vez do loop while acima.
# bot.polling()
