import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/weekday.nhn"
res= requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # lmxl 파서를 통해서 Beautiful 객체를 만듬
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # 첫번쨰로 발견되는 a 태그에대한 정보를 뿌려줘
# print(soup.a.attrs) # a 의 엘리먼트의 속성정보를 반환하고 출력
# print(soup.a["href"]) # a 대괄호 속성값넣으면 해당 속성값정보 출력

# aTag = soup.find("a", attrs={"class" : "Nbtn_upload"}) # 첫번째로 나오는 해당 엘리먼트태그 클래스가 Nbtn_upload 인거 찾아봐
# print(aTag)
#
rank1 = soup.find("li", attrs={"class" : "rank01"})
# print(rank1.a)
# print(rank1.a.get_text()) # text만 가져오기
# print(rank1.next_sibling) # 줄바꿈이있어서 이럴수 있음
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling # next_sibling
# print(rank2.a.get_text())
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling # previous_sibling
# print(rank2.a.get_text())
#
# print(rank1.parent)
#
# rank2 = rank1.find_next_sibling("li") # rank1 기준으로 다음 항목을 찾는데 li 인것만 찾는거임
# print(rank2.a.get_text())
# rank3= rank2.find_next_sibling("li")
# print(rank3.a.get_text())
#
# rank1 = rank2.find_previous_sibling("li")
# print(rank1.a.get_text())

rankList = rank1.find_next_siblings()
for rank in rankList:
    print(rank.a.get_text())


webtoon = soup.find("a", text="바른연애 길잡이-140")  # 텍스트가