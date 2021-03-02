import requests
header = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"}
res = requests.get("https://naver.com", header=header)
res.raise_for_status()

with open("mynaver.html", "w", encoding="utf8") as f :
    f.write(res.text)