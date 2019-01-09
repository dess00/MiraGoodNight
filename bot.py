# -*- coding: utf-8 -*-
import telebot
import config
import re
from telebot import types
# тупа library for py and N.E.R
bot = telebot.TeleBot(config.token)

# hello message
@bot.message_handler(commands=["start"])
def hello_photo_message(message):
    bot.send_photo(message.from_user.id, config.photoid)  
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('/nav')
    bot.send_message(message.chat.id, config.helloworld, reply_markup=user_markup)   

# помощь во всем
@bot.message_handler(commands=["help"])
def help_message(message):
    bot.send_message(message.chat.id, config.support)

# не знаю для чего,не знаю зачем,но пусть будет
@bot.message_handler(commands=['QLG'])    
def nottonight(message):
    bot.send_message(message.chat.id, config.nottonight)

# клавиатура url
@bot.message_handler(commands=["nav"])
def default_test(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Канал", url="t.me/NERabout")
    url_button2 = types.InlineKeyboardButton(text="Чат", url="t.me/joinchat/I9h0pRRp0pzQiuc_cXxoyg")
    url_button3 = types.InlineKeyboardButton(text="Shop🔒", url="t.me/NERabout")
    keyboard.add(url_button,url_button2,url_button3)

    bot.send_message(message.chat.id, "Хммммм,куда бы тебя перенести?", reply_markup=keyboard)

# Неподдерживаемый текст
@bot.message_handler (content_types=['text'])
def handle_stop(message):
    bot.send_message(message.chat.id, config.error)
    
if __name__ == '__main__':
     bot.polling(none_stop=True)     
