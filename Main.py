import time
import csv
import datetime
import ccxt
from Order import bitmex, buffer_1, buffer_2, min_data, max_data, Entry, Exit

while(True):
    from Order import Contract_num_BTCUSD, Contract_num_XBTM20
    balance = bitmex.fetch_balance()
    if balance['BTC']['free'] < balance['BTC']['total'] * 0.9:
        Exit(buffer_1, buffer_2)
    else:
        if ((bitmex.fetch_order_book('XBTM20')['bids'][0][0] / bitmex.fetch_order_book('BTC/USD')['asks'][0][0]) - min_data) / (max_data-min_data) > 0.94:
            Entry('buy', 'sell', Contract_num_BTCUSD, Contract_num_XBTM20)
        elif ((bitmex.fetch_order_book('XBTM20')['asks'][0][0] / bitmex.fetch_order_book('BTC/USD')['bids'][0][0]) - min_data) / (max_data-min_data) < 0.06:
            Entry('sell', 'buy', Contract_num_BTCUSD, Contract_num_XBTM20)
    time.sleep(2)

