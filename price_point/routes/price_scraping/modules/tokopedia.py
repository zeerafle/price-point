import datetime
import os
import pytz

from selenium import webdriver
from selenium.webdriver.common.by import By


def tokopedia(link):
    driver = webdriver.Firefox()
    driver.get(url)
    product_name = driver.find_element(By.TAG_NAME, 'h1').text
    merchant_anchor = driver.find_element(By.CSS_SELECTOR, 'a[data-testid="llbPDPFooterShopName"]')
    merchant_name = merchant_anchor.find_element(By.TAG_NAME, 'h2').text
    price = driver.find_element(By.CSS_SELECTOR, 'p[data-testid="pdpProductPrice"]').text
    price = price[2:].replace('.', '')
    price = int(price)
    last_updated = datetime.datetime.now(pytz.timezone('Asia/Makassar')).strftime('%Y-%m-%dT%H:%M:%S.%f%z')

    return {
        'name': product_name,
        'merchant': merchant_name,
        'price': price,
        'last_updated': last_updated
    }


if __name__ == '__main__':
    from config import SCRAPE_DO_API_KEY, DRIVER_PATH

    os.environ['PATH'] += DRIVER_PATH
    os.environ['MOZ_HEADLESS'] = "1"
    url = 'https://www.tokopedia.com/gojeteindonesia/jete-x-mouse-gaming-msx1-rgb-wired-6-programmable-buttons-original'
    scrape_url = f'http://api.scrape.do?token={SCRAPE_DO_API_KEY}&url={url}'
    print(tokopedia(url))
