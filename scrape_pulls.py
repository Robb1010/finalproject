import requests
import json
from time import sleep

url = "https://api.github.com/repos/microsoft/vscode/pulls"
headers = {"Authorization": "Bearer API_KEY"}

text = "123"
count = 1
data = []
while len(text) > 2:

    querystring = {f"page":{count},"per_page":"100"}

    payload = ""
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    text = response.text
    if len(text) > 2:
        data.extend(json.loads(text))
    print(f"Writing page {count}")
    count += 1
    sleep(0.5)

text = "123"
count = 1
while len(text) > 2:
    querystring = {f"page": {count}, "per_page": "100", "state": "closed"}
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    text = response.text
    if len(text) > 2:
        data.extend(json.loads(text))
    print(f"Writing page {count}")
    count += 1
    sleep(0.5)

with open('pulls.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
