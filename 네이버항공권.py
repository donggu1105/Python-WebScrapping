import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver")
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)

browser.find_element_by_link_text("가는날 선택").click()

# 이번달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번달 27이두개니까 앞에
# browser.find_elements_by_link_text("28")[0].click() # [0] -> 이번달 27이두개니까 앞에

# 다음 달
# browser.find_elements_by_link_text("27")[1].click() # [1] -> 다음 달
# browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음 달

# 이번달 27일 다음달 28일 선택
browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번달
browser.find_elements_by_link_text("28")[1].click() # [0] -> 이번달

# 제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()
browser.find_element_by_link_text("항공권 검색").click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    # 브라우저를  최대 10초 동안기다려, 그 안에 xpath 조건에 만족하는 엘리먼트가 위치할떄까지
    print(elem.text)
finally:
    browser.quit()

