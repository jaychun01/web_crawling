# reference : https://beomi.github.io/2017/02/27/HowToMakeWebCrawler-With-Selenium/
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

CDpath = "/Users/sinsanghun/Documents/pycharm/seleniumTest/chromedriver"

# 크롬 드라이버의 위치를 지정해준다
driver = webdriver.Chrome(CDpath)

def instahash(id):
    driver.get("https://www.instagram.com/"+id) # 웹 주소를 받아온다
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div[1]/div[1]/a[1]').click()

    lst = []
    num = 1
    while True :
        time.sleep(1.5)
        try:
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            tag = soup.find_all("ul", class_="_h3rdq")

            #일반글 + 해시태그
            for i in tag:
                mod = 1
                lst2 = []
                if mod % 4 == 1:
                    tag2 = i.find("span")
                    for j in tag2:
                        lst2.append(j.get_text())
                        print(j.get_text(), end="")
                mod += 1
                lst.append(lst2)

            if num == 1 :
                driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/a').click()
                driver.implicitly_wait(4)
            else :
                driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/a[2]').click()
                driver.implicitly_wait(4)
            print("")
            print("")
        except :
            break
        num += 1

    return pd.DataFrame(lst)

id = "amateurpeterpan"
lst = instahash(id)
lst.to_csv(id+".csv")


# naver log in
# driver.get('https://nid.naver.com/nidlogin.login')
# find input tags of id and pw
# driver.find_element_by_name('id').send_keys('tymbcs13')
# driver.find_element_by_name('pw').send_keys('pw')
# driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()


