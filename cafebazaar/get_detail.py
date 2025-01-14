import requests
from main import headers

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
        "email": meta['email'],
        "phoneNumber": meta['phoneNumber'],
        "homepageUrl": meta['homepageUrl'],
        "shortDescription": meta['shortDescription'],
        "app_constuctor": meta['author']['name'],
        "rate": meta['reviewInfo']['averageRate'],
        "category": meta['category']['name'],
        "type": meta['editorChoice']['title'],
        "count_download": meta['installCount']['range'],
        "price": meta['payment']['price'],
        "priceString": meta['payment']['priceString'],
        "volume": f"{package['verboseSize']} {package['verboseSizeLabel']}",
        "size": package['size'],
        "version": package['versionName'],
        "last_update": package['lastUpdated'],
        "count_viewer": meta['reviewInfo']['verboseReviewCount'],
        "img": media['iconUrl'],
        "pagckage_name": package['name']
    }
    return data