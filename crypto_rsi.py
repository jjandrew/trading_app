import time
import pyttsx3
import requests
from keys import give_taapi_key
from keys import give_alpha_key

engine = pyttsx3.init()

btc_history = []
eth_history = []
xrp_history = []
ltc_history = []


def btc_calculations(value, btc_counter, btc_change):
    if len(btc_history) < 10:
        btc_history.append(value)
    else:
        if btc_counter == 5:
            btc_counter = 0
            btc_range = value - btc_history.pop()
            btc_history.insert(0, value)
            print("BTC Range:", btc_range)
            if btc_range > 5:
                if btc_change == 'n' or btc_change == 'l':
                    btc_change = 'a'
                    engine.say("Bitcoin Appreciating Fast")
                    engine.runAndWait()
            elif btc_range < -5:
                if btc_change == 'n' or btc_change == 'h':
                    btc_change = 'l'
                    engine.say("Bitcoin Depreciating Fast")
                    engine.runAndWait()
            else:
                btc_change = 'n'
        else:
            btc_counter += 1
    return btc_counter, btc_change


def eth_calculations(value, eth_counter, eth_change):
    if len(eth_history) < 10:
        eth_history.append(value)
    else:
        if eth_counter == 5:
            eth_counter = 0
            eth_range = value - eth_history.pop()
            eth_history.insert(0, value)
            print("ETH Range:", eth_range)
            if eth_range > 5:
                if eth_change == 'n' or eth_change == 'l':
                    eth_change = 'a'
                    engine.say("Ethereum Appreciating Fast")
                    engine.runAndWait()
            elif eth_range < -5:
                if eth_change == 'n' or eth_change == 'h':
                    eth_change = 'l'
                    engine.say("Ethereum Depreciating Fast")
                    engine.runAndWait()
            else:
                eth_change = 'n'
        else:
            eth_counter += 1
    return eth_counter, eth_change


def xrp_calculations(value, xrp_counter, xrp_change):
    if len(xrp_history) < 10:
        xrp_history.append(value)
    else:
        if xrp_counter == 5:
            xrp_counter = 0
            xrp_range = value - xrp_history.pop()
            xrp_history.insert(0, value)
            print("XRP Range:", xrp_range)
            if xrp_range > 5:
                if xrp_change == 'n' or xrp_change == 'l':
                    xrp_change = 'a'
                    engine.say("Ripple Appreciating Fast")
                    engine.runAndWait()
            elif xrp_range < -5:
                if xrp_change == 'n' or xrp_change == 'h':
                    xrp_change = 'l'
                    engine.say("Ripple Depreciating Fast")
                    engine.runAndWait()
            else:
                xrp_change = 'n'
        else:
            xrp_counter += 1
    return xrp_counter, xrp_change


def ltc_calculations(value, ltc_counter, ltc_change):
    if len(ltc_history) < 10:
        ltc_history.append(value)
    else:
        if ltc_counter == 5:
            ltc_counter = 0
            ltc_range = value - ltc_history.pop()
            ltc_history.insert(0, value)
            print("LTC Range:", ltc_range)
            if ltc_range > 5:
                if ltc_change == 'n' or ltc_change == 'l':
                    ltc_change = 'a'
                    engine.say("Litecoin Appreciating Fast")
                    engine.runAndWait()
            elif ltc_range < -5:
                if ltc_change == 'n' or ltc_change == 'h':
                    ltc_change = 'l'
                    engine.say("Litecoin Depreciating Fast")
                    engine.runAndWait()
            else:
                ltc_change = 'n'
        else:
            ltc_counter += 1
    return ltc_counter, ltc_change


def btc_rsi(time_range, btc_value, key, btc_counter, btc_change):
    btc_url = "https://api.taapi.io/rsi?secret=" + key + "&exchange=binance&symbol=BTC/USDT&interval=" + time_range
    btc_response = requests.get(btc_url)
    JSON = btc_response.json()
    print('BTC:', JSON['value'])
    if JSON['value'] > 70:
        if btc_value == 'n' or btc_value == 'l':
            btc_value = 'h'
            engine.say("Sell Bitcoin")
            engine.runAndWait()
    elif JSON['value'] < 30:
        if btc_value == 'n' or btc_value == 'h':
            btc_value = 'l'
            engine.say("Buy Bitcoin")
            engine.runAndWait()
    else:
        btc_value = 'n'
    btc_counter, btc_change = btc_calculations(JSON['value'], btc_counter, btc_change)
    return btc_value, btc_counter, btc_change


def eth_rsi(time_range, eth_value, key, eth_counter, eth_change):
    eth_url = "https://api.taapi.io/rsi?secret=" + key + "&exchange=binance&symbol=ETH/USDT&interval=" + time_range
    eth_response = requests.get(eth_url)
    JSON = eth_response.json()
    print('ETH:', JSON['value'])
    if JSON['value'] > 70:
        if eth_value == 'n' or eth_value == 'l':
            eth_value = 'h'
            engine.say("Sell Ethereum")
            engine.runAndWait()
    elif JSON['value'] < 30:
        if eth_value == 'n' or eth_value == 'h':
            eth_value = 'l'
            engine.say("Buy Ethereum")
            engine.runAndWait()
    else:
        eth_value = 'n'
    eth_counter, eth_change = eth_calculations(JSON['value'], eth_counter, eth_change)
    return eth_value, eth_counter, eth_change


def xrp_rsi(time_range, xrp_value, key, xrp_counter, xrp_change):
    xrp_url = "https://api.taapi.io/rsi?secret=" + key + "&exchange=binance&symbol=XRP/USDT&interval=" + time_range
    xrp_response = requests.get(xrp_url)
    JSON = xrp_response.json()
    print('XRP:', JSON['value'])
    if JSON['value'] > 70:
        if xrp_value == 'n' or xrp_value == 'l':
            xrp_value = 'h'
            engine.say("Sell Ripple")
            engine.runAndWait()
    elif JSON['value'] < 30:
        if xrp_value == 'n' or xrp_value == 'l':
            xrp_value = 'h'
            engine.say("Buy Ripple")
            engine.runAndWait()
    else:
        xrp_value = 'n'
    xrp_counter, xrp_change = xrp_calculations(JSON['value'], xrp_counter, xrp_change)
    return xrp_value, xrp_counter, xrp_change


def ltc_rsi(time_range, ltc_value, key, ltc_counter, ltc_change):
    ltc_url = "https://api.taapi.io/rsi?secret=" + key + "&exchange=binance&symbol=LTC/USDT&interval=" + time_range
    ltc_response = requests.get(ltc_url)
    JSON = ltc_response.json()
    print('LTC:', JSON['value'])
    if JSON['value'] > 70:
        if ltc_value == 'n' or ltc_value == 'l':
            ltc_value = 'h'
            engine.say("Sell LiteCoin")
            engine.runAndWait()
    elif JSON['value'] < 30:
        if ltc_value == 'n' or ltc_value == 'h':
            ltc_value = 'l'
            engine.say("Buy LiteCoin")
            engine.runAndWait()
    else:
        ltc_value = 'n'
    ltc_counter, ltc_change = ltc_calculations(JSON['value'], ltc_counter, ltc_change)
    return ltc_value, ltc_counter, ltc_change


def get_taapi_rsi():
    time_range = '4h'
    btc_value = 'n'
    eth_value = 'n'
    xrp_value = 'n'
    ltc_value = 'n'
    btc_counter = 5
    eth_counter = 5
    xrp_counter = 5
    ltc_counter = 5
    btc_change = 'n'
    eth_change = 'n'
    xrp_change = 'n'
    ltc_change = 'n'
    api_key = give_taapi_key()
    while True:
        btc_value, btc_counter, btc_change = btc_rsi(time_range, btc_value, api_key, btc_counter, btc_change)
        time.sleep(15)
        eth_value, eth_counter, eth_change = eth_rsi(time_range, eth_value, api_key, eth_counter, eth_change)
        time.sleep(15)
        xrp_value, xrp_counter, xrp_change = xrp_rsi(time_range, xrp_value, api_key, xrp_counter, xrp_change)
        time.sleep(15)
        ltc_value, ltc_counter, ltc_change = ltc_rsi(time_range, ltc_value, api_key, ltc_counter, ltc_change)
        print("")
        time.sleep(15)






matic_history = []
link_history = []
dot_history = []
ada_history = []


def matic_calculations(value, matic_counter, matic_change):
    if len(matic_history) < 10:
        matic_history.append(value)
    else:
        if matic_counter == 5:
            matic_counter = 0
            matic_range = value - matic_history.pop()
            matic_history.insert(0, value)
            print("MATIC Range:", matic_range)
            if matic_range > 5:
                if matic_change == 'n' or matic_change == 'l':
                    matic_change = 'a'
                    engine.say("Polygon Appreciating Fast")
                    engine.runAndWait()
            elif matic_range < -5:
                if matic_change == 'n' or matic_change == 'h':
                    matic_change = 'l'
                    engine.say("Polygon Depreciating Fast")
                    engine.runAndWait()
            else:
                matic_change = 'n'
        else:
            matic_counter += 1
    return matic_counter, matic_change


def link_calculations(value, link_counter, link_change):
    if len(link_history) < 10:
        link_history.append(value)
    else:
        if link_counter == 5:
            link_counter = 0
            link_range = value - link_history.pop()
            link_history.insert(0, value)
            print("LINK Range:", link_range)
            if link_range > 5:
                if link_change == 'n' or link_change == 'l':
                    link_change = 'a'
                    engine.say("Chainlink Appreciating Fast")
                    engine.runAndWait()
            elif link_range < -5:
                if link_change == 'n' or link_change == 'h':
                    link_change = 'l'
                    engine.say("Chainlink Depreciating Fast")
                    engine.runAndWait()
            else:
                link_change = 'n'
        else:
            link_counter += 1
    return link_counter, link_change


def dot_calculations(value, dot_counter, dot_change):
    if len(dot_history) < 10:
        dot_history.append(value)
    else:
        if dot_counter == 5:
            dot_counter = 0
            dot_range = value - dot_history.pop()
            dot_history.insert(0, value)
            print("DOT Range:", dot_range)
            if dot_range > 5:
                if dot_change == 'n' or dot_change == 'l':
                    dot_change = 'a'
                    engine.say("Polkadot Appreciating Fast")
                    engine.runAndWait()
            elif dot_range < -5:
                if dot_change == 'n' or dot_change == 'h':
                    dot_change = 'l'
                    engine.say("Polkadot Depreciating Fast")
                    engine.runAndWait()
            else:
                dot_change = 'n'
        else:
            dot_counter += 1
    return dot_counter, dot_change


def ada_calculations(value, ada_counter, ada_change):
    if len(ada_history) < 10:
        ada_history.append(value)
    else:
        if ada_counter == 5:
            ada_counter = 0
            ada_range = value - ada_history.pop()
            ada_history.insert(0, value)
            print("ADA Range:", ada_range)
            if ada_range > 5:
                if ada_change == 'n' or ada_change == 'l':
                    ada_change = 'a'
                    engine.say("Cardano Appreciating Fast")
                    engine.runAndWait()
            elif ada_range < -5:
                if ada_change == 'n' or ada_change == 'h':
                    ada_change = 'l'
                    engine.say("Cardano Depreciating Fast")
                    engine.runAndWait()
            else:
                ada_change = 'n'
        else:
            ada_counter += 1
    return ada_counter, ada_change


def matic_rsi(time_range, matic_value, key, matic_counter, matic_change):
    matic_url = "https://api.taapi.io/rsi?secret=" + key + "&exchange=binance&symbol=BTC/USDT&interval=" + time_range
    matic_response = requests.get(matic_url)
    JSON = matic_response.json()
    print('MATIC:', JSON['value'])
    if JSON['value'] > 70:
        if matic_value == 'n' or matic_value == 'l':
            matic_value = 'h'
            engine.say("Sell Polygon")
            engine.runAndWait()
    elif JSON['value'] < 30:
        if matic_value == 'n' or matic_value == 'h':
            matic_value = 'l'
            engine.say("Buy Polygon")
            engine.runAndWait()
    else:
        matic_value = 'n'
    matic_counter, matic_change = matic_calculations(JSON['value'], matic_counter, matic_change)
    return matic_value, matic_counter, matic_change


def link_rsi(time_range, link_value, key, link_counter, link_change):
    link_url = "https://api.taapi.io/rsi?secret=" + key + "&exchange=binance&symbol=ETH/USDT&interval=" + time_range
    link_response = requests.get(link_url)
    JSON = link_response.json()
    print('LINK:', JSON['value'])
    if JSON['value'] > 70:
        if link_value == 'n' or link_value == 'l':
            link_value = 'h'
            engine.say("Sell Chainlink")
            engine.runAndWait()
    elif JSON['value'] < 30:
        if link_value == 'n' or link_value == 'h':
            link_value = 'l'
            engine.say("Buy Chainlink")
            engine.runAndWait()
    else:
        link_value = 'n'
    link_counter, link_change = link_calculations(JSON['value'], link_counter, link_change)
    return link_value, link_counter, link_change


def dot_rsi(time_range, dot_value, key, dot_counter, dot_change):
    dot_url = "https://api.taapi.io/rsi?secret=" + key + "&exchange=binance&symbol=XRP/USDT&interval=" + time_range
    dot_response = requests.get(dot_url)
    JSON = dot_response.json()
    print('DOT:', JSON['value'])
    if JSON['value'] > 70:
        if dot_value == 'n' or dot_value == 'l':
            dot_value = 'h'
            engine.say("Sell Polkadot")
            engine.runAndWait()
    elif JSON['value'] < 30:
        if dot_value == 'n' or dot_value == 'l':
            dot_value = 'h'
            engine.say("Buy Polkadot")
            engine.runAndWait()
    else:
        dot_value = 'n'
    dot_counter, dot_change = dot_calculations(JSON['value'], dot_counter, dot_change)
    return dot_value, dot_counter, dot_change


def ada_rsi(time_range, ada_value, key, ada_counter, ada_change):
    ada_url = "https://api.taapi.io/rsi?secret=" + key + "&exchange=binance&symbol=LTC/USDT&interval=" + time_range
    ada_response = requests.get(ada_url)
    JSON = ada_response.json()
    print('ADA:', JSON['value'])
    if JSON['value'] > 70:
        if ada_value == 'n' or ada_value == 'l':
            ada_value = 'h'
            engine.say("Sell Cardano")
            engine.runAndWait()
    elif JSON['value'] < 30:
        if ada_value == 'n' or ada_value == 'h':
            ada_value = 'l'
            engine.say("Buy Cardano")
            engine.runAndWait()
    else:
        ada_value = 'n'
    ada_counter, ada_change = ada_calculations(JSON['value'], ada_counter, ada_change)
    return ada_value, ada_counter, ada_change


def get_alpha_rsi():
    time_range = '60min'
    matic_value = 'n'
    link_value = 'n'
    dot_value = 'n'
    ada_value = 'n'
    matic_counter = 5
    link_counter = 5
    dot_counter = 5
    ada_counter = 5
    matic_change = 'n'
    link_change = 'n'
    dot_change = 'n'
    ada_change = 'n'
    api_key = give_alpha_key()
    while True:
        matic_value, matic_counter, matic_change = matic_rsi(time_range, matic_value, api_key, matic_counter, matic_change)
        time.sleep(15)
        link_value, link_counter, link_change = link_rsi(time_range, link_value, api_key, link_counter, link_change)
        time.sleep(15)
        dot_value, dot_counter, dot_change = dot_rsi(time_range, dot_value, api_key, dot_counter, dot_change)
        time.sleep(15)
        ada_value, ada_counter, ada_change = ada_rsi(time_range, ada_value, api_key, ada_counter, ada_change)
        print("")
        time.sleep(15)
