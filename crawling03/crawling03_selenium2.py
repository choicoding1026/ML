'''
    selenium 라이브러리
    1. 가상의 웹 브라우저를 활용해 자동화
        - www.selenium.dev 접속해서 webdriver 다운로드
    2. pip install selenium
        - 가상의 웹 브라우저를 제어할 수 있다.
'''

from selenium import webdriver

# 1. webdriver 설정
browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe')
# print(browser)

# 2. url  요청
browser.get("http://www.daum.net")
print(browser)
