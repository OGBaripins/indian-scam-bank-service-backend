import json

import requests

BASE = "http://127.0.0.1:5000/"

res_ac = requests.get(f"{BASE}accounts")

# res_cred = requests.get(f"{BASE}credentials")


for i in json.loads(res_ac.json()).get("data"):
    print(i)

# print(type(res_cred.json()))
