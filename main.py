import time
import requests


def get_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT"
    response = requests.get(url)
    return float(response.json()["price"])


def checking_price_droping(price, highest_price):
    if price / highest_price < 0.99:
        print("The price dropped")


highest_price = 0
while True:
    price = get_price()
    if price > highest_price:
        highest_price = price
    checking_price_droping(price, highest_price)
    time.sleep(5)
