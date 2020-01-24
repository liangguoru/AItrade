# -*- coding:utf-8 -*-
 
import tushare as ts

token = '0e693d9bddaad8bf493fd3f19a04741337bcfc9bd3b686415938f866'
ts.set_token(token)

pro = ts.pro_api()
data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
 
# df = ts.get_realtime_quotes(['300059', '399006', 'sh'])
 
# print(df['code'][2] + "  " + df['name'][2] + "  " + str(round((float(df['price'][2]) - float(df['pre_close'][2])) / float(df['pre_close'][2]) * 100, 2)) + "%" + "  ")
 
# print(df['code'][1] + "  " + df['name'][1] + "  " + str(round((float(df['price'][1]) - float(df['pre_close'][1])) / float(df['pre_close'][1]) * 100, 2)) + "%" + "  ")
 
# print(df['code'][0] + "  " + df['name'][0] + "  " + str(round((float(df['price'][0]) - float(df['pre_close'][0])) / float(df['pre_close'][0]) * 100, 2)) + "%" + "  ")