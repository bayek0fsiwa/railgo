# import requests
# import json
# import os
# from dotenv import load_dotenv

# load_dotenv()

# # url = os.getenv("URL")

# def make_request(pnr):
#     url = f"https://www.trainman.in/services/getPredictPnr?pnr={pnr}&key=012562ae-60a9-4fcd-84d6-f1354ee1ea48&token="
#     response = requests.get(url=url)
#     content = json.loads(json.dumps(response.json()))
#     print(content)

# make_request(2305672003)

import requests

url = "https://www.trainman.in/services/getPredictPnr"

querystring = {
    "pnr": "2305672003",
    "key": "012562ae-60a9-4fcd-84d6-f1354ee1ea48",
    "token": "",
}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"}

response = requests.get(url, params=querystring, headers=headers)

print(response.json())
