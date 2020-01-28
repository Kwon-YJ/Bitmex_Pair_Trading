import time
import csv
import datetime
import ccxt


bitmex = ccxt.bitmex({
    'apiKey': 'CfIk1cU00oyHEF8HTy7njTXm',
    'secret': '2tVApaQnFwe7Bh-A4lZk-tmKQj9ixoYMgZM4Lpjsk1_zGi0Z',
})


if 'test' in bitmex.urls:
    bitmex.urls['api'] = bitmex.urls['test'] # ←----- switch the base URL to testnet
print(bitmex.fetch_balance())


bitmex.create_order(symbol='BTC/USD', type='limit', side='buy', amount=70, price=8725.5)



