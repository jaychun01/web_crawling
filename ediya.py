import requests
from bs4 import BeautifulSoup
import pandas as pd

def ediyaStores(max_pages):
    list1 = []
    page = 1
    while page < max_pages:
        url = "http://ediya.com/board/listing/brd/store/page/"+str(page)
        source_code = requests.get(url)
        source_code.encoding = "utf-8"
        # requests.get 을 이용해서 url의 데이터를 받아온다
        plain_text = source_code.text
        bs = BeautifulSoup(plain_text , "html.parser")
        table1 = bs.find_all("td", class_="left")

        for i in table1:
            list1.append(i.get_text().split(" (")[0])
        page += 1

    return list1

ediyaList = ediyaStores(157)
# max_page = 157
print(ediyaList)
print(len(ediyaList))

ediyaDf = pd.DataFrame(ediyaList, columns=["주소"])
#ediyaDf.to_csv("/Users/sinsanghun/Documents/pycharm/fastcampus/ediya.csv")