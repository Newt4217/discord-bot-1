import os
import json
import requests
import asyncio
from dotenv import load_dotenv

load_dotenv()
APIKEY = os.getenv('ETHERSCAN_API')

async def mim_calc():
    parameters_mim = { 'module': 'account',
                   'action': 'tokenbalance',
                   'contractaddress': '0x99d8a9c45b2eca8864373a26d1459e3dff1e17f3',
                   'address': '0x5a6A4D54456819380173272A5E8E9B9904BdF41B',
                   'tag': 'latest',
                   'apikey': APIKEY
                 }
    response_mim = requests.get("https://api.etherscan.io/api", params=parameters_mim)
    mimamt = response_mim.json()['result']
    return mimamt

async def crv_calc():
    parameters_crv = { 'module': 'account',
                   'action': 'tokenbalance',
                   'contractaddress': '0x6c3F90f043a72FA612cbac8115EE7e52BDe6E490',
                   'address': '0x5a6A4D54456819380173272A5E8E9B9904BdF41B',
                   'tag': 'latest',
                   'apikey': APIKEY
                 }
    response_crv = requests.get("https://api.etherscan.io/api", params=parameters_crv)
    crvamt = response_crv.json()['result']
    return crvamt

async def ratio_calc():
    return (int(await mim_calc())*(10**-18))/(int(await crv_calc())*(10**-18))
