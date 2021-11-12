import time
import pyttsx3
import requests
from keys import give_alpha_key

engine = pyttsx3.init()

eurusd_history = []
gbpusd_history = []
usdjpy_history = []
eurgbp_history = []
usdnok_history = []


def eurusd_calculations(value, eurusd_counter, eurusd_change):
    if len(eurusd_history) < 10:
        eurusd_history.append(value)
    else:
        if eurusd_counter == 5:
            eurusd_counter = 0
            eurusd_range = value - eurusd_history.pop()
            eurusd_history.insert(0, value)
            print("EUR/USD Range:", eurusd_range)
            if eurusd_range > 5:
                if eurusd_change == 'n' or eurusd_change == 'l':
                    eurusd_change = 'a'
                    engine.say("Euro to US Dollar Appreciating Fast")
                    engine.runAndWait()
            elif eurusd_range < -5:
                if eurusd_change == 'n' or eurusd_change == 'h':
                    eurusd_change = 'l'
                    engine.say("Euro to US Dollar Depreciating Fast")
                    engine.runAndWait()
            else:
                eurusd_change = 'n'
        else:
            eurusd_counter += 1
    return eurusd_counter, eurusd_change


def eurusd_rsi(time_range, eurusd_value, key, eurusd_counter, eurusd_change):
    eurusd_url = "https://www.alphavantage.co/query?function=RSI&symbol=EURUSD&interval=" + time_range \
                 + "&time_period=100&series_type=open&apikey=" + key
    eurusd_response = requests.get(eurusd_url)
    JSON = eurusd_response.json()
    print('EUR/USD:', JSON['value'])
    if JSON['value'] > 70:
        if eurusd_value == 'n' or eurusd_value == 'l':
            eurusd_value = 'h'
            engine.say("Sell Euro to US Dollar")
            engine.runAndWait()
    elif JSON['value'] < 30:
        if eurusd_value == 'n' or eurusd_value == 'h':
            eurusd_value = 'l'
            engine.say("Buy Euro to US Dollar")
            engine.runAndWait()
    else:
        eurusd_value = 'n'
    eurusd_counter, eurusd_change = eurusd_calculations(JSON['value'], eurusd_counter, eurusd_change)
    return eurusd_value, eurusd_counter, eurusd_change


def get_rsi():
    time_range = '5min'
    eurusd_value = 'n'
    eth_value = 'n'
    xrp_value = 'n'
    ltc_value = 'n'
    eurusd_counter = 5
    eth_counter = 5
    xrp_counter = 5
    ltc_counter = 5
    eurusd_change = 'n'
    eth_change = 'n'
    xrp_change = 'n'
    ltc_change = 'n'
    api_key = give_alpha_key()
    while True:
        eurusd_value, eurusd_counter, eurusd_change = eurusd_rsi(time_range, eurusd_value, api_key, eurusd_counter, eurusd_change)
        break
        time.sleep(15)
        #eth_value, eth_counter, eth_change = eth_rsi(time_range, eth_value, api_key, eth_counter, eth_change)
        #time.sleep(15)
        #xrp_value, xrp_counter, xrp_change = xrp_rsi(time_range, xrp_value, api_key, xrp_counter, xrp_change)
        #time.sleep(15)
        #ltc_value, ltc_counter, ltc_change = ltc_rsi(time_range, ltc_value, api_key, ltc_counter, ltc_change)
        print("")
        time.sleep(15)
