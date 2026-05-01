import typer
import logging
import os
from dotenv import load_dotenv

from bot.client import BinanceClient
from bot.orders import create_order
from bot.validators import validate_order
from bot.logging_config import setup_logging

app = typer.Typer()

@app.command()
def trade(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None
):
    try:
        setup_logging()
        load_dotenv()

        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        validate_order(symbol, side, order_type, quantity, price)

        client = BinanceClient(api_key, api_secret)

        response = create_order(client, symbol, side, order_type, quantity, price)

        print("\n✅ ORDER SUCCESS")
        print("----------------------")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        print(f"Response: {response}")

    except Exception as e:
        logging.error(str(e))
        print("\n❌ ERROR:", str(e))


if __name__ == "__main__":
    app()
