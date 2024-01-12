API_URL = "https://www.vrbo.com/graphql"

API_HEADERS = {
    "authority": "www.vrbo.com",
    "accept": "*/*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,no;q=0.7,de;q=0.6",
    "cache-control": "no-cache",
    "client-info": "shopping-pwa,unknown,unknown",
    "content-type": "application/json",
    "origin": "https://www.vrbo.com",
    "pragma": "no-cache",
    "referer": "https://www.vrbo.com/search?adults=2&amenities=&children=&d1=2023-12-27&d2=2023-12-28&destination=73%20W%20Monroe%20St%2C%20Chicago%2C%20IL%2060603%2C%20USA&endDate=2024-03-05&latLong=&mapBounds=&pwaDialog=&regionId&semdtl=&sort=RECOMMENDED&startDate=2024-03-01&theme=&userIntent=",
    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "x-enable-apq": "true",
    "x-page-id": "page.Hotel-Search,H,20"
}

API_COOKIES = {
    "DUAID": "7f7d057e-416c-88e8-9116-641023b05fa5",
    "HMS": "824ed4ec-8aba-4618-ab87-11b03c17aa5e",
    "MC1": "GUID=7f7d057e416c88e89116641023b05fa5",
    "ak_bmsc": "25ADE56F9FB3B12107F062E897270B55~000000000000000000000000000000~YAAQfl06Fxl4uPOMAQAAoTuh/BZoHIQkNbGA+89n/R9kPejZcuHoaZTngJkwAAABwPsUBpUjH8V287kW4bFW9uHlwMehFz64yVM96M22j2x2PPdBO6bA+WwG+wQ29cqtaLF0Pkom7K2J+7aJNlaSiybxoV6mOUZ0lFzOc0zv4vNd4GIEbLfssi5LR2JyVnFECxsjiUmnDvWS3nIjv5N/jmbd6NjCj2WsKSvR3ydY69iu8c0ieXWhGVg2a2i3sNI+7c/75WIuV8C5wNS/WMPG7TlFtqjczohM6VG2c5jzFMlfufAnt2dwN+SY2OKENdR0+CXIS7djoAH/OxIBdcVUqoj0rlbNoELKn+MVPEyRpeIsUITcJwdK6Hec/w==",
    "bm_sv": "54FB403C75EDD179C87D3616A14BE33E~YAAQfl06F6R7uPOMAQAAtAKi/BYszzTk8xz6eXI4/6gkR1qcaLsn3asS78nD32PIt7IzTzQPaYuiP8q1q1XBvrJ+jQyBJPzkG4GmvacMT1TS0fqXDQKgaI8EAquvFtr+HQ83Exo6YZ+okDAg/1cYXgopzdD3UmlrhcOHFiJDm+NhkaRER+vCg0K2iVVbbGpG5C0inRjYqARocoUdCZtjrgBS5HojSROMjVARmppuKokkf1V1dgxEMet1Iz2LXw==~1",
    "cesc": "%7B%22lpe%22%3A%5B%227ec5f637-9f16-4999-9af3-0b6142c29715%22%2C1705045525076%5D%2C%22marketingClick%22%3A%5B%22false%22%2C1705045525076%5D%2C%22lmc%22%3A%5B%22DIRECT.WEB%22%2C1705045525076%5D%2C%22hitNumber%22%3A%5B%222%22%2C1705045525076%5D%2C%22amc%22%3A%5B%22DIRECT.WEB%22%2C1705045525076%5D%2C%22visitNumber%22%3A%5B%226%22%2C1705045474140%5D%2C%22ape%22%3A%5B%228d0dbd2d-a247-4d2e-a4c4-19ee27f7113b%22%2C1705045525076%5D%2C%22entryPage%22%3A%5B%22page.Hotel-Search%22%2C1705045525076%5D%2C%22cid%22%3A%5B%22Brand.DTI%22%2C1704978816575%5D%7D",
    "hav": "7f7d057e-416c-88e8-9116-641023b05fa5",
    "linfo": "v.4,|0|0|255|1|0||||||||1033|0|0||0|0|0|-1|-1",
    "JSESSIONID": "2DB35F19627A31FF24EC3803FCA8E3C5",
    "ha-device-id": "7f7d057e-416c-88e8-9116-641023b05fa5",
    "has": "279cd444-53cd-63c8-6243-7800b78d9d1c",
    "hav": "7f7d057e-416c-88e8-9116-641023b05fa5"
}

API_SOURCE = "api"
JSON_SOURCE = "json"
RESPONSE_FILE_PATH = "./response.json"
OUTPUT_FILE_NAME = "listings.csv"