import requests


url = "https://api.cafebazaar.ir/rest-v1/process/GetPageBodyRequest"
headers = {
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json',
    'origin': 'https://cafebazaar.ir'
}
payload = {
    "properties": {
        "language": 2,
        "clientID": "xrq9ozqybuasdf5l9pmaxdsmk29c58yn",
        "deviceID": "xrq9ozqybuasdf5l9pmaxdsmk29c58yn",
        "clientVersion": "web"
    },
    "singleRequest": {
        "getPageBodyRequest": {"path": "list~app~automatic~APP_NEW~weather", "offset": 0}
    }
}
session = requests.Session()
proxy = {
    "http": "http://130.162.180.254:8888",
    "https": "http://130.162.180.254:8888"
}
session.proxies.update(proxy)

try:
    response = session.post(url, json=payload, headers=headers).json()
    print("Public IP Address:", response)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
