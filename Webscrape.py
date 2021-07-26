import requests
import bs4
from replit import db

bigboys_URL = 'https://www.bigboys.ph/FUNKO-c16020004'
filbarstore_URL = 'https://shop.filbars.online/collections/funko'

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}


def checkbigboys():

    pops = ''

    page = requests.get(bigboys_URL, headers=headers)

    soup = bs4.BeautifulSoup(page.content, 'html.parser')

    for funko in db['items']:
        for item in soup.find_all('div', attrs={'class':
                                                'grid-product__wrap'}):
            item_name = item.find('div',
                                  attrs={'class': 'grid-product__title-inner'})
            if funko in item_name.text:
                pops = pops + item_name.text.strip()
                price = item.find(
                    'div',
                    attrs={'class': 'grid-product__price-value ec-price-item'})
                pops = pops + ' ' + price.text.strip() + '\n '
    try:
        return (pops)
    except:
        return ('None')


def checkfilbarstore():

    pops = ' '

    page = requests.get(filbarstore_URL, headers=headers)

    soup = bs4.BeautifulSoup(page.content, 'html.parser')

    for funko in db['items']:
        for items in soup.find_all('a', attrs={'class': 'product-card'}):
            item_name = items.find('div',
                                   attrs={'class': 'product-card__name'})
            if funko in item_name.text:
                pops = pops + item_name.text.strip()
                price = items.find('div',
                                   attrs={'class': 'product-card__price'})
                pops = pops + ' ' + price.text.strip() + '\n '
    try:
        return (pops)
    except:
        return ('None')


def update_items(item_to_find):
    if 'items' in db.keys():
        items = db['items']
        items.append(item_to_find)
        db['items'] = items
    else:
        db['items'] = ['Avatar']


def delete_item(index):
    items = db['items']
    if len(items) > index:
        del items[index]
        db['items'] = items


def get_helpmessage():

    help_message = """Commands:
&funkome - start searching for funko pops
&help - list of commands

&new_item -keyword here- to add a new keyword that the bot will use to search
&del_item -keyword here- to delete a keyword that the bot can use to search
&list_items - to show the keywords that the bot will use to search
    """
    return (help_message)
