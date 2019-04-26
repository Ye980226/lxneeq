import requests
import random
import time
timestamp_pagelet = int(time.time()*1000)
callback = "JQuery" + "181" + \
    str(random.random()).replace(".", "") + "_%d" % timestamp_pagelet
data = {"disclosureType": "5", "page": "0", "companyCd": "430203",
        "startTime":	"2019-03-27", "endTime": "2019-04-26", "keyword": "关键字",
        "xxfcbj": ""}
r = requests.post(
    "http://www.neeq.com.cn/disclosureInfoController/infoResult.do?callback=%s" % callback, data=data)
print(r.text, file=open("soft.html", "w"))
