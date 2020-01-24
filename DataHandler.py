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
	def query_all_stock_number_with_market(self,query_day = "2020-01-23"):
		raw_data = self.query_all_stock_fullinfo(query_day)
		if len(raw_data) == 0:
			return None
		result = []
		for stock in raw_data:
			result.append(stock[0] )
		return result

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

	#---------------------------------
	#功能：把列表保存为txt
	#使用方法：参数为列表，转换字符串后存盘，没有返回值
	#---------------------------------
	def writelist(self, result_list):
		with open('stock_list.txt','w') as fd:
			for _ in result_list:
				fd.write(str(_) + '\n')

	#---------------------------------
	#功能：保存单个股票某个时间段的数据
	#使用方法：参数传入时间段，股票代码，会在data文件夹里面保存CSV
	#---------------------------------
	def save_single_stock(self, s_day='2017-01-23', e_day='2020-1-23', stock_num="sh.600000"):
		rs = bs.query_history_k_data_plus(stock_num,
			"date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
			start_date='2017-01-23', end_date='2020-1-23',
			frequency="d", adjustflag="2")
		print('query_history_k_data_plus respond error_code:'+rs.error_code)
		print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)
		data_list = []
		while (rs.error_code == '0') & rs.next():
			data_list.append(rs.get_row_data())
		result = pd.DataFrame(data_list, columns=rs.fields)
		result.to_csv("data/history_A_stock_k_data_"+ stock_num +".csv", index=False)
		print (result)

	#---------------------------------
	#功能：获取分类数据原始信息
	#使用方法：直接调用即可
	#---------------------------------
	def save_stock_classify_info(self):
		rs = bs.query_stock_industry()
		print('query_history_k_data_plus respond error_code:'+rs.error_code)
		print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)
		industry_list = []
		while (rs.error_code == '0') & rs.next():
			# 获取一条记录，将记录合并在一起
			industry_list.append(rs.get_row_data())
		i = 0
		with open('stock_list_simple.txt','w') as fd:
			for _ in industry_list:
				fd.write(_[1]+'\n')
				i = i + 1
		print ("Write done!!",i)
		classify_result = self.make_classify_info(industry_list)
		result = pd.DataFrame(industry_list, columns=rs.fields)
		result.to_csv("stock_industry.csv", index=False)
		return classify_result

	#---------------------------------
	#功能：构造分类数据结构
	#使用方法：输入industry_list，产出字典
	#---------------------------------
	def make_classify_info(self, industry_list):
		result = {}
		for data in industry_list:
			if str(data[3]) in result.keys():
				result[str(data[3])].append(data[1])
			else:
				result[str(data[3])] = []
				result[str(data[3])].append(data[1])
				# print ("new" + str(data[3]) + "key = " + data[1])
		return result


if __name__ == '__main__':
	d = DataHandler()
	d.save_stock_classify_info()
	# for stock in result:
	# 	d.save_single_stock(stock_num = stock)
