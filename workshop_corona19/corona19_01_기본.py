'''
  서울시 코로나19  데이터 수집 및 분석
  1. 사이트
   http://www.seoul.go.kr/coronaV/coronaStatus.do

'''

import pandas as pd
import numpy as np

# 1. url 지정
url = "http://www.seoul.go.kr/coronaV/coronaStatus.do"

# 2. pd.read_html() 사용하여 <table>태그 필터링
table = pd.read_html(url)

# 3. 여러 table정보중에서 4번째가 확진자 정보 테이블이다.
df = table[3]
print("1. 확진자 정보:\n", df.shape)
print("2. 확진자 정보:\n", df.head())


# 4. 파일에 저장 ==> 파일명: seoul_corona_마지막확진일.csv
last_day = df.loc[0, "확진일"] # 10.11
last_day = last_day.replace(".", "_") # 10_11
file_name = f"seoul_corona_{last_day}.csv" #seoul_corona_10_11.csv
df.to_csv(file_name, index=False)
#######################################################
# 5. 파일 읽기 ==>
df = pd.read_csv(file_name, encoding="utf-8") # 한글처리
print("3. csv에 저장된 확진자 정보: \n", df.head(10))