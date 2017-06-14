import requests
from bs4 import BeautifulSoup
import pandas as pd

apikey1 = 'c23ddc34b885f710026c4fa1b72fd25b'
apikey2 = 'b63169966f69aeb0a023bbf18c9f471c'
apikey3 = '8c7f6e9c86555619ec8a6b913f401d4b'
apikey4 = "ee6747c625d134736e99ae8c52ca301f"
apikey5 = 'f130df17bfba070ada0a8018b7903ca0'
apikey6 = '0dab17d2508a2d36719dc2ecb9d8e74c'



# Full address 가 아니므로 다음 API를 이용해서 Full address로 바꾸는 작업을 해주는 함수
def toFullAdd(df_paik):
    list2 = []
    num = 0
    while num < len(df_paik):
        url = "https://apis.daum.net/local/geo/addr2coord?apikey={}&q={}&output =xml".format(apikey2, df_paik.iloc[num, 0].split(",")[0])
        source_code = requests.get(url)
        source_code.encoding = "utf-8"
        plain_text = source_code.text
        #print(plain_text)
        bs = BeautifulSoup(plain_text, "html.parser")
        title = bs.find_all("title")
        mod = 1
        for i in title:
            if mod % 2 == 0:
                print(i.get_text())
                list2.append(i.get_text())
            mod += 1
        num += 1
    return list2




# 빽다방 홈페이지에서 매장 주소 크롤링
def paikStores(max_pages):
    list1 = []
    page = 1
    while page < max_pages:
        url = "http://www.paikdabang.com/paiks/store.asp?page="+str(page)+"&shop_region=&shop_name=&shop_seoul="
        source_code = requests.get(url)
        source_code.encoding = "euc-kr"
        # requests.get 을 이용해서 url의 데이터를 받아온다
        plain_text = source_code.text
        bs = BeautifulSoup(plain_text , "html.parser")
        table1 = bs.find_all("img", src="img/st_icon_03.png")

        for i in table1:
            list1.append(i.get_text().split(": ")[1])
        page += 1

    df_paik = pd.DataFrame(list1, columns=["주소"])
    paikList = toFullAdd(df_paik)
    paikList = pd.DataFrame(paikList, columns=["주소"])
    return paikList

pages = 55
paikList = paikStores(pages)
#paikList.to_csv("/Users/sinsanghun/Documents/pycharm/fastcampus/paik2.csv")





