import json
import requests


def price_calc(ids: str, vs_currencies: str):
    parameters = { 'ids': ids,
                   'vs_currencies': vs_currencies
                 }
    response = requests.get("https://api.coingecko.com/api/v3/simple/price", params=parameters)
    firstjson = response.json()[ids]
    return firstjson[vs_currencies]

