import requests

params = { 
    "name": "your name"
}
result = requests.get("http://127.0.0.1:5000", params=params)
print(result.text)