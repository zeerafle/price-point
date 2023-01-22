from flask_cors import CORS
from price_point import app

cors = CORS(
    app,
    resource={r'/*': {'origins': '*'}}
)

if __name__ == '__main__':
    app.run()
