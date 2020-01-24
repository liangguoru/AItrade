# -*- coding: utf-8 -*-

import re
import json
import urllib.request

def fetch_fx_rate():
	url = "http://webforex.hermes.hexun.com/forex/quotelist?code=FOREXUSDCNY&column=Code,Price"
	req = urllib.request.Request(url)
	f = urllib.request.urlopen(req)
	html = f.read().decode("utf-8")
	s = re.findall("{.*}",str(html))[0]
	sjson = json.loads(s)
	USDCNY = sjson["Data"][0][0][1]/10000
	print(USDCNY)

if __name__ == '__main__':
	fetch_fx_rat:()
