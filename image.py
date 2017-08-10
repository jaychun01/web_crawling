# reference : https://beomi.github.io/2017/02/27/HowToMakeWebCrawler-With-Selenium/
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import urllib.request
import os
import numpy as np


def face(name):
    CDpath = "/Users/sinsanghun/Documents/pycharm/seleniumTest/chromedriver"

    driver = webdriver.Chrome(CDpath) # 크롬 드라이버의 위치를 지정해준다
    driver.get("https://www.google.com/imghp?hl=ko")  # 웹 주소를 받아온다

    # 해당 연예인 이미지 검색
    driver.find_element_by_name('q').send_keys(name)
    driver.find_element_by_xpath('//*[@id="_fZl"]').click()
    driver.implicitly_wait(3)

    # 첫번째 사진 클릭
    driver.find_element_by_xpath('//*[@id="rg_s"]/div[1]').click()
    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    tag = soup.findAll("img", class_="irc_mi")

    num = 1
    for i in tag:
        if num==2:
            url = i['src']
        num = num + 1

    image_set = [url]

    # 두번째 사진부터 url 검색
    for j in range(500):
        driver.find_element_by_xpath('// *[ @ id = "irc_ra"]').click()
        time.sleep(3)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        tag2 = soup.findAll("img", class_="irc_mi")

        for k in tag2:
            if 'src' in str(k):
                url = k['src']
                image_set.append(url)


    # 사진 저장
    image_set = np.unique(image_set)

    for number in range(len(image_set)):
        try :
            print(number)
            full_name = name + str(number + 1) + ".jpg"
            urllib.request.urlretrieve(image_set[number], full_name)
        except :
            pass

    driver.close()

# 한지민, 조여정, 아이비
mlist = []
flist = ["신민아", "하지원", "이보영", "박보영", "전혜빈", "서현진", "전도연", "송혜교", "김소현", "김유정", "김슬기",
         "정유미", "김태희", "조혜련", "박민영", "문채원", "김신영", "박나래", "김숙", "안영미", "이국주", "신봉선",
         "오나미", "장도연", "고아라", "강예원", "구혜선", "강소라", "손예진", "박신혜", "공효진", "문근영", "한효주",
         "전지현", "김옥빈", "이나영", "김고은", "김희선", "엄정화", "김혜수", "엄지원", "라미란", "심은하", "김민희"]
flist2 = ["서현", "태연", "강민경", "이효리", "옥주현", "최유정", "김세정", "소희", "유진", "아이유"]


for name in flist2:
    pwd = os.getcwd()  # 현재 경로 저장
    os.mkdir(name)   # 이름으로 디렉토리 생성
    os.chdir(pwd+"/"+name) # 위치 이동
    face(name) # 이미지 크롤링
    os.chdir(pwd) # 다시 원래 위치로 이동



