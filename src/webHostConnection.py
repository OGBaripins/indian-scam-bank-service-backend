import json
from urllib import response
import requests as rq
from datetime import datetime

BASE_URL = "http://pukitis.pythonanywhere.com/"

input = {'input': 'testing'}
response = rq.get(BASE_URL, params=input)

output = response.json()

rq_input = output['input']
timestamp = output['timestamp']
input_length = output['character_count']

print(f"input: {rq_input}")
print(f"date: {timestamp}")
print(f"input length: {input_length}")