from flask import Flask
from flask_cors import CORS

# import blueprint
from .routes.price_scraping.controllers import price_scraping

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return 'PricePoint Backend API Gateway'


# register blueprint
app.register_blueprint(price_scraping)
