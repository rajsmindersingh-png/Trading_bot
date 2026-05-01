# Trading Bot (Binance Futures Testnet)

## Setup

pip install -r requirements.txt

Add your API keys in .env file.

## Run

Market Order:
python cli.py trade BTCUSDT BUY MARKET 0.01

Limit Order:
python cli.py trade BTCUSDT BUY LIMIT 0.01 30000
