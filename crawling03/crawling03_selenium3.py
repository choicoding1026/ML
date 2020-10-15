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
print(browser)

# 2. url  요청
browser.get("http://www.naver.com")

# 관행적으로 delay를 좀 시켜준다.
browser.implicitly_wait(2) # 초 단위, 중지 중에 브라우저가 모두 DOM 로딩되면 실행

# 3. naver 사이트에서 로그인 버튼 찾기 => .link_login
btn_element = browser.find_element_by_css_selector(".link_login")
btn_element.click() # 로그인 화면 이동

# 관행적으로 delay를 좀 시켜준다.
import time
time.sleep(2) # 초 단위, 무조건 2초 중지

# #id #pw 아이디 비밀번호 입력
id_element =browser.find_element_by_id("id")
id_element.send_keys("ID")
pw_element =browser.find_element_by_id("pw")
pw_element.send_keys("PW")

# 관행적으로 delay를 좀 시켜준다.
browser.implicitly_wait(2) # 초 단위, 중지 중에 브라우저가 모두 DOM 로딩되면 실행

# 로그인 submit
submit_element = browser.find_element_by_id("log.login")
submit_element.click()



