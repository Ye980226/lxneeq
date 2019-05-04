import requests
import random
import time
import os
import json

dirname = os.path.dirname(os.path.abspath(__file__))

os.chdir(dirname)

timestamp_pagelet = int(time.time()*1000)
callback = "JQuery" + "181" + \
    str(random.random()).replace(".", "") + "_%d" % timestamp_pagelet
stock_ids = []
BASE_URL = "http://www.neeq.com.cn"
with open("stock.txt") as f:
    i = 0
    for line in f:
        stock_ids.append((line.split())[0])
        i += 1
        if i > 10:
            break
print(stock_ids)


def download_announcement(companyCd, startTime="2019-03-27", endTime="2019-04-26", output="announcement"):
    """
    docstring here
        :param companyCd: 股票代码
        :param startTime="2019-03-27":开始获取的时间，默认是2019-03-27
        :param endTime="2019-04-26": 结束的时间，默认是2019-04-26
        :param output="announcement":输出的文件夹，默认是announcement
    """
    if not os.path.exists(output):
        os.mkdir(output)

    data = {"disclosureType": "5", "page": "0", "companyCd": companyCd,
            "startTime": startTime, "endTime": endTime, "keyword": "关键字",
            "xxfcbj": ""}
    companyCd = os.path.join(output, companyCd)
    if not os.path.exists(companyCd):
        os.mkdir(companyCd)

    print(companyCd)
    r = requests.post(
        "http://www.neeq.com.cn/disclosureInfoController/infoResult.do?callback=%s" % callback, data=data)
    annoucements = json.loads(
        r.text[:-2].replace(callback + "([", ""))  # 去掉一头一尾，得到一个json的list,并取唯一一个元素，变成dict类型

    annoucements = annoucements['listInfo']['content']
    for annoucement in annoucements:
        disclosureTitle = annoucement["disclosureTitle"].replace(
            ":", "_")+"." + annoucement['fileExt']
        destFilePath = BASE_URL + annoucement['destFilePath']
        print(destFilePath)
        print(disclosureTitle)

        r = requests.get(destFilePath)
        with open(os.path.join(companyCd, disclosureTitle), "wb") as f:
            f.write(r.content)

    print("*"*20)


for stock_id in stock_ids:
    download_announcement(stock_id)
