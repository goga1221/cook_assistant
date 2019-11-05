import requests
from db_class import *
from bs4 import BeautifulSoup


cs_db = DB()
cs_db.create_db()

#получение html код страницы переданной в url
def get_html(url):
    resp = requests.get(url)
    return resp.text

def get_dish_name(html):
    soup = BeautifulSoup(html,'lxml')
    print(soup.h1.text)   

def get_all_ingr(html):
    soup = BeautifulSoup(html, 'lxml')
    ingr_name = soup.find('table', class_='ingr').find_all('tr',['ingr_tr_0', 'ingr_tr_1'])
    ingredients = []
    ingredients.append(soup.h1.text)
    for ingr in ingr_name:
        a = ingr.text
        ingredients.append(a)
    
    return [s.strip('\n') for s in ingredients]

def get_full_recipe(html):
    soup = BeautifulSoup(html, 'lxml')
    rec_name = soup.find('table', class_='step_images').find_all('p')
    recipe = []
    for rec in rec_name:
        b = rec.text
        recipe.append(b)
    return [s.strip('\n') for s in recipe]

def insert_recepie(ingr,rec):
    name = ingr.pop(0).lower
    category = 'категория'
    ingredients = ', '.join(ingr)
    recepie = ''
    for i in range(len(rec)):
        recepie = recepie + f'\n{i+1}) ' + rec[i]    
    recepies_list = ([name,category,recepie,ingredients],)
    print(recepies_list)    
    cs_db.insert_many('recepies', recepies_list)

def main():
    for i in range(15000):
        url = f'https://www.russianfood.com/recipes/recipe.php?rid={i+1}&ref=cro_t_8&token=55456869'
        print(url)
        all_ingr = []
        full_recipe = []

        try:
            all_ingr = get_all_ingr(get_html(url))               
            full_recipe = get_full_recipe(get_html(url))
        except AttributeError as err: print(err)

        try:
            name = all_ingr[0]         
            print('Инсертим в таблицу')
            insert_recepie(all_ingr,full_recipe)
        except IndexError as err: print(err)

        cs_db.query(f"SELECT * FROM recepies WHERE name = '{name}'")

if __name__ == '__main__':
    main()   