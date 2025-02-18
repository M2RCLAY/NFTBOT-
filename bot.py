import telebot

TOKEN = 7608640319:AAGQ8mnGmHegxvYgJZAy-svUUmMfajeg2wo
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id, "مرحبًا بك في متجر NFT!")

bot.polling()
