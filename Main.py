import time
import csv
import datetime
import ccxt

#bitmex = ccxt.bitmex()

bitmex = ccxt.bitmex({
    'apiKey': 'CfIk1cU00oyHEF8HTy7njTXm',
    'secret': '2tVApaQnFwe7Bh-A4lZk-tmKQj9ixoYMgZM4Lpjsk1_zGi0Z',
})


if 'test' in bitmex.urls:
    bitmex.urls['api'] = bitmex.urls['test'] # ←----- switch the base URL to testnet
#print(bitmex.fetch_balance())

#start = '2020-01-20T00:00:00'

timestamp = datetime.datetime.now().timestamp()
datetimeobj = str(datetime.datetime.fromtimestamp(timestamp*0.99995))
start = datetimeobj[0:10] + 'T' + datetimeobj[11:19]


#print(start)


XBT_ohlcv = bitmex.fetch_ohlcv('BTC/USD', "1h",bitmex.parse8601(start))




XBT6M_ohlcv = bitmex.fetch_ohlcv('XBTM20', "1h",bitmex.parse8601(start))

#print(XBT_ohlcv)

#print(XBT6M_ohlcv)

#max_data = 1.04521650993862
#min_data = 1.00661278471711

max_data = 1.27373960796277
min_data = 0.953225806451612

#print((float(XBT6M_ohlcv[-1][4]) / float(XBT_ohlcv[-1][4])))

print((((float(XBT6M_ohlcv[-1][4]) / float(XBT_ohlcv[-1][4])) - min_data) / (max_data - min_data)))




