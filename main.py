# -*- coding: utf-8 -*-
from DataHandler import DataHandler as DH
from DataProcesser import DataProcesser as DP
import pairtrade

if __name__ == '__main__':
	print ("Start....\n")
	dh = DH()
	dp = DP()
	classify_result = dh.save_stock_classify_info()
	pairtrade.show_single_related_stock("2019-01-23","2020-01-23",str("sz.000050"),classify_result,u"电子")

	# for stock_A in classify_result[u'家用电器']:
	# 	print ("Now checking stock_A changed!!", stock_A)
	# 	for stock_B in classify_result[u'家用电器']:
	# 		if stock_A == stock_B:
	# 			pass
	# 		else:
	# 			result = pairtrade.check_coint("2019-01-23","2020-01-23",str(stock_A),str(stock_B))
	# 			if result[1] <= 0.05:
	# 				print ("checkA = ",stock_A)
	# 				print ("checkB = ",stock_B)
	# 				print (result)




	# for key in classify_result.keys():
	# 	print (key)
	# 	print (classify_result[key])
	# 	for 
