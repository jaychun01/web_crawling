import requests
from bs4 import BeautifulSoup
import pandas as pd

def hosigiStores():
    list1 = []
    sido = {"서울" : 6, "부산" : 3, "대구" : 5, "인천" : 2, "광주" : 2, "대전" : 2, "울산" : 1, "세종":1,
            "강원":2, "경기":10, "경상남도":5, "경상북도":6, "전라남도":2, "전라북도":2, "제주":1, "충청남도":2, "충청북도":2}

    for s, pages in sido.items():
        for s2 in range(1, pages+1) :
            url = "http://www.9922.co.kr/store/search.php?ptype=&page={}&code=store&sido={}".format(s2, s)
            source_code = requests.get(url)
            source_code.encoding = "utf-8"
            plain_text = source_code.text
            bs = BeautifulSoup(plain_text , "html.parser")
            table1 = bs.find_all("table", width="100%", border="0",
                             cellpadding="0", cellspacing="0", class_="storeWrap")

            for i in table1:
                table2 = i.find_all("td", align="left")
                mod = 1
                for j in table2:
                    if mod % 3 == 2:
                        #print(j.get_text())
                        list1.append(j.get_text())
                    mod += 1

    return list1

hosigiList = hosigiStores()

print(hosigiList)
print(len(hosigiList))
# 933개

hosigiDf = pd.DataFrame(hosigiList, columns=["주소"])
#hosigiDf.to_csv("/Users/sinsanghun/Documents/pycharm/fastcampus/hosigi.csv")
