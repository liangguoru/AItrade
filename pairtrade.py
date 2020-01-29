# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import coint

def find_date_index(pd,value):
	return pd.date[pd.date == value].index.tolist()[0] 

def plot_data():
# a_price = pd.read_csv('./data/history_A_stock_k_data_sh.600000.csv')[:200]
# b_price = pd.read_csv('./data/history_A_stock_k_data_sh.600004.csv')[:200]


# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot(range(len(a_price)), a_price['close'])
# ax.plot(range(len(b_price)), b_price['close'])
# ax.legend(['a','b'])
# plt.show()
	return

def adf_check():
# a_price = np.reshape(a_price['close'].values, -1)
# a_price_diff = np.diff(a_price)
 
# b_price = np.reshape(b_price['close'].values, -1)
# b_price_diff = np.diff(b_price)

# print(adfuller(a_price_diff))
# print(adfuller(b_price_diff))

# print(coint(a_price, b_price))
	return

def check_coint(s_date,e_date,stock_A,stock_B):
	if (stock_A == None) or (stock_B == None):
		return 0,"stock name error!!"
	if (s_date > e_date):
		return 0,"Time error"
	a_price = pd.read_csv('./data/history_A_stock_k_data_' + str(stock_A) + '.csv')
	b_price = pd.read_csv('./data/history_A_stock_k_data_' + str(stock_B) + '.csv')
	start_day_a = a_price.date[0]
	start_day_b = b_price.date[0]

	s_date = max(start_day_a,start_day_b,s_date)

	end_day_a = a_price.date[a_price.date.shape[0]-1]
	end_day_b = b_price.date[b_price.date.shape[0]-1]

	e_date = min(end_day_a,end_day_b,e_date)

	s_pos_a = find_date_index(a_price,s_date)
	e_pos_a = find_date_index(a_price,e_date)
	s_pos_b = find_date_index(b_price,s_date)
	e_pos_b = find_date_index(b_price,e_date)

	if (e_pos_b - s_pos_b) != (e_pos_a - s_pos_a):
		if (e_pos_b - s_pos_b) > (e_pos_a - s_pos_a):
			e_pos_b = e_pos_a
			s_pos_b = s_pos_a
		else:
			e_pos_a = e_pos_b
			s_pos_a = s_pos_b

	a_price = np.reshape(a_price['close'][s_pos_a:e_pos_a].values,-1)
	b_price = np.reshape(b_price['close'][s_pos_b:e_pos_b].values,-1)
	result = coint(a_price, b_price)
	return result

def show_single_related_stock(s_date,e_date,stock_A,classify_result,collction_tpye):
	maxlen = len(classify_result[collction_tpye])
	i = 0
	for stock_B in classify_result[collction_tpye]:
		if stock_A == stock_B:
			pass
		else:
			result = check_coint("2019-01-23","2020-01-23",str(stock_A),str(stock_B))
			if result[1] <= 0.05:
				print (stock_B,result[1])
				i = i + 1
	print (i,maxlen)
	return

if __name__ == '__main__':
	print ("pair_trade!!\n")
	result = check_coint("2019-01-23","2020-01-23","sh.600060","sz.002959")
	print (result[1],type(result))