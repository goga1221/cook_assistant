import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from db_class import * 
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

cs_db = DB()
cs_db.create_db()

# Стартовое окно с клавиатурой
def welc_user(bot,update):
    text = 'Welcome'
    logging.info(text)
    cook_key = ReplyKeyboardMarkup([['Получить случайный рецепт','Добавить свой рецепт'],
                                    ['Найти рецепт по названию','Найти рецепт по ингредиентам'],
                                    ['Избранное', 'Справка']])
    update.message.reply_text(text,reply_markup = cook_key)

# Функция для Handler получить случайный рецепт
def get_recipe(bot,update):
    res = cs_db.get_random_recepie()
    text_rec = f'Название: {res[0]} \nКатегория:{res[1]} \nИнгридиенты: {res[2]} \nРецепт: {res[3]}'    
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

# Функция поиска рецепта по названию
def get_rec_by_name(bot,update):
    update.message.reply_text("Введите название блюда: "
    ,reply_markup=ReplyKeyboardRemove())
    name = update.message.text
    ans = cs_db.get_recepie_by_name(name)
    text_rec = []
    for i in ans:
        text_rec.append(f'Название: {i[0]} \nКатегория:{i[1]} \nИнгридиенты: {i[2]} \nРецепт: {i[3]}')
    text_rec = '\n\n'.join(text_rec)
    update.message.reply_text(text_rec)

#TODO Функция поиска рецепта по ингредиентам
""" def get_rec_by_ingr(bot,update):
    update.message.reply_text("Введите ингридиенты: "
    ,reply_markup=ReplyKeyboardRemove())
    ingredients = update.message.text
    res = cs_db.get_recepie_by_ingredients(ingredients)
    text_rec = f'Название: {res[0]} \nКатегория:{res[1]} \nИнгридиенты: {res[2]} \nРецепт: {res[3]}'
    update.message.reply_text(text_rec) """