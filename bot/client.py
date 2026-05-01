from binance.client import Client

class BinanceClient:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret, testnet=True)

    def place_order(self, params):
        return self.client.futures_create_order(**params)
