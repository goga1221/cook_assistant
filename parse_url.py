import requests
from bs4 import BeautifulSoup
import pandas as pd


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
    for ingr in ingr_name:
        a = ingr.text
        ingredients.append(a)
    return [s.strip('\n') for s in ingredients]

def get_full_recipe(html):
    soup = BeautifulSoup(html, 'lxml')
    rec_name = soup.find('table', class_='step_images').find_all('tr','p')
    recipe = []
    for rec in rec_name:
        b = rec.text
        recipe.append(b)
    return(recipe)





def main():
    
    url = 'https://www.russianfood.com/recipes/recipe.php?rid=152213'
       
    get_dish_name(get_html(url))

    all_ingr = get_all_ingr(get_html(url))

    ingr_df=pd.DataFrame(all_ingr)
   
    print(ingr_df)

    full_recipe = get_full_recipe(get_html(url))

    rec_df=pd.DataFrame(full_recipe)

    print(rec_df)
  
if __name__ == '__main__':
    main()   