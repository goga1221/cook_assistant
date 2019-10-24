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
    return [s.strip('\n') for s in ingredients]

def get_dish_name(html):
    soup = BeautifulSoup(html,'lxml')
    print(soup.h1.text)   


def main():
    
    url = 'https://www.russianfood.com/recipes/recipe.php?rid=68264'
       
    get_dish_name(get_html(url))

    all_ingr = get_all_ingr(get_html(url))

    for i in all_ingr:
        print(i)


    


if __name__ == '__main__':
    main()