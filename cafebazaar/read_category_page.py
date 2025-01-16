import requests


headers = {
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json',
    'origin': 'https://cafebazaar.ir'
}
def read_category_page(category_type: str):
    url = "https://api.cafebazaar.ir/rest-v1/process/GetPageBodyRequest"
    payload = {
        "properties": {
            "language": 2,
            "clientID": "xrq9ozqybuasdf5l9pmaxdsmk29c58yn",
            "deviceID": "xrq9ozqybuasdf5l9pmaxdsmk29c58yn",
            "clientVersion": "web"
        },
        "singleRequest": {
            "getPageBodyRequest": {"path": category_type, "offset": 24}
        }
    }
    response = requests.post(url, json=payload, headers=headers).json()
    rows = response['singleReply']['getPageBodyReply']['pageBody']['rows']
    package_name_list = []
    more_item_path_list = []

    for row in rows:
        # if row['simpleAppList'] != None:
        if 'simpleAppList' in row:
            row_expandInfo = row['simpleAppList']['expandInfo']
            is_have_more_item = row_expandInfo['show']
            if is_have_more_item:
                more_item_path_list.append(
                    row_expandInfo['vitrinExpandInfo']['path'])
            else:
                apps = row['simpleAppList']['apps']
                for app in apps:
                    package_name_list.append(app['info']['packageName'])
    return package_name_list, more_item_path_list
