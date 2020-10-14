'''
  서울시 코로나19  데이터 수집 및 분석

  26. 여행력

'''

import pandas as pd
import numpy as np

file_name = "seoul_corona_10_11_.csv"
df = pd.read_csv(file_name, encoding="utf-8") # 한글처리

# 1. '연번' 기준으로 오름차순 정렬
df = df.sort_values(by="연번", ascending=False)
print("1. '연번' 기준으로 오름차순 정렬:\n", df.head())

# 2. 확진일의 빈도수 ==> 어느 날짜에 가장 많이 확진이 되었는지 확인 가능
# value_counts() 자동으로 내림차순 정렬해서 반환
print("2. 확진일의 빈도수: \n", df["확진일"].value_counts())

# 3. '확진일자' 컬럼 추가 => 2020_10_11 날짜형식
# 기존의 '확진일' 컬럼값은 문자이기 때문에 날짜로 변경해야 된다.
'''
  1) 10.11 --> 10-11 변경
  2) 10-11 --> 2020-10-11 로 변경
  3) 2020-10-11 문자열 ---- > 2020-10-11 날짜로 변경 (pd.to_datetime 함수 )
  4) df["확진일자"] = 날짜
'''
df["확진일자"] = pd.to_datetime("2020-"+df["확진일"].str.replace(".", "-"))
print("3. '확진일자' 컬럼 추가: \n", df.head())

# 4. '확진일자' 날짜 데이터 컬럼 이용하여 '월' 컬럼 추가
df["월"] = df["확진일자"].dt.month
print("4. '월' 컬럼 추가: \n", df.head())

# 5. '확진일자' 날짜 데이터 컬럼 이용하여 '주(week)' 컬럼 추가
# 해당년도의 몇번째 주(week)인지 반환
df["주"] = df["확진일자"].dt.isocalendar().week
print("5. '주' 컬럼 추가: \n", df.head())

# 6. '확진일자' 날짜 데이터 컬럼 이용하여 '월-일' 컬럼 추가
# m = df["확진일자"].dt.month
# d = df["확진일자"].dt.day
# df["월-일"] = m.astype(str) + "-" + d.astype(str)
df["월-일"] = df["확진일자"].astype(str).map(lambda x:x[-5:]) # map함수는 데이터가공시 사용

print("6. '월-일' 컬럼 추가: \n", df.head())
print("6. '월-일' 컬럼 추가: \n", df.tail())
########################################################################

# 26. 여행력
print(df["여행력"])
print(df["여행력"].unique())
print(df["여행력"].value_counts())

'''
   1.  '-' ==> NaN 처리  
       ==> "-"을  np.nan 으로 변경 처리
       
   2.  공통명으로 변경
       '아랍에미리트',  'UAE' ===> 아랍에미리트
       '중국 청도','우한교민','우한 교민', '중국 우한시', '중국' ==> 중국
       '프랑스, 스페인','스페인, 프랑스' ==> 프랑스, 스페인
       체코,헝가리,오스트리아,이탈리아,프랑스,모로코,독일,스페인,영국,폴란드,터키,아일랜드 ==>유럽
       브라질,아르헨티아,칠레,볼리비아, 멕시코, 페루 => 남미
'''


## 공통명으로 변경하고 시각화
df["해외"]=df["여행력"]
print(df["해외"].str.contains('아랍에미리트|UAE'))
df.loc[df["해외"].str.contains('아랍에미리트|UAE'), "해외"] = "아랍에미리트"
df.loc[df["해외"].str.contains('우한|중국'), "해외"] = "중국"
df.loc[df["해외"].
str.contains('체코|헝가리|오스트리아|이탈리아|프랑스|모로코|독일,스페인|영국\폴란드|터키|아일랜드'),
       "해외"] = "유럽"
df.loc[df["해외"].str.contains('브라질|아르헨티아|칠레|볼리비아|멕시코|페루'), "해외"] = "남미"
## "-"을  np.nan 으로 변경 처리
df["해외"]=df["해외"].replace("-", np.nan)
print(df["해외"].unique())
print(df["해외"].value_counts())

# 상위 15개만 시각화
import matplotlib.pyplot as plt
plt.rc("font", family="Malgun Gothic") # 한글 처리
# plt.rc("figure", titlesize=4) # title 크기
plt.rc("ytick", labelsize=8) # y축 라벨 크기
plt.rc("xtick", labelsize=8) # x축 라벨 크기
plt.style.use("fivethirtyeight")
g = df["해외"].value_counts().head(15).sort_values().plot.barh(title="xxxx", figsize=(16,4))

plt.show()

