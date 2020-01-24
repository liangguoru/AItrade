# -*- coding: utf-8 -*-

import tushare as ts
import baostock as bs
import pandas as pd


class DataHandler:
	def __init__(self):
		#### 登陆系统 ####
		lg = bs.login()
		# 显示登陆返回信息
		print('login respond error_code:'+lg.error_code)
		print('login respond  error_msg:'+lg.error_msg)

	#---------------------------------
	#功能：获取所有的票子列表
	#使用方法：直接调用返回list对象
	#---------------------------------
	def query_all_stock_fullinfo(self,query_day = "2020-01-23"):
		data_list = []
		rs = bs.query_all_stock(day=query_day)
		print('query_all_stock respond error_code:'+rs.error_code)
		print('query_all_stock respond  error_msg:'+rs.error_msg)
		while (rs.error_code == '0') & rs.next():
			# 获取一条记录，将记录合并在一起
			stock = rs.get_row_data()
			data_list.append(stock)
			# print (type(stock),stock)
		# result = pd.DataFrame(data_list, columns=rs.fields)
		return data_list

	#---------------------------------
	#功能：获取只有代码的列表
	#使用方法：直接调用返回list对象
	#---------------------------------
	def query_all_stock_number(self,query_day = "2020-01-23"):
		raw_data = self.query_all_stock_fullinfo(query_day)
		if len(raw_data) == 0:
			return None
		result = []
		for stock in raw_data:
			result.append(stock[0].replace('sz.','').replace('sh.','') )
		return result

if __name__ == '__main__':
	d = DataHandler()
	d.query_all_stock_number()
