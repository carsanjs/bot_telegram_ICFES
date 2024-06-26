import telebot

bot = telebot.TeleBot('TOKEN', parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(commands=['start', 'stop', 'continue'])
async def start(message):
    bot.reply_to(message, "Howdy, how are you doing?")
    