import urllib.parse as urllib

def pars_url(url):

    #url = 'https://www.russianfood.com/recipes/recipe.php?rid=1000'
    url_data = urllib.urlparse(url)
    print(url_data)
    query_data = urllib.parse_qs(url_data.query)
    print(query_data)

url = 'https://www.russianfood.com/recipes/recipe.php?rid=1010'
pars_url(url)
    
    