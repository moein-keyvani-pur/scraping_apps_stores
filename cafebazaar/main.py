from concurrent.futures import ThreadPoolExecutor
import requests
import json
import time
import random
import string
from requests.adapters import HTTPAdapter
from urllib3 import Retry
headers = {
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json',
    'origin': 'https://cafebazaar.ir'
}


def read_more_item_page(more_item_path: str, proxy: str,index: int):
    url = "https://api.cafebazaar.ir/rest-v1/process/GetPageBodyRequest"
    package_name_list = []
    written_more_items=[]
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
    retry_strategy = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504]
    )

    session = requests.Session()
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    new_proxy = {
        "http": proxy,
        "https": proxy
    }
    session.proxies.update(new_proxy)
    for item_path in more_item_path:
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
                time.sleep(1)
            written_more_items.append(item_path)
            print(f"completed reading {item_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
            with open(f"cafebazaar/data/more_item_path_{index}.txt", "a") as file:
                for item in written_more_items:
                    file.write(f"{item}\n")
            break

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
    selected_proxies=["http://128.140.113.110:5678"]
    package_name_list = []
    more_item_path_list = []
    with open("cafebazaar/utils/more_item_path.txt", "r")as file:
        for item in file:
            more_item_path_list.append(item)
    print(len(more_item_path_list))

    slices = []
    slice_size = max(1, len(more_item_path_list) // len(selected_proxies))

    for i in range(0, len(more_item_path_list), slice_size):
        slices.append(more_item_path_list[i:i + slice_size])

    max_workers = min(len(selected_proxies), len(slices))
    print(f"max_workers-->{max_workers}")

    try:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(read_more_item_page, more_item_path=code_slice,
                                       proxy=selected_proxies[i % len(selected_proxies)],index=i) for i, code_slice in enumerate(slices)]
            for future in futures:
                package_name_list.extend(future.result())
    except Exception as e:
        print(f"An error occurred: {e}")

    # write packge_name_list to file
    with open("cafebazaar/utils/initial_package_names.txt", "a") as file:
        for item in package_name_list:
            file.write(f"{item}\n")
