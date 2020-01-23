# -*- coding: utf-8 -*-
# @Author: fangbei
# @Date:   2017-08-26

import re
import json
import urllib.request

url = "http://webforex.hermes.hexun.com/forex/quotelist?code=FOREXUSDCNY&column=Code,Price"
req = urllib.request.Request(url)
f = urllib.request.urlopen(req)
html = f.read().decode("utf-8")
print(html)

s = re.findall("{.*}",str(html))[0]
sjson = json.loads(s)

USDCNY = sjson["Data"][0][0][1]/10000
print(USDCNY)