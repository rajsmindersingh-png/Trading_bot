import logging

def create_order(client, symbol, side, order_type, quantity, price=None):
    params = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": order_type.upper(),
        "quantity": quantity
    }

    if order_type.upper() == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    logging.info(f"Sending order: {params}")

    response = client.place_order(params)

    logging.info(f"Response: {response}")

    return response
