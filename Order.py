import time
import csv
import datetime
import ccxt

bitmex = ccxt.bitmex({
    'apiKey': 'JMc535WFmvHM8EOZEILAOQLv',
    'secret': '6gp-75qNx3cjKbTgsOqrCe-hJnau52F143MH5vAY4v1v3XKO',
    'enableRateLimit': True,
})

lev = 10  # leverage
bitmex.private_post_position_leverage({"symbol": "XBTUSD", "leverage": str(lev)})
bitmex.private_post_position_leverage({"symbol": "XBTM20", "leverage": str(lev)})

buffer_1 = [] #BTCUSD
buffer_2 = [] #XBTM20
buffer_3 = [] #big, small

max_data = 1.06556981569043
min_data = 1.00661278471711

Input_money = 0.46 * (bitmex.fetch_balance()['BTC']['free']) 
# 얼마를 사용해서 진입하는가
Contract_num_BTCUSD = int(10 * Input_money * (bitmex.fetch_ticker('BTC/USD')['close']))
Contract_num_XBTM20 = int(10 * Input_money * (bitmex.fetch_ticker('XBTM20')['close']))
# 계약수는 얼마인가

#롱은 asks
#숏은 bids

def Entry(side_1, side_2, unit1, unit2):
    price_1 = 0.0
    price_2 = 0.0
    if side_1 == 'buy':
        price_1 = bitmex.fetch_order_book('BTC/USD')['asks'][0][0]
        price_2 = bitmex.fetch_order_book('XBTM20')['bids'][0][0]
        buffer_3.append('big')
    else:
        price_1 = bitmex.fetch_order_book('BTC/USD')['bids'][0][0]
        price_2 = bitmex.fetch_order_book('XBTM20')['asks'][0][0]
        buffer_3.append('small')
    
    order_1 = bitmex.create_order('BTC/USD', 'limit', side_1 , unit1 , price_1)
    # 무기한 진입
    order_2 = bitmex.create_order('XBTM20', 'limit', side_2 , unit2 , price_2)
    # 6월물 진입
    resp_1 = order_1['info']['orderID']
    resp_2 = order_2['info']['orderID']
    i = 0
    #time.sleep(10)
    #if ((bitmex.fetch_order_status(resp_1, 'BTC/USD) != 'open) and(bitmex.fetch_order_status(resp_2,'XBTM20') != 'open')):
    #   모든 주문 취소, 모든 거래 중단
    #   Entry(side_1, side_2, unit1, unit2) 
    if bitmex.fetch_order_status(resp_1,'BTC/USD') != 'open':
        buffer_1.append(side_1)
        buffer_1.append(order_1['amount'])
    if bitmex.fetch_order_status(resp_2,'XBTM20') != 'open':
        buffer_2.append(side_2)
        buffer_2.append(order_2['amount'])
    # 주문체결 여부 조회 및 버퍼(buffer[]) 입력

def Exit(side_1, side_2):
    price_1 = 0
    price_2 = 0
    if buffer_3[0] == 'big':
        price_1 = bitmex.fetch_order_book('BTC/USD')['bids'][0][0]
        price_2 = bitmex.fetch_order_book('XBTM20')['asks'][0][0]        
    else:
        price_1 = bitmex.fetch_order_book('BTC/USD')['asks'][0][0]
        price_2 = bitmex.fetch_order_book('XBTM20')['bids'][0][0]

    order_1 = bitmex.create_limit_order('BTC/USD',side_1[0], int(side_1[1]), price_1)
    # 무기한 청산
    order_2 = bitmex.create_limit_order('XBTM20',side_2[0], int(side_2[1]), price_2)
    # 6월물 청산
    resp_1 = order_1['info']['orderID']
    resp_2 = order_2['info']['orderID']
    if bitmex.fetch_order_status(resp_1,'BTC/USD') != 'open':
        buffer_1.clear()
        buffer_3.clear()
    if bitmex.fetch_order_status(resp_2,'XBTM20') != 'open':
        buffer_2.clear()
        buffer_3.clear()
