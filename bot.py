import os

import telebot
from gradio_client import Client
BOT_TOKEN = '6111719383:AAFD6T-cb_d4JOlUoP1m-wuG5HWGSvCpWD4'
client = Client("https://io-runwayml-stable-diffusion-v1-5.hf.space/")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    result = client.predict(str(message.text),api_name="/predict")
    photo1 = open(str(result), 'rb')
    bot.send_photo(message.chat.id, photo1)
    #bot.reply_to(message, message.text)
bot.infinity_polling()
