import pandas as pd
import sqlalchemy
from binance.client import Client
from binance import BinanceSocketManager
from keys import give_binance_key

key, secret = give_binance_key()
client = Client()