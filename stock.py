# -*- coding:utf-8 -*-
 
import tushare as ts
import os
import threading
import time
from FxFetcher import *

def make_stock_list():
	result = []
	with open('config.ini','r') as fd:
		for line in fd.readlines():
			result.append(str(line).replace('\n','').replace('\r',''))
	return result

def get(stocklist):
    i = os.system("clear")                                          # 清屏操作
    print ("===1=====================")
    fetch_fx_rate()
    print ("========================")
    df = ts.get_realtime_quotes(stocklist)
    for i in range(len(stocklist)):
        #print(df['code'][i] + "  " + df['name'][i] + "  " + str(df['price'][i])  + str(round((float(df['price'][i]) - float(df['pre_close'][i])) / float(df['pre_close'][i]) * 100, 2)) + "%" + "  ")
        print(df['code'][i] + "  "  + str(df['price'][i]) + "  " + str(round((float(df['price'][i]) - float(df['pre_close'][i])) / float(df['pre_close'][i]) * 100, 2)) + "%" + "  ")

    global timer
    timer = threading.Timer(10.0, get, [stocklist])
    timer.start()
 
if __name__ == "__main__":
	resultlist = make_stock_list()
	timer = threading.Timer(10.0, get, [resultlist])
	timer.start()
