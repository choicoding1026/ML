'''
    python crawling 대표적인 라이브러리: beautiful soup
    1. 2012년 공개된 버전 4
    2. 주로 html parsing에 최적화
        1) parsing 처리 담당하는 parser: html.parser
    3. pip install bs4
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
         <a data-io="link3" href="http://example.com/little" class="sister" id="link3">Little</a>
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
print(type(soup))
print(soup.prettify()) # html 문서 보기
print(dir(soup))

# 2. h1 태그 접근: 순회방식
h1 = soup.html.body.h1
print(h1, type(h1)) # Tag Class
print(h1.string) # h1 태그의 body 값

# 3. p 태그 접근
p = soup.html.body.p
print(p, type(p)) # Tag Class
print(p.string)
print(p.next_element) # p 태그의 자식태그
print(p.attrs) # p 태그 속성
print(p.attrs['id']) # p 태그 속성명이 id인 값

# 4. 형제
p = soup.html.body.p
p2 = p.next_sibling.next_sibling # 공백 때문에 next_sibling 한번 더 지정
print(p2)
print(p2.text)
print(p2.next_element, type(p2.next_element))