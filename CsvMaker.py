import time
import csv
import datetime
import ccxt

bitmex = ccxt.bitmex()
#markets = bitmex.fetch_tickers()

basis = []

'''
ticker1_ohlcvs = bitmex.fetch_ohlcv('BTC/USD', "1h",bitmex.parse8601('2019-12-13T17:45:00'))

print(ticker1_ohlcvs)

'''

def calculate(ticker1, ticker2, time_):
    time.sleep(5.01)
    ticker1_ohlcvs = bitmex.fetch_ohlcv(ticker1, "1h",bitmex.parse8601(time_))
    ticker2_ohlcvs = bitmex.fetch_ohlcv(ticker2, "1h", bitmex.parse8601(time_))
    for i in range(0,len(ticker1_ohlcvs)):
        basis.append(str(datetime.datetime.fromtimestamp(ticker1_ohlcvs[i][0]/1000)))
        basis.append(ticker2_ohlcvs[i][1]/ticker1_ohlcvs[i][1])
        basis.append(ticker2_ohlcvs[i][2]/ticker1_ohlcvs[i][2])
        basis.append(ticker2_ohlcvs[i][3]/ticker1_ohlcvs[i][3])
        basis.append(ticker2_ohlcvs[i][4]/ticker1_ohlcvs[i][4])
        timestamp = ticker2_ohlcvs[-1][0]
        datetimeobj = str(datetime.datetime.fromtimestamp(timestamp/1000))
        nexttime = datetimeobj[0:10] + 'T' + datetimeobj[11:19]
    try:
        time.sleep(5.01)
        calculate(ticker1, ticker2, nexttime)
    except:
        print(" ")

start = '2019-12-13T17:45:00'
#start = '2020-01-10T00:00:00'

a = start[0:10]+" " + start[11:19]
convert_date = str((datetime.datetime.strptime(a, "%Y-%m-%d %H:%M:%S")).timestamp())
now =str(datetime.datetime.now().timestamp())
now_ = str(datetime.datetime.now() + datetime.timedelta(hours = 9))
remaining =str(int((float(now) - float(convert_date))/72000))
print("현재시간" +"["+now_[11:16]+"]")
print("소요시간 최소" + remaining + "분")


calculate('BTC/USD', 'XBTM20', start)


f = open('result.csv','w',encoding="euc-kr",newline='')

wr = csv.writer(f)

try:
	i = 0
	while(len(basis)):
		if i ==0:
			wr.writerow(["time", "Open", "High", "low", "Close"])
		wr.writerow([basis[i], basis[i+1], basis[i+2], basis[i+3], basis[i+4]])
		i = i+5
except:
	print("프로그램 실행 완료")
f.close()





