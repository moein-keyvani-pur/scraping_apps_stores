from concurrent.futures import ThreadPoolExecutor
import requests
import json
import time
import random
import string
from requests.adapters import HTTPAdapter
from urllib3 import Retry
from read_category_page import read_category_page
from get_detail import get_detail_app
headers = {
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json',
    'origin': 'https://cafebazaar.ir'
}


def read_more_item_page(item_path: str):
    url = "https://api.cafebazaar.ir/rest-v1/process/GetPageBodyRequest"
    package_name_list = []
    # written_more_items = []
    length = 7
    payload = {
        "properties": {
            "language": 2,
            "clientID": "",
            "deviceID": "",
            "clientVersion": "web"
        },
        "singleRequest": {
            "getPageBodyRequest": {"path": "", "offset": 0}
        }
    }
    # retry_strategy = Retry(
    #     total=5,
    #     backoff_factor=1,
    #     status_forcelist=[429, 500, 502, 503, 504]
    # )

    session = requests.Session()
    # adapter = HTTPAdapter(max_retries=retry_strategy)
    # session.mount("https://", adapter)
    # new_proxy = {
    #     "http": proxy,
    #     "https": proxy
    # }
    # session.proxies.update(new_proxy)
    try:
        print(f"started reading {item_path}")
        my_strrand = ''.join(random.choices(
            string.ascii_letters + string.digits, k=length))
        payload['properties']['clientID'] = f"xrq9ozqybuasdf5l9{my_strrand}k29c58yn"
        payload['properties']['deviceID'] = f"xrq9ozqybuasdf5l9{my_strrand}k29c58yn"
        payload['singleRequest']['getPageBodyRequest']['path'] = item_path
        offset = 0
        while True:
            payload['singleRequest']['getPageBodyRequest']['offset'] = offset
            response = session.post(url, json=payload, headers=headers).json()
            rows = response['singleReply']['getPageBodyReply']['pageBody']['rows']
            if not rows:
                break
            for row in rows:
                packageName = row['simpleAppItem']['info']['packageName']
                package_name_list.append(packageName)
            offset += 24
            time.sleep(0.5)
    except Exception as e:
        print(f"An error occurred: {e}")
        print(f"error in path {item_path} in offset {offset}")

    finally:
        return package_name_list


def load_proxies_from_file(proxy_file):
    formatted_lines = []
    with open(proxy_file, "r") as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) == 4:
                ip, port, user, password = parts
                formatted_line = f'socks5://{user}:{password}@{ip}:{port}'
                formatted_lines.append(formatted_line)
    return formatted_lines


if __name__ == "__main__":
    # selected_proxies = load_proxies_from_file(
    #     "cafebazaar/utils/working_proxies.txt")
    # selected_proxies = ["http://130.162.180.254:8888", "47.91.104.88:3128"]
    error_app_list = []
    json_app_list = []
    app_package_names = []
    with open("cafebazaar/utils/app_package_names.txt", "r")as file:
        for item in file:
            app_package_names.append(item.strip())

    print(len(app_package_names))

    for app in app_package_names:
        try:
            data = get_detail_app(app)
            json_app_list.append(data)
            time.sleep(0.3)
        except Exception as e:
            error_app_list.append(app)
            continue

    file_path = "cafebazaar/data/cafebazaar_apps.json"
    with open(file_path, "a") as file:
        json.dump(json_app_list, file, indent=4)
        
    erro_app_path = "cafebazaar/data/error_app.txt"
    with open(erro_app_path, "a") as file:
        for item in error_app_list:
            file.write(f"{item}\n")



    error_game_list = []
    json_game_list = []
    game_package_names = []
    with open("cafebazaar/utils/game_package_names.txt", "r")as file:
        for item in file:
            game_package_names.append(item.strip())

    print(len(game_package_names))

    for app in game_package_names:
        try:
            data = get_detail_app(app)
            json_game_list.append(data)
            time.sleep(0.3)
        except Exception as e:
            error_game_list.append(app)
            continue

    file_path = "cafebazaar/data/cafebazaar_games.json"
    with open(file_path, "a") as file:
        json.dump(json_game_list, file, indent=4)
        
    erro_game_path = "cafebazaar/data/error_app.txt"
    with open(erro_game_path, "a") as file:
        for item in error_game_list:
            file.write(f"{item}\n")
            