import json
import requests


#parameters = {
#    "ids": "bitcoin",
#    "vs_currencies": "usd"
#}
def price_calc(ids: str, vs_currencies: str)
    parameters = { 'ids': ids,
                   'vs_currencies': vs_currencies
                 }
    response = requests.get("https://api.coingecko.com/api/v3/simple/price", params=parameters)
    raw_data = json.loads(response)
    return raw_data["price"]

print(price_calc('bitcoin', 'usd')
