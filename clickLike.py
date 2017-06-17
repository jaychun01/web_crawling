# reference : https://beomi.github.io/2017/02/27/HowToMakeWebCrawler-With-Selenium/
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

CDpath = "/Users/sinsanghun/Documents/pycharm/seleniumTest/chromedriver"


# 크롬 드라이버의 위치를 지정해준다
driver = webdriver.Chrome(CDpath)

def login(myid, mypw, id):
    driver.get("https://www.instagram.com/")  # 웹 주소를 받아온다
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a').click()

    # 로그인을 한다
    driver.find_element_by_name('username').send_keys(myid)
    driver.find_element_by_name('password').send_keys(mypw)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/span/button').click()
    driver.implicitly_wait(3)

    # id의 인스타에 들어간다
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(id)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]').click()



def click():
    driver.implicitly_wait(3)
    # 첫번째 사진 클릭
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div[1]/div[1]/a[1]').click()

    num = 1
    while True :
        time.sleep(1.5)
        try:
            if num == 1 :
                # 좋아요 누르고 다음 사진으로 이동
                driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/article/div[2]/section[1]/a[1]').click()
                driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/a').click()
                driver.implicitly_wait(4)
            else :
                # 좋아요 누르고 다음 사진으로 이동
                driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/article/div[2]/section[1]/a[1]').click()
                driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/a[2]').click()
                driver.implicitly_wait(4)
        except :
            # 사진의 끝에 갔을 때 에러 발생하면 루프 종료
            break
        num += 1


def like(myid, mypw, id):
    login(myid, mypw, id)
    click()


# like(myid, mypw, id)



