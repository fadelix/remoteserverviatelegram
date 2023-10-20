import time
#using pip install pyTelegramBotAPI
import telebot
import os
import requests

token = 'inputyourtoken'
bot = telebot.TeleBot(token)
rfile = ' >tmp.txt'
file = 'tmp.txt'
salah = 'command salah, mohon masukkan linux base command'

def get_msg(msg):
    for m in msg:
        chat = m.chat.id
        if m.content_type == 'text':
                text = m.text
                result = os.system(text + rfile)
                if result == 0:
                    kirim = open(file, 'rb')
                    bot.send_document(chat, kirim)
                else :
                    bot.send_message(chat, salah)


while True:
    try:
        bot.set_update_listener(get_msg)
        bot.polling()
    except Exception:
        time.sleep(15)
