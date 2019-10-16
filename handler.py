import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler

# Стартовое окно с клавиатурой
def welc_user(bot,update):
    text = 'Welcome'
    logging.info(text)
    cook_key = ReplyKeyboardMarkup([['Получить случайный рецепт','Добавить свой рецепт'],
                                    ['Избранное', 'Справка']])
    update.message.reply_text(text,reply_markup = cook_key)

# Функция для Handler получить случайный рецепт
def get_recipe(bot,update):
    text_rec = 'РЕЦЕПТ'
    update.message.reply_text(text_rec)

# Функция для Handler справка
def send_help(bot,update):
    text_help = ("""Получить рецепт - для получения случайного рецепта 
Добавить свой рецепт - для добавления нового
Избранное - для проверки своих избранных""")
    update.message.reply_text(text_help)

# Функция для Handler избранное
def get_favorite(bot,update):
    text_fav = 'Избранное'
    update.message.reply_text(text_fav)

# Функции ConversationHandler для добавление своего рецепта
def own_recipe_add (bot,update):
    update.message.reply_text("Введите название блюда: "
    ,reply_markup=ReplyKeyboardRemove())
    return 'ingredient'   


def own_recipe_get_ingr(bot, update, comment):
    
    update.message.reply_text(
            """Добавьте ингридиенты для вашего блюда либо 
               /end чтобы завершить введение""")
    return('formula')

def own_recipe_full(bot, update):
    update.message.reply_text('весь рецепт')
    return ConversationHandler.END

def own_recipe_skip(bot,update):
    text_skip = 'конец ввода'
    update.message.reply_text(text_skip)
    return ConversationHandler.END   