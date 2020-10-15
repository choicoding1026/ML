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

from urllib.request import urlretrieve

# 1. 요청 url 지정
img_url = "https://s.pstatic.net/static/www/mobile/edit/2016/0705/mobile_212852414260.png"
html_url = "http://www.w3schools.com"

# 2. 파일 다운로드 경로
img_save_path = r"c:\temp\naver.gif"
html_save_path = r"c:\temp\w3schools.html"

# 3. 예외처리
try:
    # header 정보: 네트워크 연동 시 서버와 클라이언트(브라우저) 사이에 전달되는 추가정보
    img_file, img_header = urlretrieve(img_url, img_save_path)
    html_file, html_header = urlretrieve(html_url, html_save_path)
except Exception as e:
    print(e)
else:
    print(img_file, dict(img_header))
    print(html_file, dict(html_header))

