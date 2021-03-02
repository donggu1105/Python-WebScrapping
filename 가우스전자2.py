import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td", attrs={"class":"title"})
# 만화 제목 + 평점 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com"+ cartoon.a["href"]
#     print(title)
#     print(link)

total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})


for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
    print("전체 점수는 {0}".format(total_rates))
    print("평균 점수는 {0}".format(total_rates / len(cartoons)))