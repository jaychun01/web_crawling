# reference : https://beomi.github.io/2017/02/27/HowToMakeWebCrawler-With-Selenium/
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np



def getNbaData(kind, dataidx, season):

    print("======================================================================")
    print("                "+ season + " season "+ kind +" data loading....                 ")
    print("======================================================================")


    CDpath = "/Users/sinsanghun/Documents/pycharm/seleniumTest/chromedriver"
    driver = webdriver.Chrome(CDpath)
    driver.get("http://stats.nba.com/players/" + kind + "/#!?Season=" +season+ "&SeasonType=Regular%20Season&sort=PTS&dir=-1") # 웹 주소를 받아온다
    time.sleep(5)
    driver.implicitly_wait(3)

    columns = []
    data = []
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # 페이지 찾기
    page = soup.find_all("div", class_="stats-table-pagination__info")
    for i in page:
        pageNum = (i.get_text().split("of ")[1])
    page = int(pageNum)

    for k in range(page) :
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        tag = soup.find_all("div", class_="nba-stat-table__overflow")
        num = 0
        for i in tag:
            tag3 = i.find_all("tr")
            for j in tag3:
                if num != 0 :
                    # 데이터 부분
                    row = j.get_text().split("\n")
                    empty = []
                    for idx in range(len(row)):
                        if row[idx] == "":
                            empty.append(idx)
                    row = np.array(row)
                    row = np.delete(row, empty)
                    #row = row[1:]
                    data.append(row)
                    #print(row)
                else :
                    # 칼럼부분
                    row = j.get_text().split("\n")
                    empty = []
                    for idx in range(len(row)):
                        if row[idx] == "":
                            empty.append(idx)
                    row = np.array(row)
                    row = np.delete(row, empty)
                    columns = row[:dataidx]
                    #print(columns)
                num = num + 1
        if k != (page-1) :
            driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/a[2]').click()
            time.sleep(0.5)

    #print(data)
    df = pd.DataFrame(data, columns=columns)
    print(df)
    df.to_csv(season + kind + ".csv")

    driver.close()


# 주소에 넣을 시즌명 만들기
year1 = ["1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010",
         "2011", "2012", "2013", "2014", "2015", "2016" ]
year2 = ["97", "98", "99", "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17" ]

season = []
for i in range(21):
    season.append(year1[i] + "-" + year2[i])



for i in season:
    #getNbaData("advanced",22, i)
    #getNbaData("defense", 20, i)
    #getNbaData("opponent", 27, i) no data
    getNbaData("traditional", 28, i)
    #getNbaData("usage", 25, i)
    #getNbaData("misc", 19, i)




# AGE, W, L

