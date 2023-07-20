from bs4 import BeautifulSoup
import requests
import telebot
import os
from os.path import join, dirname
from dotenv import load_dotenv
from telebot import types
def get_from_env(key):
    dotenv_path = join(dirname(__file__), 'token.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)
token = get_from_env('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(token)


url = 'https://ignio.com/r/export/utf/xml/daily/com.xml'
resp = requests.get(url)
with open('com.xml', 'wb') as f:
    f.write(resp.content)
with open('com.xml', 'r', encoding='utf-8') as f:
    data = f.read()

Bs_data = BeautifulSoup(data, "xml")
libra = Bs_data.find('libra')
libratoday = libra.find('today')
aries = Bs_data.find('aries')
ariestoday = aries.find('today')
taurus = Bs_data.find('taurus')
taurustoday = taurus.find('today')
gemini = Bs_data.find('gemini')
geminitoday = gemini.find('today')
cancer = Bs_data.find('cancer')
cancertoday = cancer.find('today')
leo = Bs_data.find('leo')
leotoday = leo.find('today')
virgo = Bs_data.find('virgo')
virgotoday = virgo.find('today')
scorpio = Bs_data.find('scorpio')
scorpiotoday = scorpio.find('today')
sagittarius = Bs_data.find('sagittarius')
sagittariustoday = sagittarius.find('today')
capricorn = Bs_data.find('capricorn')
capricorntoday = capricorn.find('today')
aquarius = Bs_data.find('aquarius')
aquariustoday = aquarius.find('today')
pisces = Bs_data.find('pisces')
piscestoday = pisces.find('today')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    aries = types.InlineKeyboardButton(text="Овен \u2648", callback_data="aries")
    taurus = types.InlineKeyboardButton(text="Телец \u2649", callback_data="taurus")
    gemini = types.InlineKeyboardButton(text="Близнецы \u264A", callback_data="gemini")
    cancer = types.InlineKeyboardButton(text="Рак \u264B", callback_data="cancer")
    leo = types.InlineKeyboardButton(text="Лев \u264C", callback_data="leo")
    virgo = types.InlineKeyboardButton(text="Дева \u264D", callback_data="virgo")
    libra = types.InlineKeyboardButton(text="Весы \u264E", callback_data="libra")
    scorpio = types.InlineKeyboardButton(text="Скорпион \u264F", callback_data="scorpio")
    sagittarius = types.InlineKeyboardButton(text="Стрелец \u2650", callback_data="sagittarius")
    capricorn = types.InlineKeyboardButton(text="Козерог \u2651", callback_data="capricorn")
    aquarius = types.InlineKeyboardButton(text="Водолей \u2652", callback_data="aquarius")
    pisces = types.InlineKeyboardButton(text="Рыбы \u2653", callback_data="pisces")
    markup.add(pisces, aquarius, capricorn, sagittarius, scorpio, libra, virgo, leo, cancer, gemini, taurus, aries)
    bot.send_message(message.chat.id, 'Выберите свой знак зоодиака и я пришлю вам предсказание на сегодня:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def test_callback(call): # <- passes a CallbackQuery type object to your function
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    back = types.KeyboardButton('Посмотреть предсказание')
    tip = types.KeyboardButton('Поддержать создателя')
    markup2.add(back,tip)
    if call.data == 'pisces':
        bot.send_message(call.message.chat.id, f'Вот сегоднящний гороскоп для Рыб:{piscestoday.getText()}', reply_markup=markup2)
    elif call.data == 'aquarius':
        bot.send_message(call.message.chat.id, f'Вот сегоднящний гороскоп для Водолеев:{aquariustoday.getText()}', reply_markup=markup2)
    elif call.data == 'capricorn':
        bot.send_message(call.message.chat.id, f'Вот сегоднящний гороскоп для Козерогов:{capricorntoday.getText()}', reply_markup=markup2)
    elif call.data == 'sagittarius':
        bot.send_message(call.message.chat.id, f'Вот сегоднящний гороскоп для Стрельцов:{sagittariustoday.getText()}', reply_markup=markup2)
    elif call.data == 'scorpio':
        bot.send_message(call.message.chat.id, f'Вот сегоднящний гороскоп для Скорпионов:{scorpiotoday.getText()}', reply_markup=markup2)
    elif call.data == 'libra':
        bot.send_message(call.message.chat.id, f'Вот сегоднящний гороскоп для Весов:{libratoday.getText()}', reply_markup=markup2)
    elif call.data == 'virgo':
        bot.send_message(call.message.chat.id, f'Вот сегоднящний гороскоп для Дев:{virgotoday.getText()}', reply_markup=markup2)
    elif call.data == 'leo':
        bot.send_message(call.message.chat.id, f'Вот сегоднящний гороскоп для Львов:{leotoday.getText()}', reply_markup=markup2)
    elif call.data == 'cancer':
        bot.send_message(call.message.chat.id, f'Вот сегоднящний гороскоп для Раков:{cancertoday.getText()}', reply_markup=markup2)
    elif call.data == 'gemini':
        bot.send_message(call.message.chat.id, f'Вот сегоднящний гороскоп для Близнецов:{geminitoday.getText()}', reply_markup=markup2)
    elif call.data == 'taurus':
        bot.send_message(call.message.chat.id, f'Вот сегоднящний гороскоп для Тельцов:{taurustoday.getText()}', reply_markup=markup2)
    elif call.data == 'aries':
        bot.send_message(call.message.chat.id, f'Вот сегоднящний гороскоп для Овнов:{ariestoday.getText()}', reply_markup=markup2)
@bot.message_handler()
def text(message):
    if message.text == 'Поддержать создателя':
        bot.send_message(message.chat.id, 'https://www.buymeacoffee.com//wolfhoundt6')
    elif message.text == 'Посмотреть предсказание':
        start(message)

bot.polling(none_stop=True)