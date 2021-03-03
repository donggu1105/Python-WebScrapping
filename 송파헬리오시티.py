from bs4 import BeautifulSoup
from selenium import webdriver
import re

options = webdriver.ChromeOptions()
options.headless = True

browser = webdriver.Chrome("./chromedriver", options=options)
url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
browser.get(url)

soup = BeautifulSoup(browser.page_source, "lxml")


houses = soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr")

for idx, house in enumerate(houses):

    cols = house.find_all("td")

    print("========매물"+str(idx+1)+"==========")
    print("거래 :"+ cols[0].get_text().strip())
    print("면적 :"+ cols[1].get_text().strip())
    print("가격 :"+ cols[2].get_text().strip())
    print("동 :"+ cols[3].get_text().strip())
    print("층 :"+ cols[4].get_text().strip())


browser.quit()
