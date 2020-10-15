'''
    selenium 라이브러리
    1. 가상의 웹 브라우저를 활용해 자동화
        - www.selenium.dev 접속해서 webdriver 다운로드
    2. pip install selenium
        - 가상의 웹 브라우저를 제어할 수 있다.
    3. headless
        - 브라우저를 열지 않고 내부적으로 동작
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 0. headless option 설정
chrome_options = Options()
chrome_options.add_argument("--headless")

# 1. webdriver 설정
browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe', options=chrome_options)
print(browser)

# 2. url  요청
browser.get("http://www.naver.com")

# 관행적으로 delay를 좀 시켜준다.
browser.implicitly_wait(2) # 초 단위, 중지 중에 브라우저가 모두 DOM 로딩되면 실행

# 3. python 검색
element = browser.find_element_by_id("query")
element.send_keys("hyunjin ryu")

# 관행적으로 delay를 좀 시켜준다.
browser.implicitly_wait(2) # 초 단위, 중지 중에 브라우저가 모두 DOM 로딩되면 실행

element.submit()

# 4. screenshot
browser.save_screenshot(r"c:\temp\ryu.png")