from flask import Blueprint, jsonify, request
from price_point.config import SCRAPE_DO_API_KEY
from price_point.routes.price_scraping.modules.tokopedia import tokopedia

price_scraping = Blueprint(
    name='price_scraping',
    import_name=__name__,
    url_prefix='/priceScraping'
)


@price_scraping.route('/', methods=['POST'])
def get_price():
    url = request.form['url']
    scrape_url = f'http://api.scrape.do?token={SCRAPE_DO_API_KEY}&url={url}'
    data = tokopedia(scrape_url)

    return jsonify(
        {
            'tokopedia': data
        }
    )
