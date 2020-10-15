'''
    python crawling 대표적인 라이브러리: beautiful soup
    1. 2012년 공개된 버전 4
    2. 주로 html parsing에 최적화
        1) parsing 처리 담당하는 parser: html.parser
    3. pip install bs4
    4. 요소 찾기
        1) find, find_all => 태그로 찾기(태그명, 속성)
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

# 2. a 태그 선택(find), 모든 a 태그 선택(find_all)
link = soup.find(name="a")
link1 = soup.find_all("a")
print(link, link.text)
print(link1)
for link in link1:
    print(link.text)

# 3. 모든 a 태그 선택 + 조건
link2 = soup.find_all("a", string=["Elsie", "Little"])
print(link2)
link3 = soup.find_all("a", class_=["sister", "sister2"])
print(link3)
link4 = soup.find_all("a", attrs={"id":"link1","class":"sister"})
print(link4)
link5 = soup.find_all("a", attrs={"class":"sister", "id":"link2"})
print(link5)
link6 = soup.find_all("a", limit=2) # 갯수
print(link6)
