'''
    python network
    1. 내장된 라이브러리 사용
        1) urllib
            (1) urlretrieve(): 지정된 url을 요청하여 응답데이터를 받아 파일로 저장
            (2) urlopen(): 지정된 url을 요청하여 응답처리하는 함수
            (3) urlparse(): url 정보
            (4) urlencode(): dict를 queryString으로 변경해주는 함수
    2. 외부 라이브러리 사용
        - apache에서 제공하는 requests 라이브러리
'''

from urllib.request import urlopen


# 1. 요청 url 지정
url = "http://www.w3schools.com"

# 2. url open
response = urlopen(url)

# 3. response 객체 속성 정보
print(response.status, response.getcode()) # 200: 성공, 404: File not found, 405: GET/POST 불일치, 500: 서버오류..
print(response.url)
print(response.info())

# 4. 응답 데이터 읽기1 - read()함수 (한꺼번에 bytes로 읽기)
# try:
#     # 한글처리 및 bytes 처리 인코딩(암호화)
#     encoding = response.info().get_content_charset(failobj="utf-8")
#     response_data = response.read().decode(encoding) # 디코딩(복호화)
#     print(response_data)
# except Exception as e:
#     print(e)

# 4. 응답 데이터 읽기2 - readline()함수 (한줄씩 읽기)
# try:
#     # 한글처리 및 bytes 처리 인코딩(암호화)
#     encoding = response.info().get_content_charset(failobj="utf-8")
#     while True:
#         line = response.readline().decode(encoding) # 디코딩(복호화)
#         if not line: break
#         print(line, end="")
# except Exception as e:
#     print(e)

# 4. 응답 데이터 읽기3 - readlines(한꺼번에 list로 읽기)
try:
    # 한글처리 및 bytes 처리 인코딩(암호화)
    encoding = response.info().get_content_charset(failobj="utf-8")
    for line in response.readlines():
        print(line.decode(encoding), end="")
except Exception as e:
    print(e)