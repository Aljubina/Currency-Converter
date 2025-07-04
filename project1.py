#API : Application programming interface -> call - return some data to our code

import requests

API_KEY = 'fca_live_LArFgX5cm7sB55m5u25BykWDSKWJ6meqLulnXPpk'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY }"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)       #.join() takes all of the elements from currencies list and it combine them together in string . output : "USD, CAD,EUR..."

    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)     #sending request 
        data = response.json()        #JSOn -> return dictionary of data u pass
        return data["Invalid Currency"]
    except Exception as e:
        print(e)
        return None

while True:
    base = input("Enter the base currency (q for quit) : ").upper()

    if base == "Q":
        break


    data = convert_currency(base)
    if not data:
        continue

    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}:{value}")