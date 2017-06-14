import requests
from bs4 import BeautifulSoup
import pandas as pd

def kyochonStores():
    list1 = []
    # 18 , 50
    sido1 = range(1, 18)
    sido2 = range(1, 50)
    for i in sido1:
        for j in sido2 :
            url = "http://www.kyochon.com/shop/domestic.asp?sido1={}&sido2={}&txtsearch=".format(i, j)
            source_code = requests.get(url)
            source_code.encoding = "utf-8"
            # requests.get 을 이용해서 url의 데이터를 받아온다
            plain_text = source_code.text
            bs = BeautifulSoup(plain_text , "html.parser")
            table1 = bs.find_all("ul", class_="list")

            for k in table1:
                table2 = k.find_all("dd")
                for kk in table2:
                    aa = kk.get_text().lstrip().split("(")[0]
                    list1.append(aa.split("\r")[0])
    return list1

kyochonList = kyochonStores()

print(kyochonList)
print(len(kyochonList))
# 988개

kyochonDf = pd.DataFrame(kyochonList, columns=["주소"])
#kyochonDf.to_csv("/Users/sinsanghun/Documents/pycharm/fastcampus/kyochon.csv")
