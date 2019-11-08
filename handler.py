import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from db_class import * 
from telegram import InlineKeyboardButton, InlineKeyboardMarkup




cs_db = DB()
cs_db.create_db()

# Стартовое окно с клавиатурой
def welc_user(bot,update):
    text = 'Давай начнём! Выбери один из вариантов'
    logging.info(text)
    cook_key = ReplyKeyboardMarkup([['Получить случайный рецепт','Добавить свой рецепт'],
                                    ['Найти рецепт по названию','Найти рецепт по ингредиентам'],
                                    ['Подписаться','Избранное']])
    update.message.reply_text(text,reply_markup = cook_key,resize_keyboard=True)

# Функция для Handler получить случайный рецепт
def get_recipe(bot,update):
    res = cs_db.get_random_recepie()
    text_rec = f'Название: {res[0]} \nКатегория:{res[1]} \nИнгридиенты: {res[2]} \nРецепт: {res[3]}'
    inlinekeyboard = [[InlineKeyboardButton("Добавить в избранное", callback_data='1')]]
    reply_markup = InlineKeyboardMarkup(inlinekeyboard)
    text_rec = f'Название: {res[0].capitalize()} \nКатегория: {res[1]} \nИнгридиенты: {res[2]} \nРецепт: {res[3]}'                    
    update.message.reply_text(text_rec,reply_markup=reply_markup,resize_keyboard=True)

# Функция для Handler справка
def subscribe(bot,update):
    user_info = update.message.from_user
    id = int(user_info['id'])
    try:
        cs_db.client_subscription(id,user_info['username'])
        update.message.reply_text('Вы подписались!')
    except:
        update.message.reply_text('Уже подписаны!')
    print (user_info['id'],user_info['username'])
       
    

def send_help(bot,update):
    update.message.reply_text(f' Здравствуйте! Я бот призванный помочь вам \n в приготовлении различных блюд \n /recipe для получения случайного блюда \n /subscribe для регистрации \n /search_by_name для поиска рецепта по имени \n /add_recipe для добавления своего рецепта \n /info для получения справки')
                     
# Функция для Handler избранное
def get_favorite(bot,update):
    cook_key = ReplyKeyboardMarkup([['Получить случайный рецепт','Добавить свой рецепт'],
                                    ['Найти рецепт по названию','Найти рецепт по ингредиентам'],
                                    ['Подписаться','Избранное']])
    user_info = update.message.from_user
    client_name = user_info['username']
    ans = cs_db.get_favourites(client_name)
    text_rec = []
    for i in ans:        
        text_rec.append(f'Название: {i[0].capitalize()} \nКатегория: {i[1]} \nИнгридиенты: {i[2]} \nРецепт: {i[3]}')
    if text_rec:    
        text_rec = '\n\n'.join(text_rec)
        update.message.reply_text(text_rec,reply_markup = cook_key)
    else:
        update.message.reply_text('К сожалению список пуст, /recipe для вывода случайного')
        update.message.reply_text(reply_markup = cook_key)
    

# Функции ConversationHandler для добавление своего рецепта
def own_recipe_add (bot,update):
    update.message.reply_text("Введите название блюда: "
    ,reply_markup=ReplyKeyboardRemove())
    return 'ingredient'   


def own_recipe_get_ingr(bot, update):
    update.message.reply_text("Добавьте ингридиенты для вашего блюда через запятую "
               ,reply_markup=ReplyKeyboardRemove())
    return 'formula'

def own_recipe_full(bot, update):
    update.message.reply_text('Введите рецепт приготовления ',reply_markup=ReplyKeyboardRemove())
    return 'end'

def own_recipe_skip(bot,update):
    cook_key = ReplyKeyboardMarkup([['Получить случайный рецепт','Добавить свой рецепт'],
                                    ['Найти рецепт по названию','Найти рецепт по ингредиентам'],
                                    ['Подписаться','Избранное']])
    text_skip = 'Рецепт Добавлен!'
    update.message.reply_text(text_skip,reply_markup = cook_key) 
    return ConversationHandler.END 

def unknown(bot,update):
    update.message.reply_text('Введите заново')


# Функция поиска рецепта по названию
def get_rec_by_name(bot,update):
    update.message.reply_text("Введите название блюда: "
    ,reply_markup=ReplyKeyboardRemove())
    return ('name')    

def recipe_get_name(bot,update):
    cook_key = ReplyKeyboardMarkup([['Получить случайный рецепт','Добавить свой рецепт'],
                                    ['Найти рецепт по названию','Найти рецепт по ингредиентам'],
                                    ['Подписаться','Избранное']])
    name = update.message.text    
    ans = cs_db.get_recepie_by_name(name)
    text_rec = []
    for i in ans:        
        text_rec.append(f'Название: {i[0].capitalize()} \nКатегория: {i[1]} \nИнгридиенты: {i[2]} \nРецепт: {i[3]}')
    if text_rec:    
        text_rec = '\n\n'.join(text_rec)
        update.message.reply_text(text_rec,reply_markup = cook_key)
    else:
        update.message.reply_text('К сожалению такого рецепта нету, /recipe для вывода случайного',reply_markup = cook_key)
    return ConversationHandler.END

# Функция поиска рецепта по ингредиентам
def get_rec_by_ingr(bot,update):
    cook_key = ReplyKeyboardMarkup([['Получить случайный рецепт','Добавить свой рецепт'],
                                    ['Найти рецепт по названию','Найти рецепт по ингредиентам'],
                                    ['Подписаться','Избранное']])
    ingredients = update.message.text
    res = cs_db.get_recepie_by_ingredients(ingredients)
    text_rec = []
    for i in res:        
        text_rec.append(f'Название: {i[0].capitalize()} \nКатегория: {i[1]} \nРецепт: {i[2]} \nИнгредиенты: {i[3]} ')
    if text_rec:    
        text_rec = '\n\n'.join(text_rec)
        update.message.reply_text(text_rec,reply_markup = cook_key)
    else:
        update.message.reply_text('К сожалению такого рецепта нету, /recipe для вывода случайного',reply_markup = cook_key)
    update.message.reply_text(text_rec,reply_markup = cook_key)

def get_ingr (bot,update):
    update.message.reply_text("Введите ингредиенты: "
    ,reply_markup=ReplyKeyboardRemove())
    return 'ingredient'

def add_fav(bot,update):
    query = update.callback_query
    data = int(query.message.chat.id)
    name = ((((query.message.text).split('\n')[0]).split(': ')[1]).lower()).strip()
    cs_db.add_to_favourites(data, name)
    text = "Рецепт добавлен, /favorite для просмотра избранных"
    bot.edit_message_text(text=text, chat_id=query.message.chat.id,
            message_id=query.message.message_id)
    print(data, name)
    


