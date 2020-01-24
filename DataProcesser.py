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
			result_list = rs.get_row_data()
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


	#---------------------------------
	#功能：统计每日滚动数据中，最优指标的几只
	#使用方法：输入每个指标抽取个数,以及分析日期，返回字典类型，每个成员是一个列表
	#---------------------------------
	def find_good_target_daily(self,number = 5,query_day = "2020-01-23"):
		# result_list = {'peTTM':[],'psTTM':[],'pcfNcfTTM':[],'pbMRQ':[]}
		result_list = []
		with open('stock_list.txt','r') as fd:
			i = 0
			for line in fd.readlines():
				# print (line)
				result = self.query_day_standard(stocknum = line.replace('\n',''), query_day = query_day)
				print (result)
				result_list.append(result)
				i = i + 1
				if i == 100:
					break
		peTTM_list = sorted(result_list, key = lambda result: result[3], reverse = True)[:number - 1]
		pbMRQ_list = sorted(result_list, key = lambda result: result[4], reverse = True)[:number - 1]
		psTTM_list = sorted(result_list, key = lambda result: result[5], reverse = True)[:number - 1]
		pcfNcfTTM_list = sorted(result_list, key = lambda result: result[6], reverse = True)[:number - 1]
		print (peTTM_list)
		print (pbMRQ_list)
		print (psTTM_list)
		print (pcfNcfTTM_list)
		return peTTM_list,pbMRQ_list,psTTM_list,pcfNcfTTM_list

		


if __name__ == '__main__':
	d = DataProcesser()
	result_list = d.find_good_target_daily()
