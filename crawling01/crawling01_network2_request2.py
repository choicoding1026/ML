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
url = " http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=3d430a039fb1bae3fe5f0bc48df64e46&targetDt=20201014"

# 2. url 요청
response = requests.get(url)

# 3. 응답 결과 받기
response_data = response.content.decode("utf-8")
print(type(response_data)) # <class 'str'>

# 4. json형식의 dict로 변경
import json

json_object = json.loads(response_data)
print(type(json_object)) # <class 'dict'>

from pprint import pprint # dict type 읽기 쉽게 출력해주는 패키지
# print(pprint(json_object))

# 5. movieNm 출력
for dailyBoxOffice in json_object['boxOfficeResult']['dailyBoxOfficeList']:
    print("rank{}. {}".format(dailyBoxOffice['rank'], dailyBoxOffice['movieNm']))

'''
    1) 공공 데이터 사용해 임의의 데이터를 요청해서 반환 => Open API 활용한 데이터 처리(크롤링)
        정부, 기업체, 학교 등
    2) 응답 데이터 종류: JSON, csv, xml, yml 등
    3) pandas의 DataFrame으로 변환 및 파일, DB 저장(데이터 전처리 필요)
    4) 데이터 분석 등 활용
'''