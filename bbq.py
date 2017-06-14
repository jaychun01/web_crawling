import requests
from bs4 import BeautifulSoup
import pandas as pd

def bbqStores():
    list1 = []
    # 1~1382, 2877~4800
    chainId = list(range(1, 1382)) + list(range(2877, 4760))
    for s in chainId:
        url = ('https://www.bbq.co.kr/shop/shop_view.asp?CHAINID={}'.format(s))
        source_code = requests.get(url)
        source_code.encoding = "utf-8"
        # requests.get 을 이용해서 url의 데이터를 받아온다
        plain_text = source_code.text
        bs = BeautifulSoup(plain_text , "html.parser")
        table1 = bs.find_all("li", class_="rightRight")

        mod = 1
        for i in table1:
            if mod == 1:
                #print(s, end=" ")
                #print(i.get_text())
                list1.append(i.get_text())
            mod+=1

    return list1

bbqList = bbqStores()

print(bbqList)

bbqDf = pd.DataFrame(bbqList, columns=["주소"])
#bbqDf.to_csv("/Users/sinsanghun/Documents/pycharm/fastcampus/bbq.csv")
# 1483개