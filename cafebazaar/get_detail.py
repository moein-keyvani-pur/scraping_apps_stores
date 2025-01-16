import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json',
    'origin': 'https://cafebazaar.ir'
}

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
    media = response['singleReply']['appDetailsV2Reply']['media']
    package = response['singleReply']['appDetailsV2Reply']['package']
    data = {
        "name": meta['name'],
        "link": f"https://cafebazaar.ir/app/{package_name}",
        "img": media['iconUrl'],
        "shortDescription": meta['shortDescription'],
        "version": package['versionName'],
        "last_update": package['lastUpdated'],
        "count_download": meta['installCount']['range'],
        "rate": meta['reviewInfo']['averageRate'],
        "count_viewer": meta['reviewInfo']['verboseReviewCount'],
        "volume": f"{package['verboseSize']} {package['verboseSizeLabel']}",
        "type": meta['editorChoice']['title'],
        "category": meta['category']['name'],
        "app_constuctor": meta['author']['name'],
        "price": meta['payment']['price'],
        "priceString": meta['payment']['priceString'],
        "homepageUrl": meta['homepageUrl'],
        "phoneNumber": meta['phoneNumber'],
        "email": meta['email'],
        "size": package['size'],
        "pagckage_name": package['name']
    }
    return data