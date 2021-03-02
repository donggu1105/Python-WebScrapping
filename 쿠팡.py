import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

for item in items:

    # 광고 제품 제외
    ad_badge = item.find("span",attrs={"class":"ad-badge-text"})

    if ad_badge:
        print("광고상품은 제외합니다")
        continue


    name = item.find("div", attrs={"class":"name"}).get_text() # 제품명

    # 애플 제품제외

    if "Apple" in name:
        print("<Apple 상품을 제외합니다.>")
        continue


    price = item.find("strong", attrs={"class":"price-value"}) # 가격
    if price:
        price = price.get_text()
    else:
        price = "가격없음"

    # 리뷰 100개이상, 평점 4.5 이상 되는것만 조회

    rate = item.find("em", attrs={"class":"rating"})
    if rate:
        rate = rate.get_text()
    else:
        rate = "평점 없음"
        print("<평점 없는 상품 제외합니다.>")

    rate_cnt = item.find("span", attrs={"class":"rating-total-count"})
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
        rate_cnt = rate_cnt[1:-1] # slicing
    else:
        rate_cnt = "평점기록없음"
        print("<평점 수 없는 상품 제외합니다.>")


    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
        print("상품이름 : {0}, 상품 가격 - {1}, 평점 - {2}, 평점수 - {3} ".format(name,price, rate, rate_cnt))

