import os
from dotenv import load_dotenv

load_dotenv()

SCRAPE_DO_API_KEY = os.environ['SCRAPE_DO_API_KEY']
FIREBASE_KEY_PATH = os.environ['FIREBASE_KEY_PATH']
DRIVER_PATH = os.environ['DRIVER_PATH']