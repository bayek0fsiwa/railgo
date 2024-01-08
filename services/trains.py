import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_train_list():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"}
    response = requests.get(os.getenv("TRAINS_URL"), headers=headers)
    return response.json()
