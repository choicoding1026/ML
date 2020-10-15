'''
    python crawling 대표적인 라이브러리: beautiful soup
    1. 2012년 공개된 버전 4
    2. 주로 html parsing에 최적화
        1) parsing 처리 담당하는 parser: html.parser
    3. pip install bs4
    4. 요소 찾기
        1) find, find_all => 태그로 찾기(태그명, 속성)
        2) select_one, select => css로 찾기
            - css 선택자 사용(#id, .class, >자식,자손, [속성] ...)
'''

html = \
'''
    <html>
      <head>
        <title>The Dormouse's story</title>
      </head>  
      <body>
       <h1>this is h1 area</h1>
       <h2>this is h2 area</h2>
       <p class="title" id="ccd"><b>The Dormouse's story</b></p>
       <p class="story">
         Once upon a time there were three little sisters.
         <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
         <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
         <a data-io="link3" href="http://example.com/little" class="sister2" id="link3">Little</a>
       </p>
       <p class="story">
          story....
       </p>
      </body>
    </html>
'''

from bs4 import BeautifulSoup

# 1. bs4 초기화
soup = BeautifulSoup(html, "html.parser")

# 2. a 태그 선택(select_one), 모든 a 태그 선택(select)
link = soup.select_one("a")
link1 = soup.select("a")
print(link, link.text)
print(link1)
for link in link1:
    print(link.text)

# 3. 태그 선택 + 조건
link2 = soup.select_one("p.title > b")
print(link2)
link3 = soup.select_one("a[class='sister2']")
print(link3)
link4 = soup.select("a#link1")
print(link4)
