from market import get_price

def analyze():

    price = get_price()

    if price is None:
        return None

    close = price["close"]
    open_price = price["open"]

    if close > open_price:
        return {
            "signal": "BUY",
            "entry": close,
            "sl": close - 5,
            "tp": close + 10
        }

    elif close < open_price:
        return {
            "signal": "SELL",
            "entry": close,
            "sl": close + 5,
            "tp": close - 10
        }

    return None
