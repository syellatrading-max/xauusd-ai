import requests
from config import TWELVE_API_KEY, SYMBOL, INTERVAL

def get_price():
    url = (
        f"https://api.twelvedata.com/time_series"
        f"?symbol={SYMBOL}"
        f"&interval={INTERVAL}"
        f"&outputsize=1"
        f"&apikey={TWELVE_API_KEY}"
    )

    response = requests.get(url)
    data = response.json()

    if "values" not in data:
        return None

    candle = data["values"][0]

    return {
        "open": float(candle["open"]),
        "high": float(candle["high"]),
        "low": float(candle["low"]),
        "close": float(candle["close"])
    }
