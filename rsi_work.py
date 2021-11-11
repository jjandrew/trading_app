import time
import pyttsx3
import requests
from keys import give_keys

engine = pyttsx3.init()


def btc_rsi(time_range, btc_value, key):
    btc_url = "https://api.taapi.io/rsi?secret=" + key + "&exchange=binance&symbol=BTC/USDT&interval=" + time_range
    btc_response = requests.get(btc_url)
    JSON = btc_response.json()
    print('BTC:', JSON['value'])
    if JSON['value'] > 55:
        if btc_value == 'n':
            btc_value = 'h'
            engine.say("Sell Bitcoin")
            engine.runAndWait()
    elif JSON['value'] < 35:
        if btc_value == 'n':
            btc_value = 'l'
            engine.say("Buy Bitcoin")
            engine.runAndWait()
    else:
        btc_value = 'n'
    return btc_value


def eth_rsi(time_range, eth_value, key):
    eth_url = "https://api.taapi.io/rsi?secret=" + key + "&exchange=binance&symbol=ETH/USDT&interval=" + time_range
    eth_response = requests.get(eth_url)
    JSON = eth_response.json()
    print('ETH:', JSON['value'])
    if JSON['value'] > 55:
        if eth_value == 'n':
            btc_value = 'h'
            engine.say("Sell Ethereum")
            engine.runAndWait()
    elif JSON['value'] < 35:
        if eth_value == 'n':
            eth_value = 'l'
            engine.say("Buy Ethereum")
            engine.runAndWait()
    else:
        eth_value = 'n'
    return eth_value


def xrp_rsi(time_range, xrp_value, key):
    xrp_url = "https://api.taapi.io/rsi?secret=" + key + "&exchange=binance&symbol=XRP/USDT&interval=" + time_range
    xrp_response = requests.get(xrp_url)
    JSON = xrp_response.json()
    print('XRP:', JSON['value'])
    if JSON['value'] > 55:
        if xrp_value == 'n':
            xrp_value = 'h'
            engine.say("Sell Ripple")
            engine.runAndWait()
    elif JSON['value'] < 35:
        if xrp_value == 'n':
            xrp_value = 'h'
            engine.say("Buy Ripple")
            engine.runAndWait()
    else:
        xrp_value = 'n'
    return xrp_value


def ltc_rsi(time_range, ltc_value, key):
    ltc_url = "https://api.taapi.io/rsi?secret=" + key + "&exchange=binance&symbol=LTC/USDT&interval=" + time_range
    ltc_response = requests.get(ltc_url)
    JSON = ltc_response.json()
    print('LTC:', JSON['value'])
    if JSON['value'] > 55:
        if ltc_value == 'n':
            ltc_value = 'h'
            engine.say("Sell LiteCoin")
            engine.runAndWait()
    elif JSON['value'] < 35:
        if ltc_value == 'n':
            ltc_value = 'l'
            engine.say("Buy LiteCoin")
            engine.runAndWait()
    else:
        ltc_value = 'n'
    return ltc_value


def get_rsi():
    time_range = '4h'
    btc_value = 'n'
    eth_value = 'n'
    xrp_value = 'n'
    ltc_value = 'n'
    api_key = give_keys()
    while True:
        btc_value = btc_rsi(time_range, btc_value, api_key)
        time.sleep(15)
        eth_value = eth_rsi(time_range, eth_value, api_key)
        time.sleep(15)
        xrp_value = xrp_rsi(time_range, xrp_value, api_key)
        time.sleep(15)
        ltc_value = ltc_rsi(time_range, ltc_value, api_key)
        print("")
        time.sleep(15)
