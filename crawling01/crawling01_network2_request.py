'''
    python network
    1. 내장된 라이브러리 사용
        1) urllib
            (1) urlretrieve(): 지정된 url을 요청하여 응답데이터를 받아 파일로 저장
            (2) urlopen(): 지정된 url을 요청하여 응답처리하는 함수
            (3) urlparse(): url 정보
            (4) urlencode(): dict를 queryString으로 변경해주는 함수
    2. 외부 라이브러리 사용
        1) apache에서 제공하는 requests 라이브러리
        2) pip install requests
            import requests
'''
import requests

# 1. url 지정
url = "http://www.w3schools.com"

# 2. url 요청
response = requests.get(url)

# 3. 응답 데이터 정보
print(response.status_code)
print(response.url)
print(response.headers)
print(response.encoding)
print(response.raw)
print(response.cookies.items())
print(response.content) # byte
print(response.content.decode('utf-8')) # str
print(response.text) # str

