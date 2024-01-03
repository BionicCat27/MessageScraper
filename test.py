import requests

params = { 
    "name": "john smith"
}
result = requests.get("http://127.0.0.1:5000", params=params)
print(result.status_code)
if result.status_code <= 200:
    with open("received_image.png", "wb") as f:
        f.write(result.content)
else:
    print("Bad response, not writing")