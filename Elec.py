import telebot
from telebot import types
import random
import os

Token = '665567135:AAGdohyS5FcrQ5sVvQEMcQPqV6k8G-tbH-I'
bot = telebot.TeleBot(Token)

@bot.message_handler(commands = ['start'])
def start(message):
    kek = ('Выберите вариант: \n'
           '/el1 , /el2 , /el3 , /el4 , /el5 , /el6 ,\n'
           '/el7 , /el8 , /el9 , /el10 , /el11, /el12 , \n'
           '/el13 , /el14 , /el15 , /el16 , /el17 , /el18 \n'
           '/el19 , /el20 , /el21 , /el22 , /el23 , /el24 , ''/el25')
    bot.send_message(message.chat.id, kek)


@bot.message_handler(content_types=['text'])
def elec(message):
    if message.text == '/el1':
        bot.send_message(message.chat.id, 'Вариант 1\n''1)E  2)B  3)A  4)B  5)C  6)E  7)C  8)B  9)D  10)D \n'
                                          '11)D  12)A  13)A  14)B  15)E  16)E  17)A  18)C 19)B 20)D')
    if message.text == '/el2':
        bot.send_message(message.chat.id, 'Вариант 2\n''1)A  2)D  3)A  4)E  5)C  6)B  7)D  8)E  9)B  10)A \n'
                                          '11)E  12)C  13)A  14)D  15)C  16)B  17)E  18)A 19)E 20)D')
    if message.text == '/el3':
        bot.send_message(message.chat.id, 'Вариант 3\n''1)D  2)C  3)C  4)B  5)E  6)E  7)E  8)C  9)B  10)D \n'
                                          '11)B  12)B  13)C  14)A  15)B  16)D  17)C  18)B 19)C 20)A')
    if message.text == '/el4':
        bot.send_message(message.chat.id, 'Вариант 4\n''1)A  2)E  3)D  4)A  5)B  6)C  7)C  8)E  9)B  10)D \n'
                                          '11)C  12)C  13)B  14)B  15)A  16)B  17)E  18)E 19)D 20)B')
    if message.text == '/el5':
        bot.send_message(message.chat.id, 'Вариант 5\n''1)C  2)B  3)A  4)A  5)B  6)D  7)C  8)D  9)D  10)E \n'
                                          '11)E  12)C  13)B  14)E  15)B  16)A  17)D  18)D 19)A 20)B')
    if message.text == '/el6':
        bot.send_message(message.chat.id, 'Вариант 6\n''1)D  2)B  3)A  4)E  5)E  6)B  7)B  8)B  9)C  10)D \n'
                                          '11)E  12)A  13)B  14)A  15)C  16)D  17)A  18)B 19)C 20)A')
    if message.text == '/el7':
        bot.send_message(message.chat.id, 'Вариант 7\n''1)B  2)B  3)A  4)B  5)C  6)E  7)C  8)B  9)D  10)D \n'
                                          '11)D  12)A  13)A  14)B  15)E  16)E  17)A  18)C 19)B 20)D')
    if message.text == '/el8':
        bot.send_message(message.chat.id, 'Вариант 8\n''1)A  2)E  3)C  4)B  5)C  6)E  7)E  8)E  9)E  10)A \n'
                                          '11)B  12)A  13)B  14)B  15)C  16)B  17)D  18)E 19)D 20)D')

    if message.text == '/el9':
        bot.send_message(message.chat.id, 'Вариант 9\n''1)C  2)E  3)C  4)C  5)E  6)D  7)A  8)C  9)D  10)C \n'
                                          '11)E  12)B 13)A  14)D  15)A  16)B  17)B  18)E 19)D 20)B')
    if message.text == '/el10':
        bot.send_message(message.chat.id, 'Вариант 10\n''1)A  2)D  3)A  4)D  5)B  6)B  7)E  8)C  9)E  10)A \n'
                                          '11)B  12)C  13)C  14)D  15)B  16)A  17)E  18)D 19)A 20)B')
    if message.text == '/el11':
        bot.send_message(message.chat.id, 'Вариант 11\n''1)B  2)D  3)C  4)D  5)C  6)E  7)E  8)C  9)B  10)E \n'
                                          '11)A  12)B  13)E  14)D  15)E  16)B  17)B 18)E 19)C 20)B')
    if message.text == '/el12':
        bot.send_message(message.chat.id, 'Вариант 12\n''1)E  2)B  3)B  4)B  5)C  6)D  7)E  8)A  9)B  10)A \n'
                                          '11)C  12)D  13)D  14)C  15)B  16)A  17)E  18)C 19)B 20)E')
    if message.text == '/el15':
        bot.send_message(message.chat.id, 'Вариант 13\n''1)B  2)D  3)C  4)D  5)D  6)E  7)E  8)C  9)B  10)E \n'
                                          '11)B  12)D  13)A  14)D  15)B  16)B  17)E  18)C 19)E 20)D')
    if message.text == '/el13':
        bot.send_message(message.chat.id, 'Вариант 14\n''1)B  2)A  3)E  4)C  5)B  6)D  7)D  8)E  9)A  10)B \n'
                                          '11)D  12)E  13)C  14)B  15)C  16)E  17)E  18)D 19)E 20)E')
    if message.text == '/el14':
        bot.send_message(message.chat.id, 'Вариант 15\n''1)C  2)E  3)E  4)D  5)B  6)C  7)B  8)A  9)B  10)B \n'
                                          '11)C  12)B  13)C  14)C  15)A  16)D  17)A  18)C 19)D 20)E')
    if message.text == '/el16':
        bot.send_message(message.chat.id, 'Вариант 16\n''1)E  2)C  3)B  4)D  5)D  6)E  7)A  8)B  9)D  10)E \n'
                                          '11)B  12)A  13)B  14)C  15)E  16)E  17)B  18)C 19)D 20)E')
    if message.text == '/el17':
        bot.send_message(message.chat.id, 'Вариант 17\n''1)E  2)D  3)E  4)C  5)B  6)A  7)B  8)B  9)A  10)A \n'
                                          '11)D  12)A  13)E  14)C  15)E  16)D  17)E  18)B 19)A 20)A')
    if message.text == '/el18':
        bot.send_message(message.chat.id, 'Вариант 18\n''1)A  2)C  3)D  4)C  5)C  6)B  7)A  8)D  9)A  10)D \n'
                                          '11)C  12)C  13)B  14)E  15)E  16)E  17)B  18)C 19)D 20)D')
    if message.text == '/el19':
        bot.send_message(message.chat.id, 'Вариант 19\n''1)E  2)C  3)E  4)A  5)B  6)C  7)C  8)D  9)B  10)C \n'
                                          '11)D  12)C  13)C  14)B  15)A  16)D  17)D  18)B 19)E 20)E')
    if message.text == '/el20':
        bot.send_message(message.chat.id, 'Вариант 20\n''1)E  2)C  3)B  4)E  5)B  6)B  7)A  8)E  9)E  10)C \n'
                                          '11)A  12)C  13)B  14)D  15)D  16)A  17)C  18)D 19)C 20)C')
    if message.text == '/el21':
        bot.send_message(message.chat.id, 'Вариант 21\n''1)A  2)E  3)E  4)B  5)D  6)E  7)E  8)D  9)B  10)B \n'
                                          '11)E  12)A  13)E  14)D  15)B  16)E  17)C  18)B 19)A 20)E')
    if message.text == '/el22':
        bot.send_message(message.chat.id, 'Вариант 22\n''1)E  2)C  3)C  4)A  5)C  6)D  7)E  8)A  9)B  10)D \n'
                                          '11)C  12)B  13)E  14)A  15)E  16)E  17)B  18)B 19)E 20)B')
    if message.text == '/el23':
        bot.send_message(message.chat.id, 'Вариант 23\n''1)C  2)B  3)C  4)E  5)B  6)D  7)D  8)C  9)A  10)B \n'
                                          '11)E  12)E  13)D  14)B  15)D  16)E  17)A  18)B 19)A 20)C')
    if message.text == '/el24':
        bot.send_message(message.chat.id, 'Вариант 24\n'
                                          '1)C  2)C  3)E  4)D  5)E  6)C  7)B  8)C  9)E  10)A \n'
                                          '11)D  12)D  13)A  14)B  15)D  16)D  17)E  18)A 19)B 20)C')
    if message.text == '/el25':
        bot.send_message(message.chat.id, 'Вариант 25\n'
                                          '1)A  2)D  3)B  4)B  5)D  6)E  7)E  8)B  9)D  10)C \n'
                                          '11)D  12)D  13)B  14)C  15)C  16)B  17)B  18)A 19)C 20)D')








if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)