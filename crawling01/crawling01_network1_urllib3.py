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
from urllib.parse import urlencode

# 1. 요청 url 지정
# url = "http://mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1014"
url = "http://mois.go.kr/gpms/view/jsp/rss/rss.jsp"

params = {
    "ctxCd": 1014
}
print("queryString 변경 전: ", params)
params = urlencode(params)
print("queryString 변경 후: ", params)

try:
    response = urlopen(url+"?"+params)
    encoding = response.info().get_content_charset(failobj="utf-8")
    response_data = response.read().decode(encoding)
    print(response_data)
except Exception as e:
    print(e)
