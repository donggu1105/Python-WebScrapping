from selenium import webdriver
import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
}
url = "https://play.google.com/store/movies/top"

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)

# with open("movie.html","w",encoding="utf8") as f:
#     f.write(soup.prettify()) # html 문서 예쁘게 출력