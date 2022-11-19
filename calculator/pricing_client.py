import requests as requests

from models.pricing import PriceResponse

URL = 'https://www.bizportal.co.il/forex/quote/ajaxrequests/'


class PricingClient:
    def get_price(self, symbol: str) -> float:
        path = f'paperdatagraphjson?period=yearly&paperID={symbol}'
        response = self._request(path)
        prices = PriceResponse.from_dict(response)
        return prices.points[0].price

    def _request(self, path, params=None):
        headers = {
            'authority': 'www.bizportal.co.il',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.bizportal.co.il',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.bizportal.co.il/forex/quote/',
        }
        response = requests.get(URL + path, params=params, headers=headers)
        if response.status_code != 200:
            raise Exception("Failed to fetch data from API")
        return response.json()
