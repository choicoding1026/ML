'''
    python crawling 대표적인 라이브러리: beautiful soup
    1. 2012년 공개된 버전 4
    2. 주로 html parsing에 최적화
        1) parsing 처리 담당하는 parser: html.parser
    3. pip install bs4
    4. 요소 찾기
        1) find, find_all => 태그로 찾기(태그명, 속성)
        2) select_one, select => css로 찾기
            - css 선택자 사용(#id, .class, > 자식,자손, [속성] ...)
'''

from bs4 import BeautifulSoup
import requests

# 1. url 지정
url = "http://www.daum.net"

# 2. url 요청
session = requests.session()
response_data = session.get(url)
# print(response_data.text)
html = response_data.text

# 3. bs4 생성
soup = BeautifulSoup(html, 'html.parser')

# 4. select 함수 이용해서 parsing
menu_list = soup.select(".list_mainsvc > li > a > span")
for menu in menu_list:
    print(menu.text)