import json
import csv
import requests
from config import API_URL,API_HEADERS,API_COOKIES, API_SOURCE, JSON_SOURCE, RESPONSE_FILE_PATH, OUTPUT_FILE_NAME

def make_post_request(url, data, headers=None,cookies=None):
    try:
        response = requests.post(url, data=json.dumps(data), headers=headers,cookies=cookies)
        print(response.text)
        return response.json()
    except Exception as e:
        print(f"Error making POST request: {e}")
        return None

def make_api_body(
        address="73 W Monroe St, Chicago, IL 60603, USA", 
        page_size=50
    ):
    data = {
        "variables": {
            "context": {
            "siteId": 9001001,
            "locale": "en_US",
            "eapid": 1,
            "currency": "USD",
            "device": {
                "type": "DESKTOP"
            },
            "identity": {
                "duaid": "65cbd87c-ebb5-ab83-a4c1-812db78bb787",
                "expUserId": "-1",
                "tuid": "-1",
                "authState": "ANONYMOUS"
            },
            "privacyTrackingState": "CAN_TRACK",
            "debugContext": {
                "abacusOverrides": []
            }
            },
            "criteria": {
            "primary": {
                "dateRange": {
                "checkInDate": {
                    "day": 1,
                    "month": 3,
                    "year": 2024
                },
                "checkOutDate": {
                    "day": 5,
                    "month": 3,
                    "year": 2024
                }
                },
                "destination": {
                "regionName": address,
                "regionId": None,
                "coordinates": None,
                "pinnedPropertyId": None,
                "propertyIds": None,
                "mapBounds": None
                },
                "rooms": [
                {
                    "adults": 2,
                    "children": []
                }
                ]
            },
            "secondary": {
                "counts": [
                {
                    "id": "resultsStartingIndex",
                    "value": 150
                },
                {
                    "id": "resultsSize",
                    "value": page_size
                }
                ],
                "booleans": [],
                "selections": [
                {
                    "id": "sort",
                    "value": "RECOMMENDED"
                },
                {
                    "id": "privacyTrackingState",
                    "value": "CAN_TRACK"
                },
                {
                    "id": "useRewards",
                    "value": "SHOP_WITHOUT_POINTS"
                },
                {
                    "id": "searchId",
                    "value": "d1342ebe-2e4c-4c8d-8838-a3967204a6f2"
                }
                ],
                "ranges": []
            }
            },
            "destination": {
            "regionName": None,
            "regionId": None,
            "coordinates": None,
            "pinnedPropertyId": None,
            "propertyIds": None,
            "mapBounds": None
            },
            "shoppingContext": {
            "multiItem": None
            },
            "returnPropertyType": False,
            "includeDynamicMap": True
        },
        "operationName": "LodgingPwaPropertySearch",
        "extensions": {
            "persistedQuery": {
            "sha256Hash": "e4ffcd90dd44f01455f9ddd89228915a177f9ec674f0df0db442ea1b20f551c3",
            "version": 1
            }
        }
    }
    return data

def get_response_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in file '{file_path}': {e}")
        return None
    
def get_listings_data(data):

    listings = data.get('data', {}).get('propertySearch', {}).get('propertySearchListings', [])

    if not listings:
            print("No listings found")
            return None
    
    fieldnames = ['Listing ID', 'Listing Title', 'Nightly Price', 'Listing URL']
    listings_data = [
            {
                'Listing ID': listing.get('id', ''),
                'Listing Title': listing.get('headingSection', {}).get('heading', ''),
                'Nightly Price': listing.get('priceSection', {}).get('priceSummary', {}).get('displayMessages', [{}])[0].get('lineItems', [{}])[0].get('price', {}).get('formatted', ''),
                'Listing URL': listing.get('cardLink', {}).get('resource', {}).get('value', '')
            }
            for listing in listings
        ]
    
    return listings_data,fieldnames

def write_to_csv(data, fieldnames, csv_filename=OUTPUT_FILE_NAME):
    if data:
        try:
            with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                writer.writeheader()

                writer.writerows(data)

            print(f"CSV '{csv_filename}' file successfully generated.")
        except Exception as e:
            print(f"Error writing to CSV: {e}")

def get_listings_and_make_csv(source = API_SOURCE):

    if source == API_SOURCE:
        data = make_api_body()
        response = make_post_request(API_URL,data,API_HEADERS,API_COOKIES)
    elif source == JSON_SOURCE:
        file_path = RESPONSE_FILE_PATH
        response = get_response_from_file(file_path)
    else:
        print("Not Found")

    if response is not None:
        listings_data,field_names = get_listings_data(response)
        write_to_csv(listings_data,field_names)
    else:
        print("Not Found")

if __name__ == "__main__":

    source = JSON_SOURCE
    get_listings_and_make_csv(source)
    