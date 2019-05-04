import requests
import os
from bs4 import BeautifulSoup
i = 1
dirname = os.path.dirname(os.path.abspath(__file__))
os.chdir(dirname)

filename = "stock.txt"
f = open(filename, "w")
BASE_URL = "http://www.jingujie.com/stocklist/?page=%d"
while i <= 769:
    r = requests.get(BASE_URL % i)
    i += 1
    bsObj = BeautifulSoup(r.text, "lxml")
    tbody = bsObj.find("tbody", {"id": "mores"})
    trs = tbody.findAll("tr")
    for tr in trs:
        tds = tr.findAll("td")
        stock_account = tds[0].text
        stock_name = tds[1].text
        f.write(stock_account + "  " + stock_name + "\n")
    f.flush()
