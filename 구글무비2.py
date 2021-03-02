from selenium import webdriver
import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
}
url = "https://play.google.com/store/movies/top"


browser = webdriver.Chrome("./chromedriver")
browser.maximize_window()
browser.get(url)

# 지정한 위치로 스크롤 내리기
# 모니터의(해상도) 높이인 1080만큼 스크롤 내리
# browser.execute_script("window.scrollTo(0,2080)")로


# 화면 가장 아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)") # 화면가장 아래

import time
interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행

while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight")

    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")



soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()


    # 할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})

    if original_price:
        original_price = original_price.get_text()
    else:
        continue

    # 할인 된 가격

    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    print("할인된 가격 : {0}", price)
    link = "https://play.google.com"+movie.find("div", attrs={"class":"b8cIId ReQCgd Q9MA7b"}).a["href"]
    print(link)

browser.quit()



