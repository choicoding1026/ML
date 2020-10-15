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
url = "http://httpbin.org/"
params = {
    "ID":"justin6130",
    "PW":"1234"
}

# 2. post 요청
session = requests.session()
response = session.post(url+"post", params=params)
json_data = response.json()
print(json_data)

# 3. get 요청
session = requests.session()
response = session.get(url+"get", params=params)
json_data = response.json()
print(json_data)

# 4. put 요청
session = requests.session()
response = session.put(url+"put", params=params)
json_data = response.json()
print(json_data)

# 5. delete 요청
session = requests.session()
response = session.delete(url+"delete", params=params)
json_data = response.json()
print(json_data)








