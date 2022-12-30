import json
import requests
import asyncio

def mim_calc():
    parameters_mim = { 'module': 'account',
                   'action': 'tokenbalance',
                   'contractaddress': '0x99d8a9c45b2eca8864373a26d1459e3dff1e17f3',
                   'address': '0x5a6A4D54456819380173272A5E8E9B9904BdF41B',
                   'tag': 'latest',
                   'apikey': 'HWN3T1MVI2MEFS7Z4ZFFBZCYZGVK2S7II2'
                 }
    response_mim = requests.get("https://api.etherscan.io/api", params=parameters_mim)
    mimamt = response_mim.json()['result']
    return mimamt

def crv_calc():
    parameters_crv = { 'module': 'account',
                   'action': 'tokenbalance',
                   'contractaddress': '0x6c3F90f043a72FA612cbac8115EE7e52BDe6E490',
                   'address': '0x5a6A4D54456819380173272A5E8E9B9904BdF41B',
                   'tag': 'latest',
                   'apikey': 'HWN3T1MVI2MEFS7Z4ZFFBZCYZGVK2S7II2'
                 }
    response_crv = requests.get("https://api.etherscan.io/api", params=parameters_crv)
    crvamt = response_crv.json()['result']
    return crvamt

def calc():
    return (int(mim_calc())*(10**-18))/(int(crv_calc())*(10**-18))

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    calc()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")