import telebot
import config
from telebot import types
import gspread
from datetime import date

credentials = config.creds
googlesheet_id = config.google_name
gc = gspread.service_account_from_dict(credentials) 
bot = telebot.TeleBot(config.TOKEN)


user_dict = {}
class User:
    def __init__(self, qt):
        self.qt = qt


@bot.message_handler(commands=['start'])
def welcome(message):
    stic = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, stic)
 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Стикеры")
    item2 = types.KeyboardButton("Упаковки 5 шт")
    item3 = types.KeyboardButton("Штучные")
    item4 = types.KeyboardButton("Упаковки 25 шт")
    item5 = types.KeyboardButton("Упаковки 15 шт")
    markup.add(item1, item2, item3, item4, item5)
 
    bot.send_message(message.chat.id, "{0.first_name}, привет! Выбери в меню ниже, что ты сегодня сделала".format(message.from_user),
        parse_mode='html', reply_markup=markup)


# 25
@bot.message_handler(regexp="Упаковки 25 шт")
def handle_message(message):
    if message.chat.type == 'private':
        msg = bot.send_message(message.chat.id, 'Сколько их сделано?') 
        bot.register_next_step_handler(msg, process_quantaty_25)
        
def process_quantaty_25(message):
    if message.chat.type == 'private':
        
        chat_id = message.chat.id
        qt = message.text
        if not qt.isdigit():
            msg = bot.reply_to(message, 'Неправильно, введи на обычной клавиатуре количество сделанных упаковок по 25 шт цифрами')
            bot.register_next_step_handler(msg, process_quantaty_25)
            return
        user = User(qt)
        user_dict[chat_id] = user
        
        girl = message.from_user.first_name
        today = date.today().strftime("%d.%m.%Y")
        sh = gc.open_by_key(googlesheet_id)
        sh.sheet1.append_row([today, girl, 'Упаковки 25 шт', int(qt)])
        
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Да", callback_data='yes')
        item2 = types.InlineKeyboardButton("Нет, это всё", callback_data='no')
        markup.add(item1, item2)
            
        bot.send_message(chat_id, 'Что нибудь еще?', reply_markup=markup) 


# 15        
@bot.message_handler(regexp="Упаковки 15 шт")
def handle_message(message):
    if message.chat.type == 'private':
        msg = bot.send_message(message.chat.id, 'Сколько их сделано?') 
        bot.register_next_step_handler(msg, process_quantaty_15)
        
def process_quantaty_15(message):
    if message.chat.type == 'private':
        
        chat_id = message.chat.id
        qt = message.text
        if not qt.isdigit():
            msg = bot.reply_to(message, 'Неправильно, введи на обычной клавиатуре количество сделанных упаковок по 25 шт цифрами')
            bot.register_next_step_handler(msg, process_quantaty_15)
            return
        user = User(qt)
        user_dict[chat_id] = user
        
        girl = message.from_user.first_name
        today = date.today().strftime("%d.%m.%Y")
        sh = gc.open_by_key(googlesheet_id)
        sh.sheet1.append_row([today, girl, 'Упаковки 15 шт', int(qt)])
        
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Да", callback_data='yes')
        item2 = types.InlineKeyboardButton("Нет, это всё", callback_data='no')
        markup.add(item1, item2)
            
        bot.send_message(chat_id, 'Что нибудь еще?', reply_markup=markup) 

        
# 5
@bot.message_handler(regexp="Упаковки 5 шт")
def handle_message(message):
    if message.chat.type == 'private':
        msg = bot.send_message(message.chat.id, 'Сколько их собрано?') 
        bot.register_next_step_handler(msg, process_quantaty_5)
        
def process_quantaty_5(message):
    if message.chat.type == 'private':
        
        chat_id = message.chat.id
        qt = message.text
        if not qt.isdigit():
            msg = bot.reply_to(message, 'Неправильно, введи на обычной клавиатуре количество сделанных упаковок по 5 шт цифрами')
            bot.register_next_step_handler(msg, process_quantaty_5)
            return
        user = User(qt)
        user_dict[chat_id] = user
        
        girl = message.from_user.first_name
        today = date.today().strftime("%d.%m.%Y")
        sh = gc.open_by_key(googlesheet_id)
        sh.sheet1.append_row([today, girl, 'Упаковки 5 шт', int(qt)])
        
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Да", callback_data='yes')
        item2 = types.InlineKeyboardButton("Нет, это всё", callback_data='no')
        markup.add(item1, item2)
            
        bot.send_message(chat_id, 'Что нибудь еще?', reply_markup=markup)


# Стикеры
@bot.message_handler(regexp="Стикеры")
def handle_message(message):
    if message.chat.type == 'private':
        msg = bot.send_message(message.chat.id, 'Сколько их проклеено?') 
        bot.register_next_step_handler(msg, process_quantaty_stikers)
        
def process_quantaty_stikers(message):
    if message.chat.type == 'private':
        
        chat_id = message.chat.id
        qt = message.text
        if not qt.isdigit():
            msg = bot.reply_to(message, 'Неправильно, введи на обычной клавиатуре количество проклеенных стикеров цифрами')
            bot.register_next_step_handler(msg, process_quantaty_stikers)
            return
        user = User(qt)
        user_dict[chat_id] = user
        
        girl = message.from_user.first_name
        today = date.today().strftime("%d.%m.%Y")
        sh = gc.open_by_key(googlesheet_id)
        sh.sheet1.append_row([today, girl, 'Стикеры', int(qt)])
        
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Да", callback_data='yes')
        item2 = types.InlineKeyboardButton("Нет, это всё", callback_data='no')
        markup.add(item1, item2)
            
        bot.send_message(chat_id, 'Что нибудь еще?', reply_markup=markup)       


# Штучные
@bot.message_handler(regexp="Штучные")
def handle_message(message):
    if message.chat.type == 'private':
        msg = bot.send_message(message.chat.id, 'Сколько конфет отдано?') 
        bot.register_next_step_handler(msg, process_quantaty_items)
        
def process_quantaty_items(message):
    if message.chat.type == 'private':
        
        chat_id = message.chat.id
        qt = message.text
        if not qt.isdigit():
            msg = bot.reply_to(message, 'Неправильно, введи на обычной клавиатуре количество отданных конфет цифрами')
            bot.register_next_step_handler(msg, process_quantaty_items)
            return
        user = User(qt)
        user_dict[chat_id] = user
        
        girl = message.from_user.first_name
        today = date.today().strftime("%d.%m.%Y")
        sh = gc.open_by_key(googlesheet_id)
        sh.sheet1.append_row([today, girl, 'Штучные', int(qt)])
        
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Да", callback_data='yes')
        item2 = types.InlineKeyboardButton("Нет, это всё", callback_data='no') 
        markup.add(item1, item2)
            
        bot.send_message(chat_id, 'Что нибудь еще?', reply_markup=markup)


# inline
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'yes':
                
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Стикеры")
                item2 = types.KeyboardButton("Упаковки 5 шт")
                item3 = types.KeyboardButton("Штучные")
                item4 = types.KeyboardButton("Упаковки 25 шт")
                item5 = types.KeyboardButton("Упаковки 15 шт")
                markup.add(item1, item2, item3, item4, item5)                
                
                bot.send_message(call.message.chat.id, 'Снова выбери это в меню снизу', reply_markup=markup)
                
            elif call.data == 'no':
                stic = open('static/bye.webp', 'rb')
                bot.send_sticker(call.message.chat.id, stic)
                bot.send_message(call.message.chat.id, 'Спасибо за работу! Чтобы отправить результаты завтра, нажми /start')
 
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Супер!",
                reply_markup=None)
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Отлично!")
 
    except Exception as e:
        print(repr(e))
            
 
bot.polling(none_stop=True)
# bot.infinity_polling()