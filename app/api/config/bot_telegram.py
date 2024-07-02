import telebot
from api.endpoint.icfes import main

#INICIAR CONEXIÓN
bot = telebot.TeleBot('TOKEN', parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

user_data = {}

@bot.message_handler(commands=['start'])
async def start_send(message):
    bot.send_message(message.chat.id, "Hola! Consulta tu resultado del ICFES ejecuntando el comando /consultar")
    bot.send_animation(message.chat.id, "https://th.bing.com/th/id/OIP.bVHRuKHzYMpQYu1-VS_bPQHaD5?rs=1&pid=ImgDetMain")
    # bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['consultar'])
async def consulta_send(message):
    # user_data[message.chat.id]['registro'] = message.text
    user_data[message.chat.id] = {'step': 1}
    bot.send_message(message.chat.id, "por favor, ingresa tu numero de registro")
    user_data[message.chat.id]['step'] = 2

@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get('step') == 1)
async def driver_register(message):
    user_data[message.chat.id]['registro'] = message.text
    bot.send_message(message.chat.id, "Ahora, por favor, ingresa tu numero de documento")
    user_data[message.chat.id] = {'step': 2}

@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get('step') == 2)
async def driver_document(message):
    user_data[message.chat.id]['documento'] = message.text
    bot.send_message(message.chat.id, "Por ultimo el tipo de documento (TI,CC)")
    user_data[message.chat.id] = {'step': 3}

@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get('step') == 3)
async def driver_td(message):
    user_data[message.chat.id]['td'] = message.text
    registro = user_data[message.chat.id]['registro']
    documento = user_data[message.chat.id]['documento']
    td = user_data[message.chat.id]['td']
    response, pdf = main(registro, documento, td)
    bot.send_message(message.chat.id, "Ahora, por favor, ingresa tu numero de documento")
    user_data[message.chat.id] = {'step': 2}




@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()