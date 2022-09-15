import requests

BASE = "http://127.0.0.1:5000/"

res = requests.get(f"{BASE}hello_there")

print(res.json())
