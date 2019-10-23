import requests
from bs4 import BeautifulSoup


#получение html код страницы переданной в url
def get_html(url):
    resp = requests.get(url)
    return resp.text


def get_all_ingr(html):
    soup = BeautifulSoup(html, 'lxml')
    rec_name = soup.find('table', class_='ingr').find_all('tr',['ingr_tr_0', 'ingr_tr_1'])
    ingredients = []
    for ingr in rec_name:
        a = ingr.text
        ingredients.append(a)
    return ingredients

def get_dish_name(html):
    soup = BeautifulSoup(html,'lxml')
    dish_name = soup.findAll("h1",class_ = "title ")
    data = dish_name

    return data      


def main():
    
    url = 'https://www.russianfood.com/recipes/recipe.php?rid=68264'
    
    all_ingr = get_all_ingr(get_html(url))

    for i in all_ingr:
        print(i)

    get_dish_name(get_html(url))
    

if __name__ == '__main__':
    main()