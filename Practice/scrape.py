import requests
from bs4 import BeautifulSoup
'''
def scape_planetdesert(url):
    
    page_html = requests.get(url)
    #print(page_html)
    html_soup = BeautifulSoup(page_html.text, 'html.parser')
    catcus_items = html_soup.find_all('div', class_="grid-product__content")
    cactuslist = []

    for catcus in catcus_items:
        
        title=catcus.find('div', class_="grid-product__title grid-product__title--body").text
        price=catcus.find('div', class_="grid-product__price").text
        cactuslist.append([title,price])
        print(str(title) + str(price))
    return cactuslist



scape_planetdesert("https://planetdesert.com/collections/cactus")
'''
def scape_uniqlo(url):
    page_html = requests.get(url)
    #print(page_html)
    html_soup = BeautifulSoup(page_html.text, 'html.parser')
    clothes_items = html_soup.find_all('div', id_="shop-by-look-page")
    clotheslist = []

    for clothes in clothes_items:
        
        title=clothes.find('a', class_="name-link").text
        price=clothes.find('span', class_="product-sales-price saleprice").text
        clotheslist.append([title,price])
        print(str(title) + str(price))
    return clotheslist

scape_uniqlo("https://www.uniqlo.com/us/en/men/uniqlo-u")
