import datetime
from bs4 import BeautifulSoup
import requests


def tokopedia(link):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'}
    webpage = requests.get(link, headers=headers)
    dom = BeautifulSoup(webpage.content, 'html.parser')
    product_name = dom.find('h1').text
    price = dom.find('p', {'data-testid': 'pdpProductPrice'}).text
    price = price[2:].replace('.', '')
    price = int(price)
    last_updated = datetime.datetime.now()

    return {
        'name': product_name,
        'price': price,
        'last_updated': last_updated
    }


if __name__ == '__main__':
    from price_point.config import SCRAPE_DO_API_KEY

    url = 'https://www.tokopedia.com/gojeteindonesia/jete-x-mouse-gaming-msx1-rgb-wired-6-programmable-buttons-original'
    scrape_url = f'http://api.scrape.do?token={SCRAPE_DO_API_KEY}&url={url}'
    print(tokopedia(scrape_url))
