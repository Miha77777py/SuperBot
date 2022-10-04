import sys
from bs4 import BeautifulSoup as Bs
import requests
import telebot
import datetime
import random
from telebot import types
import webbrowser
import pytz
from googletrans import Translator


bot = telebot.TeleBot('5359712276:AAGHkmxQRVj3i0dcgYlgRSTtdkGAAatrvLs')
timer = 0


@bot.message_handler(commands=['start'])
def Hi(message):
    bot.send_message(message.chat.id, text='Привіт)')
    bot.send_sticker(message.chat.id, sticker=open('photo_2022-08-07_13-52-35.jpg', 'rb'))
    first_func_start(message)


def first_func_start(message):
    markup = types.ReplyKeyboardMarkup()
    btn_weather = types.KeyboardButton('Погода')
    btn_news = types.KeyboardButton('Новини')
    btn_rating = types.KeyboardButton('Курс валюти в Україні')
    BTC = types.KeyboardButton('Курс біткоїна')
    time = types.KeyboardButton('Час')
    date = types.KeyboardButton('Дата')
    jokes = types.KeyboardButton('Жарти')
    close_bot = types.KeyboardButton('Вийти')
    rock_paper_scissors = types.KeyboardButton('Камінь Ножиці Папір')
    change_language = types.KeyboardButton('Змінити мову')
    markup.add(btn_weather, btn_news, btn_rating, BTC, time, date, jokes, rock_paper_scissors, change_language,
               close_bot)
    words_of_bot = bot.send_message(message.chat.id, text='Виберіть команду для роботи зі мною', reply_markup=markup)
    bot.register_next_step_handler(words_of_bot, terminal)


def first_func_start2(message):
    markup = types.ReplyKeyboardMarkup()
    btn_weather = types.KeyboardButton('Погода')
    btn_news = types.KeyboardButton('Новини')
    btn_rating = types.KeyboardButton('Курс валюти в Україні')
    BTC = types.KeyboardButton('Курс біткоїна')
    time = types.KeyboardButton('Час')
    date = types.KeyboardButton('Дата')
    jokes = types.KeyboardButton('Жарти')
    close_bot = types.KeyboardButton('Вийти')
    rock_paper_scissors = types.KeyboardButton('Камінь Ножиці Папір')
    change_language = types.KeyboardButton('Змінити мову')
    markup.add(btn_weather, btn_news, btn_rating, BTC, time, date, jokes, rock_paper_scissors, change_language,
               close_bot)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.id, text='Мова змінена!')
    words_of_bot = bot.send_message(message.chat.id, text='Виберіть команду для роботи зі мною', reply_markup=markup)
    bot.register_next_step_handler(words_of_bot, terminal)


def first_func_start_eng(message):
    markup = types.ReplyKeyboardMarkup()
    btn_weather = types.KeyboardButton('Weather')
    btn_news = types.KeyboardButton('News')
    btn_ = types.KeyboardButton('Exchange rate')
    BTC = types.KeyboardButton('Bitcoin')
    time = types.KeyboardButton('Time')
    date = types.KeyboardButton('Date')
    jokes = types.KeyboardButton('Jokes')
    close_bot = types.KeyboardButton('Quit')
    rock_paper_scissors = types.KeyboardButton('Rock Paper Scissors')
    change_language = types.KeyboardButton('Change language')
    markup.add(btn_weather, btn_news, btn_, BTC, time, date, jokes, rock_paper_scissors, change_language,
               close_bot)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.id, text='Language changed!')
    words_of_bot = bot.send_message(message.chat.id, text='Chose action to work '
                                                          'with me', reply_markup=markup)
    bot.register_next_step_handler(words_of_bot, terminal_eng)


def first_func_start_eng2(message):
    markup = types.ReplyKeyboardMarkup()
    btn_weather = types.KeyboardButton('Weather')
    btn_news = types.KeyboardButton('News')
    btn_ = types.KeyboardButton('Exchange rate')
    BTC = types.KeyboardButton('Bitcoin')
    time = types.KeyboardButton('Time')
    date = types.KeyboardButton('Date')
    jokes = types.KeyboardButton('Jokes')
    close_bot = types.KeyboardButton('Quit')
    rock_paper_scissors = types.KeyboardButton('Rock Paper Scissors')
    change_language = types.KeyboardButton('Change language')
    markup.add(btn_weather, btn_news, btn_, BTC, time, date, jokes, rock_paper_scissors, change_language,
               close_bot)
    words_of_bot = bot.send_message(message.chat.id, text='Chose action to work '
                                                          'with me', reply_markup=markup)
    bot.register_next_step_handler(words_of_bot, terminal_eng)


def terminal(message):
    if message.text == 'Погода':
        which_city(message)
    elif message.text == 'Новини':
        news(message)
    elif message.text == 'Курс валюти в Україні':
        rate(message)
    elif message.text == 'Час':
        time_now(message)
    elif message.text == 'Дата':
        date_now(message)
    elif message.text == 'Жарти':
        jokes_func(message)
    elif message.text == 'Камінь Ножиці Папір':
        rock_paper_scissors_func(message)
    elif message.text == 'Вийти':
        delete = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, text='Допобачення!)', reply_markup=delete)
        bot.stop_polling()
        sys.exit()
    elif message.text == 'Курс біткоїна':
        BTC_func(message)
    elif message.text == 'Змінити мову':
        change_language_func(message)
    else:
        bot.send_message(message.chat.id, text='Я не розумію Вас')
        first_func_start(message)


def terminal_eng(message):
    if message.text == 'Weather':
        which_city_eng(message)
    elif message.text == 'News':
        news_eng(message)
    elif message.text == 'Exchange rate':
        rate_eng(message)
    elif message.text == 'Time':
        time_now_eng(message)
    elif message.text == 'Date':
        date_now_eng(message)
    elif message.text == 'Jokes':
        jokes_func_eng(message)
    elif message.text == 'Rock Paper Scissors':
        game_eng(message)
    elif message.text == 'Quit':
        delete = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, text='Good bye!)', reply_markup=delete)
        bot.stop_polling()
        sys.exit()
    elif message.text == 'Bitcoin':
        BTC_func_eng(message)
    elif message.text == 'Change language':
        change_language_func2(message)
    else:
        bot.send_message(message.chat.id, text='I don`t understand You')
        first_func_start_eng(message)


def change_language_func(message):
    delete = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, text='Oкей)', reply_markup=delete)
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Українська🇺🇦', callback_data='ukrainian')
    button2 = types.InlineKeyboardButton(text='Англійська🇺🇸', callback_data='english')
    markup.add(button1, button2)
    bot.send_message(message.chat.id, text='Виберіть мову',
                     reply_markup=markup)


def change_language_func2(message):
    delete = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, text='Ok)', reply_markup=delete)
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Ukrainian🇺🇦', callback_data='ukrainian')
    button2 = types.InlineKeyboardButton(text='English🇺🇸', callback_data='english')
    markup.add(button1, button2)
    bot.send_message(message.chat.id, text='Choose language',
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'english')
def english(call):
    first_func_start_eng(call.message)


@bot.callback_query_handler(func=lambda call: call.data == 'ukrainian')
def ukrainian(call):
    first_func_start2(call.message)


def BTC_func(message):
    url = 'https://minfin.com.ua/currency/crypto/bitcoin/'
    response = requests.get(url)
    html = Bs(response.content, 'html.parser')
    text = html.select('.sc-18a2k5w-1')[3].text
    bot.send_message(message.chat.id, text=f'1 біткойн - {text.split(".")[0]}')
    first_func_start(message)


def BTC_func_eng(message):
    url = 'https://minfin.com.ua/currency/crypto/bitcoin/'
    response = requests.get(url)
    html = Bs(response.content, 'html.parser')
    text = html.select('.sc-18a2k5w-1')[3].text
    bot.send_message(message.chat.id, text=f'1 BTC - {text.split(".")[0]}')
    first_func_start_eng2(message)


def rock_paper_scissors_func(message):
    delete = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, text='Oкей)', reply_markup=delete)
    buttons = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton('Камінь🪨', callback_data='rock')
    button2 = types.InlineKeyboardButton('Ножиці✂', callback_data='scissors')
    button3 = types.InlineKeyboardButton('Папір📜', callback_data='paper')
    buttons.add(button1, button2, button3)
    bot.send_message(message.chat.id, text='Виберіть свою дію', reply_markup=buttons)


@bot.callback_query_handler(func=lambda call: call.data == 'rock' or call.data == 'scissors' or call.data == 'paper')
def callback(call):
    if call.message:
        if call.data == 'rock':
            bot.answer_callback_query(call.id)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Ви обрали камінь')
            bot.send_sticker(call.message.chat.id, sticker=open('box/stone.jpg', 'rb'))
            variant = 'rock'
            bot_(call, variant)
        elif call.data == 'scissors':
            bot.answer_callback_query(call.id)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Ви обрали ножиці')
            bot.send_sticker(call.message.chat.id, sticker=open('box/scissors.jpg', 'rb'))
            variant = 'scissors'
            bot_(call, variant)
        elif call.data == 'paper':
            bot.answer_callback_query(call.id)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Ви обрали папір')
            bot.send_sticker(call.message.chat.id, sticker=open('box/paper.jpg', 'rb'))
            variant = 'paper'
            bot_(call, variant)


def bot_(call, variant):
    lst = ['box/stone.jpg', 'box/scissors.jpg', 'box/paper.jpg']
    choice = random.choice(lst)
    if choice == 'box/stone.jpg':
        bot.send_message(call.message.chat.id, text='Бот обрав камінь')
        bot.send_sticker(call.message.chat.id, sticker=open(f'{choice}', 'rb'))
        if variant == 'rock':
            bot.send_message(call.message.chat.id, text='Нічія!')
        elif variant == 'scissors':
            bot.send_message(call.message.chat.id, text='Бот виграв!')
        else:
            bot.send_message(call.message.chat.id, text='Ви виграли!')
    elif choice == 'box/scissors.jpg':
        bot.send_message(call.message.chat.id, text='Бот обрав ножиці')
        bot.send_sticker(call.message.chat.id, sticker=open(f'{choice}', 'rb'))
        if variant == 'rock':
            bot.send_message(call.message.chat.id, text='Ви виграли!')
        elif variant == 'scissors':
            bot.send_message(call.message.chat.id, text='Нічія!')
        else:
            bot.send_message(call.message.chat.id, text='Бот виграв!')
    elif choice == 'box/paper.jpg':
        bot.send_message(call.message.chat.id, text='Бот обрав папір')
        bot.send_sticker(call.message.chat.id, sticker=open(f'{choice}', 'rb'))
        if variant == 'rock':
            bot.send_message(call.message.chat.id, text='Бот виграв!')
        elif variant == 'scissors':
            bot.send_message(call.message.chat.id, text='Ви виграли!')
        else:
            bot.send_message(call.message.chat.id, text='Нічія!')
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Зіграти ще раз')
    btn2 = types.KeyboardButton('Вернутися в меню')
    markup.add(btn1, btn2)
    words_of_bot = bot.send_message(call.message.chat.id, text='Що ви хочете зробити? Зіграти зі мною ще раз чи '
                                                               'вернутися в меню?', reply_markup=markup)
    bot.register_next_step_handler(words_of_bot, new_terminal)


def game_eng(message):
    delete = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, text='Ok)', reply_markup=delete)
    buttons = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton('Rock🪨', callback_data='rock_eng')
    button2 = types.InlineKeyboardButton('Scissors✂', callback_data='scissors_eng')
    button3 = types.InlineKeyboardButton('Paper📜', callback_data='paper_eng')
    buttons.add(button1, button2, button3)
    bot.send_message(message.chat.id, text='Choose action)',
                     reply_markup=buttons)


@bot.callback_query_handler(
    func=lambda call: call.data == 'rock_eng' or call.data == 'scissors_eng' or call.data == 'paper_eng'
)
def callback2_eng(call):
    if call.message:
        if call.data == 'rock_eng':
            bot.answer_callback_query(call.id)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='You chose rock')
            bot.send_sticker(call.message.chat.id, sticker=open('box/stone.jpg', 'rb'))
            variant = 'rock'
            bot_eng(call, variant)
        elif call.data == 'scissors_eng':
            bot.answer_callback_query(call.id)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='You chose scissors')
            bot.send_sticker(call.message.chat.id, sticker=open('box/scissors.jpg', 'rb'))
            variant = 'scissors'
            bot_eng(call, variant)
        elif call.data == 'paper_eng':
            bot.answer_callback_query(call.id)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='You chose paper')
            bot.send_sticker(call.message.chat.id, sticker=open('box/paper.jpg', 'rb'))
            variant = 'paper'
            bot_eng(call, variant)


def bot_eng(call, variant):
    lst = ['box/stone.jpg', 'box/scissors.jpg', 'box/paper.jpg']
    choice = random.choice(lst)
    if choice == 'box/stone.jpg':
        bot.send_message(call.message.chat.id, text='Bot chose rock')
        bot.send_sticker(call.message.chat.id, sticker=open(f'{choice}', 'rb'))
        if variant == 'rock':
            bot.send_message(call.message.chat.id, text='Draw!')
        elif variant == 'scissors':
            bot.send_message(call.message.chat.id, text='Bot won!')
        else:
            bot.send_message(call.message.chat.id, text='You won!')
    elif choice == 'box/scissors.jpg':
        bot.send_message(call.message.chat.id, text='Bot chose scissors')
        bot.send_sticker(call.message.chat.id, sticker=open(f'{choice}', 'rb'))
        if variant == 'rock':
            bot.send_message(call.message.chat.id, text='You won!')
        elif variant == 'scissors':
            bot.send_message(call.message.chat.id, text='Draw!')
        else:
            bot.send_message(call.message.chat.id, text='Bot won!')
    elif choice == 'box/paper.jpg':
        bot.send_message(call.message.chat.id, text='Bot chose paper')
        bot.send_sticker(call.message.chat.id, sticker=open(f'{choice}', 'rb'))
        if variant == 'rock':
            bot.send_message(call.message.chat.id, text='Bot won!')
        elif variant == 'scissors':
            bot.send_message(call.message.chat.id, text='You won!')
        else:
            bot.send_message(call.message.chat.id, text='Draw!')
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Play again')
    btn2 = types.KeyboardButton('Return to menu')
    markup.add(btn1, btn2)
    words_of_bot = bot.send_message(call.message.chat.id, text='What do you want to do? Play again or '
                                                               'return to menu?', reply_markup=markup)
    bot.register_next_step_handler(words_of_bot, new_terminal_eng)


def new_terminal(message):
    if message.text == 'Зіграти ще раз':
        rock_paper_scissors_func(message)
    else:
        first_func_start(message)


def new_terminal_eng(message):
    if message.text == 'Play again':
        game_eng(message)
    else:
        first_func_start_eng2(message)


def rate(message):
    delete = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, text='Oкей)', reply_markup=delete)
    url = 'https://minfin.com.ua/ua/currency/'
    response = requests.get(url)
    html = Bs(response.content, 'html.parser')
    text = html.select('.mfm-grey-bg > .table-response > tbody > tr > .mfm-text-nowrap')[0].text
    lst = text.split()
    bot.send_message(message.chat.id, text=f'Доллар:\n'
                                           f'Купівля: {lst[0]} / Продажа:{lst[4]}\n')
    text2 = html.select('.mfm-grey-bg > .table-response > tbody > tr > .mfm-text-nowrap')[2].text
    lst2 = text2.split()
    bot.send_message(message.chat.id, text=f'Євро:\n'
                                           f'Купівля: {lst2[0]} / Продажа:{lst2[4]}\n')

    text3 = html.select('.mfm-grey-bg > .table-response > tbody > tr > .mfm-text-nowrap')[4].text
    lst3 = text3.split()
    bot.send_message(message.chat.id, text=f'Польські Злоті:\n'
                                           f'Купівля: {lst3[0]} / Продажа:{lst3[4]}')
    first_func_start(message)


def rate_eng(message):
    url = 'https://minfin.com.ua/ua/currency/converter/?from=cad&to=usd&val1=1&val2=1.2565947242206235'
    response = requests.get(url)
    html = Bs(response.content, 'html.parser')
    text = html.select('.sc-1xh0v1v-1')
    bot.send_message(message.chat.id, text=f'1 CAD-{text[1].get("value")} USD')

    url = 'https://minfin.com.ua/ua/currency/converter/?from=usd&to=eur&val1=1&val2=1'
    response = requests.get(url)
    html = Bs(response.content, 'html.parser')
    text1 = html.select('.sc-1v7zcr1-10')[3].text
    t = text1.split()
    bot.send_message(message.chat.id, text=f'1 EUR-{t[3]} USD')

    url = 'https://minfin.com.ua/ua/currency/converter/?from=uah&to=usd&val1=1&val2=1'
    response = requests.get(url)
    html = Bs(response.content, 'html.parser')
    text2 = html.select('.sc-1xh0v1v-1')
    bot.send_message(message.chat.id, text=f'1 UAH-{text2[1].get("value")} USD')
    first_func_start_eng2(message)


def news(message):
    delete = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, text='Oкей)', reply_markup=delete)
    buttons = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Веб Сайт', url='https://news.google.com')
    buttons.add(button1)
    bot.send_message(message.chat.id, text='Новини:', reply_markup=buttons)
    first_func_start(message)


def news_eng(message):
    delete = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, text='Ok)', reply_markup=delete)
    buttons = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Web Site', url='https://news.google.com/publications/CAAqBwgKMI7D-wowkqT0Ag?hl=en-GB&gl=GB&ceid=GB%3Aen')
    buttons.add(button1)
    bot.send_message(message.chat.id, text='News:', reply_markup=buttons)
    first_func_start_eng2(message)


def which_city(message):
    delete = types.ReplyKeyboardRemove(selective=False)
    city = bot.send_message(message.chat.id, text='Введіть назву міста:', reply_markup=delete)
    bot.register_next_step_handler(city, weather)


def which_city_eng(message):
    delete = types.ReplyKeyboardRemove(selective=False)
    city = bot.send_message(message.chat.id, text='Enter name of the city:', reply_markup=delete)
    bot.register_next_step_handler(city, weather_eng)


def weather(message):
    weather_func(message, message.text)


def weather_func(message, text):
    global timer
    try:
        delete = types.ReplyKeyboardRemove(selective=False)
        response = requests.get(f'https://ua.sinoptik.ua/погода-{text}')
        html = Bs(response.content, 'html.parser')
        description = html.select('.description')
        lst_images = [i.get('src') for i in html.find_all('img')]
        url_image = f'https:{lst_images[8]}'
        response_image = requests.get(url_image)
        with open('weather.jpg', 'wb') as photo:
            photo.write(response_image.content)
        bot.send_message(message.chat.id, text='Oкей)', reply_markup=delete)
        bot.send_message(message.chat.id, text='Погода:')
        bot.send_photo(message.chat.id, photo=open('weather.jpg', 'rb'))
        for i in html.select('#bd1'):
            min_temp = i.select('.temperature > .min > span')[0].text
            max_temp = i.select('.temperature > .max > span')[0].text
            bot.send_message(message.chat.id, text=f'Мінімальна: {min_temp}\n'
                                                   f'Максимальна: {max_temp}\n'
                                                   f'{description[-2].text}\n'
                                                   f'{description[-1].text}')
        timer = 0
        first_func_start(message)
    except IndexError:
        translator = Translator()
        text2 = translator.translate(text, src="en", dest="uk").text.lower()
        timer += 1
        if timer >= 3:
            bot.send_message(message.chat.id, text='Я не розумію Вас')
            which_city(message)
            timer = 0
        else:
            weather_func(message, text2)


def weather_eng(message):
    weather_eng_func(message, message.text)


def weather_eng_func(message, text):
    global timer
    try:
        delete = types.ReplyKeyboardRemove(selective=False)
        translator = Translator()
        response = requests.get(f'https://ua.sinoptik.ua/погода-{text}')
        html = Bs(response.content, 'html.parser')
        description = html.select('.description')
        lst_images = [i.get('src') for i in html.find_all('img')]
        url_image = f'https:{lst_images[8]}'
        response_image = requests.get(url_image)
        with open('weather_eng.jpg', 'wb') as photo:
            photo.write(response_image.content)
        bot.send_message(message.chat.id, text='Ok)', reply_markup=delete)
        bot.send_message(message.chat.id, text='Weather:')
        bot.send_photo(message.chat.id, photo=open('weather_eng.jpg', 'rb'))
        for i in html.select('#bd1'):
            min_temp = i.select('.temperature > .min > span')[0].text
            max_temp = i.select('.temperature > .max > span')[0].text
            bot.send_message(message.chat.id, text=f'Min: {min_temp}\n'
                                                   f'Max: {max_temp}\n'
                                                   f'{translator.translate(description[-2].text, src="uk", dest="en").text}\n'
                                                   f'{translator.translate(description[-1].text, src="uk", dest="en").text}')
        timer = 0
        first_func_start_eng2(message)
    except IndexError:
        translator = Translator()
        text2 = translator.translate(text, src="en", dest="uk").text.lower()
        timer += 1
        if timer >= 3:
            bot.send_message(message.chat.id, text='I don`t understand You')
            which_city(message)
            timer = 0
        else:
            weather_eng_func(message, text2)


def time_now(message):
    delete = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, text='Oкей)', reply_markup=delete)
    now = datetime.datetime.now()
    bot.send_message(message.chat.id, text='Час:')
    if 0 <= now.minute < 10:
        if 0 <= now.hour < 10:
            bot.send_message(message.chat.id, f'0{now.hour}:0{now.minute}')
        else:
            bot.send_message(message.chat.id, f'{now.hour}:0{now.minute}')
    else:
        if 0 <= now.hour < 10:
            bot.send_message(message.chat.id, f'0{now.hour}:{now.minute}')
        else:
            bot.send_message(message.chat.id, f'{now.hour}:{now.minute}')
    first_func_start(message)


def time_now_eng(message):
    delete = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, text='Ok)', reply_markup=delete)
    p = pytz.timezone('US/Eastern')
    now = datetime.datetime.now(tz=p)
    bot.send_message(message.chat.id, text='Time:')
    if 0 <= now.minute < 10:
        if 0 <= now.hour < 10:
            bot.send_message(message.chat.id, f'0{now.hour}:0{now.minute}')
        else:
            bot.send_message(message.chat.id, f'{now.hour}:0{now.minute}')
    else:
        if 0 <= now.hour < 10:
            bot.send_message(message.chat.id, f'0{now.hour}:{now.minute}')
        else:
            bot.send_message(message.chat.id, f'{now.hour}:{now.minute}')
    first_func_start_eng2(message)


def date_now(message):
    delete = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, text='Oкей)', reply_markup=delete)
    now = datetime.datetime.now()
    bot.send_message(message.chat.id, text='Дата:')
    if 1 <= now.day < 10:
        if 1 <= now.month < 10:
            bot.send_message(message.chat.id, f'0{now.day}.0{now.month}.{now.year}')
        else:
            bot.send_message(message.chat.id, f'0{now.day}.{now.month}.{now.year}')
    else:
        if 1 <= now.month < 10:
            bot.send_message(message.chat.id, f'{now.day}.0{now.month}.{now.year}')
        else:
            bot.send_message(message.chat.id, f'{now.day}.{now.month}.{now.year}')
    date_now_2(message)
    first_func_start(message)


def date_now_2(message):
    now = datetime.datetime.now()
    if now.month == 1:
        bot.send_message(message.chat.id, text=f'{now.day} Січня {now.year}')
    elif now.month == 2:
        bot.send_message(message.chat.id, text=f'{now.day} Лютого {now.year}')
    elif now.month == 3:
        bot.send_message(message.chat.id, text=f'{now.day} Березня {now.year}')
    elif now.month == 4:
        bot.send_message(message.chat.id, text=f'{now.day} Квітня {now.year}')
    elif now.month == 5:
        bot.send_message(message.chat.id, text=f'{now.day} Травня {now.year}')
    elif now.month == 6:
        bot.send_message(message.chat.id, text=f'{now.day} Червня {now.year}')
    elif now.month == 7:
        bot.send_message(message.chat.id, text=f'{now.day} Липня {now.year}')
    elif now.month == 8:
        bot.send_message(message.chat.id, text=f'{now.day} Серпня {now.year}')
    elif now.month == 9:
        bot.send_message(message.chat.id, text=f'{now.day} Вересня {now.year}')
    elif now.month == 10:
        bot.send_message(message.chat.id, text=f'{now.day} Жовтня {now.year}')
    elif now.month == 11:
        bot.send_message(message.chat.id, text=f'{now.day} Листопада {now.year}')
    elif now.month == 12:
        bot.send_message(message.chat.id, text=f'{now.day} Грудня {now.year}')


def date_now_eng(message):
    delete = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, text='Ok)', reply_markup=delete)
    p = pytz.timezone('US/Eastern')
    now = datetime.datetime.now(tz=p)
    bot.send_message(message.chat.id, text='Date:')
    if 1 <= now.day < 10:
        if 1 <= now.month < 10:
            bot.send_message(message.chat.id, f'0{now.day}.0{now.month}.{now.year}')
        else:
            bot.send_message(message.chat.id, f'0{now.day}.{now.month}.{now.year}')
    else:
        if 1 <= now.month < 10:
            bot.send_message(message.chat.id, f'{now.day}.0{now.month}.{now.year}')
        else:
            bot.send_message(message.chat.id, f'{now.day}.{now.month}.{now.year}')
    date_now_2_eng(message)
    first_func_start_eng2(message)


def date_now_2_eng(message):
    now = datetime.datetime.now()
    if now.day == 1:
        if now.month == 1:
            bot.send_message(message.chat.id, text=f'The {now.day}st of January {now.year}')
        elif now.month == 2:
            bot.send_message(message.chat.id, text=f'The {now.day}st of February {now.year}')
        elif now.month == 3:
            bot.send_message(message.chat.id, text=f'The {now.day}st of March {now.year}')
        elif now.month == 4:
            bot.send_message(message.chat.id, text=f'The {now.day}st of April {now.year}')
        elif now.month == 5:
            bot.send_message(message.chat.id, text=f'The {now.day}st of May {now.year}')
        elif now.month == 6:
            bot.send_message(message.chat.id, text=f'The {now.day}st of June {now.year}')
        elif now.month == 7:
            bot.send_message(message.chat.id, text=f'The {now.day}st of July {now.year}')
        elif now.month == 8:
            bot.send_message(message.chat.id, text=f'The {now.day}st of August {now.year}')
        elif now.month == 9:
            bot.send_message(message.chat.id, text=f'The {now.day}st of September {now.year}')
        elif now.month == 10:
            bot.send_message(message.chat.id, text=f'The {now.day}st of October {now.year}')
        elif now.month == 11:
            bot.send_message(message.chat.id, text=f'The {now.day}st of November {now.year}')
        elif now.month == 12:
            bot.send_message(message.chat.id, text=f'The {now.day}st of December {now.year}')
    elif now.day == 2:
        if now.month == 1:
            bot.send_message(message.chat.id, text=f'The {now.day}nd of January {now.year}')
        elif now.month == 2:
            bot.send_message(message.chat.id, text=f'The {now.day}nd of February {now.year}')
        elif now.month == 3:
            bot.send_message(message.chat.id, text=f'The {now.day}nd of March {now.year}')
        elif now.month == 4:
            bot.send_message(message.chat.id, text=f'The {now.day}nd of April {now.year}')
        elif now.month == 5:
            bot.send_message(message.chat.id, text=f'The {now.day}nd of May {now.year}')
        elif now.month == 6:
            bot.send_message(message.chat.id, text=f'The {now.day}nd of June {now.year}')
        elif now.month == 7:
            bot.send_message(message.chat.id, text=f'The {now.day}nd of July {now.year}')
        elif now.month == 8:
            bot.send_message(message.chat.id, text=f'The {now.day}nd of August {now.year}')
        elif now.month == 9:
            bot.send_message(message.chat.id, text=f'The {now.day}nd of September {now.year}')
        elif now.month == 10:
            bot.send_message(message.chat.id, text=f'The {now.day}nd of October {now.year}')
        elif now.month == 11:
            bot.send_message(message.chat.id, text=f'The {now.day}nd of November {now.year}')
        elif now.month == 12:
            bot.send_message(message.chat.id, text=f'The {now.day}nd of December {now.year}')
    elif now.day == 3:
        if now.month == 1:
            bot.send_message(message.chat.id, text=f'The {now.day}rd of January {now.year}')
        elif now.month == 2:
            bot.send_message(message.chat.id, text=f'The {now.day}rd of February {now.year}')
        elif now.month == 3:
            bot.send_message(message.chat.id, text=f'The {now.day}rd of March {now.year}')
        elif now.month == 4:
            bot.send_message(message.chat.id, text=f'The {now.day}rd of April {now.year}')
        elif now.month == 5:
            bot.send_message(message.chat.id, text=f'The {now.day}rd of May {now.year}')
        elif now.month == 6:
            bot.send_message(message.chat.id, text=f'The {now.day}rd of June {now.year}')
        elif now.month == 7:
            bot.send_message(message.chat.id, text=f'The {now.day}rd of July {now.year}')
        elif now.month == 8:
            bot.send_message(message.chat.id, text=f'The {now.day}rd of August {now.year}')
        elif now.month == 9:
            bot.send_message(message.chat.id, text=f'The {now.day}rd of September {now.year}')
        elif now.month == 10:
            bot.send_message(message.chat.id, text=f'The {now.day}rd of October {now.year}')
        elif now.month == 11:
            bot.send_message(message.chat.id, text=f'The {now.day}rd of November {now.year}')
        elif now.month == 12:
            bot.send_message(message.chat.id, text=f'The {now.day}rd of December {now.year}')
    else:
        if now.month == 1:
            bot.send_message(message.chat.id, text=f'The {now.day}th of January {now.year}')
        elif now.month == 2:
            bot.send_message(message.chat.id, text=f'The {now.day}th of February {now.year}')
        elif now.month == 3:
            bot.send_message(message.chat.id, text=f'The {now.day}th of March {now.year}')
        elif now.month == 4:
            bot.send_message(message.chat.id, text=f'The {now.day}th of April {now.year}')
        elif now.month == 5:
            bot.send_message(message.chat.id, text=f'The {now.day}th of May {now.year}')
        elif now.month == 6:
            bot.send_message(message.chat.id, text=f'The {now.day}th of June {now.year}')
        elif now.month == 7:
            bot.send_message(message.chat.id, text=f'The {now.day}th of July {now.year}')
        elif now.month == 8:
            bot.send_message(message.chat.id, text=f'The {now.day}th of August {now.year}')
        elif now.month == 9:
            bot.send_message(message.chat.id, text=f'The {now.day}th of September {now.year}')
        elif now.month == 10:
            bot.send_message(message.chat.id, text=f'The {now.day}th of October {now.year}')
        elif now.month == 11:
            bot.send_message(message.chat.id, text=f'The {now.day}th of November {now.year}')
        elif now.month == 12:
            bot.send_message(message.chat.id, text=f'The {now.day}th of December {now.year}')


def jokes_func(message):
    url = 'https://www.pinterest.com/alinarastorgueva/%D0%BF%D1%80%D0%B8%D0%BA%D0%BE%D0%BB%D0%B8-%D1%83%D0%BA%D1%80%D' \
          '0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D0%BE%D1%8E/'
    response = requests.get(url)
    html = Bs(response.content, 'html.parser')
    lst_image = [i.get('src') for i in html.find_all('img')]
    a = random.randint(1, 25)
    response_image = requests.get(lst_image[a])
    with open('joke.jpg', 'wb') as image:
        image.write(response_image.content)
    bot.send_photo(message.chat.id, photo=open('joke.jpg', 'rb'))
    first_func_start(message)


def jokes_func_eng(message):
    lst = ['I just saw some idiot at the gym… He put a water bottle in the Pringles holder on the treadmill!',
           'Tequila is an excelent teacher… Just last night it taught me to count… One Tequila, Two Tequila, Three Tequila, Floor!',
           '''– Don’t give up on your dreams.
– Really? You mean it?
– Yeah, just keep sleeping.''', 'How does a bunny eat? Very carrotfully!', 'What did the buffalo say when his son left for college? Bison!',
           '''Father: What did you get that big medal for?
Ringo: For stopping.
Father: What did you get that big medal for?
Ringo: For stopping.''',
           '''Reporter: What made you go out on that dangerous pond ice and risk your life to save a friend?
Boy: I had to do it. He had my skates on.''']
    a = random.choice(lst)
    bot.send_message(message.chat.id, text=a)
    first_func_start_eng2(message)


if __name__ == '__main__':
    webbrowser.open('https://t.me/Miha77777SuperBot')
    bot.polling(non_stop=True)
