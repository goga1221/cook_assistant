import requests
from bs4 import BeautifulSoup




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

def main():
    
    url = 'https://www.russianfood.com/recipes/recipe.php?rid=145626&ref=cro_t_8&token=55456869'
    
    all_ingr = get_all_ingr(get_html(url))
    
    print(all_ingr)

    full_recipe = get_full_recipe(get_html(url))

    print(full_recipe)
  
if __name__ == '__main__':
    main()   