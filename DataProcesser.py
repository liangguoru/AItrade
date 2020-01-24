# -*- coding: utf-8 -*-

import tushare as ts
import baostock as bs
import pandas as pd


class DataProcesser:
	def __init__(self):
		#### 登陆系统 ####
		lg = bs.login()
		# 显示登陆返回信息
		print('login respond error_code:'+lg.error_code)
		print('login respond  error_msg:'+lg.error_msg)

	#---------------------------------
	#功能：获得股票单日滚动数据（日频）
	#使用方法：需要知道股票代码和查询日期
	#---------------------------------
	def query_day_standard(self,stocknum = "sz.000005",query_day = "2020-01-23"):
		#### 获取沪深A股估值指标(日频)数据 ####
		# peTTM    滚动市盈率
		# psTTM    滚动市销率
		# pcfNcfTTM    滚动市现率
		# pbMRQ    市净率
		rs = bs.query_history_k_data_plus(stocknum,
			"date,code,close,peTTM,pbMRQ,psTTM,pcfNcfTTM",
			start_date=query_day, end_date=query_day, 
			frequency="d", adjustflag="3")
		print('query_history_k_data_plus respond error_code:'+rs.error_code)
		print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)
		result_list = []
		while (rs.error_code == '0') & rs.next():
			# 获取一条记录，将记录合并在一起
			result_list.append(rs.get_row_data())
		# result = pd.DataFrame(result_list, columns=rs.fields)
		return result_list

	#---------------------------------
	#功能：获得股票单日滚动数据（日频）
	#使用方法：需要知道股票代码和查询日期
	#---------------------------------
	def query_period_standard(self,stocknum = "sz.000005",s_day = "2020-01-23",e_day = "2020-01-23"):
		#### 获取沪深A股估值指标(日频)数据 ####
		# peTTM    滚动市盈率
		# psTTM    滚动市销率
		# pcfNcfTTM    滚动市现率
		# pbMRQ    市净率
		rs = bs.query_history_k_data_plus(stocknum,
			"date,code,close,peTTM,pbMRQ,psTTM,pcfNcfTTM",
			start_date=s_day, end_date=e_day, 
			frequency="d", adjustflag="3")
		print('query_history_k_data_plus respond error_code:'+rs.error_code)
		print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)
		result_list = []
		while (rs.error_code == '0') & rs.next():
			# 获取一条记录，将记录合并在一起
			result_list.append(rs.get_row_data())
		# result = pd.DataFrame(result_list, columns=rs.fields)
		return result_list


if __name__ == '__main__':
	d = DataProcesser()
	d.query_day_standard()
