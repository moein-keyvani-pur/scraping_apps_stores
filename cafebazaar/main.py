import requests
import json

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
            "getPageBodyRequest": {"path": category_type, "offset": 0}
        }
    }
    response = requests.post(url, json=payload, headers=headers).json()
    rows = response['singleReply']['getPageBodyReply']['pageBody']['rows']
    package_name_list = []
    more_item_path_list = []
    for row in rows:
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


def read_more_item_page(more_item_path: str):
    url = "https://api.cafebazaar.ir/rest-v1/process/GetPageBodyRequest"
    package_name_list = []
    payload = {
        "properties": {
            "language": 2,
            "clientID": "xrq9ozqybuasdf5l9pmaxdsmk29c58yn",
            "deviceID": "xrq9ozqybuasdf5l9pmaxdsmk29c58yn",
            "clientVersion": "web"
        },
        "singleRequest": {
            "getPageBodyRequest": {"path": more_item_path, "offset": 0}
        }
    }
    response = requests.post(url, json=payload, headers=headers).json()
    rows = response['singleReply']['getPageBodyReply']['pageBody']['rows']
    while len(rows > 0):
        for row in rows:
            packageName = row['simpleAppItem']['info']['packageName']
            package_name_list.append(packageName)
        payload['singleRequest']['getPageBodyRequest']['offset'] += 24
        response = requests.post(url, json=payload, headers=headers).json()
        rows = response['singleReply']['getPageBodyReply']['pageBody']['rows']
    return package_name_list


def get_detail_app(package_name: str):
    url = "https://api.cafebazaar.ir/rest-v1/process/appDetailsV2Request"
    payload = {
        "properties": {
            "language": 2,
            "clientID": "xrq9ozqybughjk5l9pmaxdsmk29c58yn",
            "deviceID": "xrq9ozqybughjk5l9pmaxdsmk29c58yn",
            "clientVersion": "web"
        },
        "singleRequest": {"appDetailsV2Request": {"packageName": package_name}}
    }
    response = requests.post(url, json=payload, headers=headers).json()
    meta = response['singleReply']['appDetailsV2Reply']['meta']
    media=response['singleReply']['appDetailsV2Reply']['media']
    package=response['singleReply']['appDetailsV2Reply']['package']
    data={
        "name": meta['name'],
        "email":meta['email'],
        "phoneNumber":meta['phoneNumber'],
        "homepageUrl": meta['homepageUrl'],
        "shortDescription":meta['shortDescription'],
        "app_constuctor":meta['author']['name'],
        "rate":meta['reviewInfo']['averageRate'],
        "category":meta['category']['name'],
        "type":meta['editorChoice']['title'],
        "count_download":meta['installCount']['range'],
        "price":meta['payment']['price'],
        "priceString":meta['payment']['priceString'],
        "volume":f"{package['verboseSize']} {package['verboseSizeLabel']}",
        "size":package['size'],
        "version":package['versionName'],
        "last_update":package['lastUpdated'],
        "count_viewer":meta['reviewInfo']['verboseReviewCount'],
        "img":media['iconUrl'],
        "pagckage_name":package['name']
    }
    return data



if __name__ == "__main__":
    list_app_category = []
    with open("cafebazaar/utils/app_category.txt", "r")as file:
        for line in file:
            list_app_category.append(line.strip())
    package_name_list = []
    more_item_path_list = []
    for category in list_app_category:
        package_names, more_items_pathes = read_category_page(category)
        package_name_list.append(package_names)
        more_item_path_list.append(more_items_pathes)
        break
    package_flat_list = [item for sublist in package_name_list for item in sublist]
    print(len(package_flat_list))

    # for more_item_path in more_item_path_list:
    #     package_name_list.append(read_more_item_page(more_item_path))   
        
    # package_flat_list = [item for sublist in package_name_list for item in sublist]
    # package_flat_list=['com.farsitel.bazaar']
    # for package_name in package_flat_list:
    #     data=get_detail_app(package_name)
    #     print(data)
    #     break