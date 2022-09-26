import json

import requests

BASE = "http://127.0.0.1:5000/"

res_ac = requests.get(f"{BASE}accounts")

# res_cred = requests.get(f"{BASE}credentials")

print(res_ac.text)

# for i in res_cred.json().get("data"):
#     print(i)

