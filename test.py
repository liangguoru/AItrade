# -*- coding:utf-8 -*-
 
import tushare as ts
 
df = ts.get_realtime_quotes(['300059', '399006', 'sh'])
 
print(df['code'][2] + "  " + df['name'][2] + "  " + str(round((float(df['price'][2]) - float(df['pre_close'][2])) / float(df['pre_close'][2]) * 100, 2)) + "%" + "  ")
 
print(df['code'][1] + "  " + df['name'][1] + "  " + str(round((float(df['price'][1]) - float(df['pre_close'][1])) / float(df['pre_close'][1]) * 100, 2)) + "%" + "  ")
 
print(df['code'][0] + "  " + df['name'][0] + "  " + str(round((float(df['price'][0]) - float(df['pre_close'][0])) / float(df['pre_close'][0]) * 100, 2)) + "%" + "  ")