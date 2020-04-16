import time
import csv
import datetime
import ccxt

bitmex = ccxt.bitmex({
    'apiKey': '3pFJ5lblk8ff8brlz2plOG2o',
    'secret': 'KKFk0a-YvtW8aEcS33HbQlxJ63rHpdA95D7IWNALSOTVraB1',
    'enableRateLimit': True,
})
bitmex.load_markets()

exchange_class = getattr(ccxt, 'binance')
binance = exchange_class(
	{'urls': 
		{'api': 
			{'public': 'https://fapi.binance.com/fapi/v1', 'private': 'https://fapi.binance.com/fapi/v1',
			},
		}
	}
)

binance.enableRateLimit = True
binance.RateLimit = 10000
binance.apiKey = "FRbVseExyAWjQUtYFnS4memLnPCcgNAeRW7HEBrrw9qyIyPUMCTzUKxZKOJIHcfV"
binance.secret = "CbDX3DE5r9ErdLBOphDB4rjCaAaKbUqITbNK05YIitktZ24VfcNrvVRbIgfK6L87"
binance.load_markets()



basis = [] # binance
basis2 = [] # bitmex

def calculate(ticker, time_, xxx):
    time.sleep(5.01)
    if xxx == 0:
        ohlcvs = binance.fetch_ohlcv(ticker, "1m",binance.parse8601(time_))
    else:
        ohlcvs = bitmex.fetch_ohlcv(ticker, "1m",bitmex.parse8601(time_))
    
    for i in range(0,len(ohlcvs)):
        if xxx == 0:
            basis.append(ohlcvs[i][0])
            basis.append(ohlcvs[i][4])
        else:
            basis2.append(ohlcvs[i][0])
            basis2.append(ohlcvs[i][4])

    timestamp = ohlcvs[-1][0]
    datetimeobj = str(datetime.datetime.fromtimestamp(timestamp/1000))
    nexttime = datetimeobj[0:10] + 'T' + datetimeobj[11:19]
    try:
        time.sleep(5.01)
        calculate(ticker, nexttime, xxx)
    except:
        print(" ")

#start = '2019-12-13T17:45:00'
start = '2020-01-10T00:00:00'
#start = '2020-03-15T00:00:00'
#start = '2020-04-15T00:00:00'

a = start[0:10]+" " + start[11:19]
convert_date = str((datetime.datetime.strptime(a, "%Y-%m-%d %H:%M:%S")).timestamp())
now =str(datetime.datetime.now().timestamp())
now_ = str(datetime.datetime.now() + datetime.timedelta(hours = 9))
remaining =str(int((float(now) - float(convert_date))/72000))
print("현재시간" +"["+now_[11:16]+"]")
print("소요시간 최소" + remaining + "분")


calculate('BTC/USDT',start, 0)

calculate('BTC/USD',start, 1)

print(len(basis))
print(len(basis2))


f = open('binance.csv','w',encoding="euc-kr",newline='')

wr = csv.writer(f)

try:
    i = 0
    while(len(basis2)):
        if i ==0:
            wr.writerow(["Time", "binance"])
        wr.writerow([basis[i], basis[i+1]])
        i = i+2
except:
	print("프로그램 실행 완료")
f.close()





f = open('bitmex.csv','w',encoding="euc-kr",newline='')

wr = csv.writer(f)

try:
    i = 0
    while(len(basis2)):
        if i ==0:
            wr.writerow(["Time", "bitmex"])
        wr.writerow([basis2[i], basis2[i+1]])
        i = i+2
except:
	print("프로그램 실행 완료")
f.close()



#str((datetime.datetime.strptime(basis[i], "%Y-%m-%d %H:%M:%S")).timestamp())



