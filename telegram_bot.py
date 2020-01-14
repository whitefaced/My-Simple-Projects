import telebot

bot = telebot.TeleBot('925294229:AAFBqbzgCxMKEoJv2hQoDVk1--ffpJqmWZ8')

@bot.message_handler(content_types=['text'])
def reply_to_message(message):
    bot.send_message(message.chat.id, message.text)

if name == "main":
    bot.infinity_polling()
