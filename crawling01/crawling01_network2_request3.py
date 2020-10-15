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
        3) session
            다양한 기능 추가(Restful - get/post/put/delete, ..)
'''
import requests

# 1. url 지정
url = " http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"

params = {
    "key":"3d430a039fb1bae3fe5f0bc48df64e46",
    "targetDt":"20201014"
}
# 2. url 요청
session = requests.session()
response = session.get(url, params=params)

response_data = response.content.decode("utf-8")

json_object = response.json()
print(type(json_object))



