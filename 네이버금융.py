import csv
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"}

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f) # 이거 이용해서 쓸수있
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t") # 탭으로 뛰어져있으니 스플릿해서 리스트로 변환
print(type(title))
writer.writerow(title)

for page in range(1,2):

    res = requests.get(url + str(page), headers = headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text,"lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")

    for row in data_rows:
            columns = row.find_all("td")

            if len(columns) <= 1: # 의미없는 데이터는 skip
                continue
            data = [column.get_text().strip() for column in columns]
            # print(data)
            writer.writerow(data)