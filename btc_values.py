import time
import requests
import pyttsx3
from keys import give_alpha_key
import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt

engine = sqlalchemy.create_engine('sqlite:///BTCGBPstream.db')


def create_frame(json):
    df = pd.DataFrame([json])
    market = json['1. From_Currency Code'] + json['3. To_Currency Code']
    df = df.loc[:, ['1. From_Currency Code', '6. Last Refreshed', '5. Exchange Rate']]
    df.columns = ['Symbol', 'Time', 'Price']
    df.Price = df.Price.astype(float)
    return df


def btc_value(api_key):
    btc_url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=GBP" \
              "&apikey=" + api_key
    btc_response = requests.get(btc_url)
    JSON = btc_response.json()
    return JSON['Realtime Currency Exchange Rate']


def eth_value(api_key):
    return


def xrp_value(api_key):
    return


def ltc_value(api_key):
    return


def get_alpha_values():
    api_key = give_alpha_key()
    while True:
        count = 0
        while count < 3:
            btc_json = btc_value(api_key)
            btc_df = create_frame(btc_json)
            btc_df.to_sql('BTCGBP', engine, if_exists='append', index=False)
            print('Data Frame: ', btc_df)
            count += 1
            time.sleep(180)
        count = 0

        df = pd.read_sql('BTCGBP', engine)
        df.Price.plot()
        plt.show()

if __name__ == '__main__':
    get_alpha_values()
    # print(engine)
    ## json = {'1. From_Currency Code': 'BTC', '3. To_Currency Code': 'GBP', '6. Last Refreshed': '2021-11-19 16:02:03', '5. Exchange Rate': '43075.99730620'}
    ## print(json)
    # print(create_frame(json))