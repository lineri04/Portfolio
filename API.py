import requests
import json

class StockAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.example.com'  # Ersätt med den faktiska API-basadressen

    def get_stock_price(self, symbol):
        endpoint = f'{self.base_url}/stocks/{symbol}/price'  # Ersätt med den faktiska slutpunkten för att få aktiekurs
        params = {'api_key': self.api_key}

        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            data = response.json()
            return data['price']
        except requests.exceptions.RequestException as e:
            print('Error:', e)
            return None

    def get_stock_info(self, symbol):
        endpoint = f'{self.base_url}/stocks/{symbol}'  # Ersätt med den faktiska slutpunkten för att få aktie infrormation
        params = {'api_key': self.api_key}

        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print('Error:', e)
            return None

# Exempel användning:
api_key = 'your_api_key'
stock_api = StockAPI(api_key)
stock_symbol = 'AAPL'

stock_price = stock_api.get_stock_price(stock_symbol)
print(f'The current price of {stock_symbol} is: {stock_price}')

stock_info = stock_api.get_stock_info(stock_symbol)
print(f'Additional information for {stock_symbol}:')
print(json.dumps(stock_info, indent=4))
