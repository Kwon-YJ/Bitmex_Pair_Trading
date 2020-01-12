import ccxt
import datetime
import time

bitmex = ccxt.bitmex()
#markets = bitmex.fetch_tickers()

basis = []


epoch = 0
def counter():
	global epoch
	print(epoch)
	epoch =+ 1

def calculate(ticker1, ticker2, time_):

	counter()	
	
	time.sleep(5)

	ticker1_ohlcvs = bitmex.fetch_ohlcv(ticker1, "1m",bitmex.parse8601(time_))
	ticker2_ohlcvs = bitmex.fetch_ohlcv(ticker2, "1m", bitmex.parse8601(time_))
	for i in range(0,len(ticker1_ohlcvs)):
		#basis.apeend(str(datetime.datetime.fromtimestamp(ticker1_ohlcvs[i][0]))
		basis.append(ticker2_ohlcvs[i][4]/ticker1_ohlcvs[i][4])
		
	timestamp = ticker2_ohlcvs[-1][0]
	datetimeobj = str(datetime.datetime.fromtimestamp(timestamp/1000))
	nexttime = datetimeobj[0:10] + 'T' + datetimeobj[11:19]
	try:
		calculate(ticker1, ticker2, nexttime)
	except:
		print(basis)

start = '2019-12-13T17:45:00'

a = start[0:10]+" " + start[11:19]

convert_date = str((datetime.datetime.strptime(a, "%Y-%m-%d %H:%M:%S")).timestamp())

now =str(datetime.datetime.now().timestamp())
print(now)
print(convert_date)



b = (float(now) - float(convert_date))/60
print(b)
#calculate('BTC/USD', 'XBTM20', start)


#f = open('result.csv','w',encoding="euc-kr",newline='')

#wr = csv.writer(f)

#try:
#	i = 0
#	while(len(basis)):
#		if i ==0:
#			wr.writerow(["time", "basis"])
#		wr.writerow([basis[i], basis[i+1])
#		i = i+2
#except:
#	print("프로그램 실행 완료")
#f.close()





