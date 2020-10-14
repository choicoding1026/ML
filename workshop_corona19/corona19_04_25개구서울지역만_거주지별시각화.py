'''
  서울시 코로나19  데이터 수집 및 분석

  18. '거주지' 별 확진자의 빈도수 확인 및 막대 그래프(barh) 시각화
  19. 서울 지역만 추출하고 시각화 ( 서울시 25개구만 출력 ) ==> 타시도, 한국, 기타 항목 제외
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

# 18. '거주지' 별 확진자의 빈도수 구하고 시각화
## '거주지' 별 확진자의 빈도수 확인
gu_count = df["거주지"].value_counts()
print("'거주지' 별 확진자의 빈도수 확인: \n", gu_count)
# (인덱스)   컬럼
#  관악구     417
# 송파구     350
# 성북구     335
# 타시도     322

## '거주지' 별 확진자의 빈도수 확인 및 막대 그래프 시각화
# import matplotlib.pyplot as plt
# plt.rc("font", family="Malgun Gothic") # 한글 처리
# # plt.rc("figure", titlesize=4) # title 크기
# plt.rc("ytick", labelsize=18) # y축 라벨 크기
# plt.rc("xtick", labelsize=18) # x축 라벨 크기
# plt.style.use("fivethirtyeight")
# gu_count.plot.barh(figsize=(15,8))
# plt.show()

# 19. 서울 지역만 추출하고 시각화
## 서울 지역만 추출 ==> 한국, 기타, 타시도 제외
seoul_gu_count = gu_count.index[~gu_count.index.isin(['한국','기타','타시도'])]
print(seoul_gu_count)
seoul_gu_count = gu_count[seoul_gu_count]
print(" 서울 지역만 추출: \n", seoul_gu_count)

# 추출된 데이터로 시각화 ==> barh

import matplotlib.pyplot as plt
plt.rc("font", family="Malgun Gothic") # 한글 처리
# plt.rc("figure", titlesize=4) # title 크기
plt.rc("ytick", labelsize=18) # y축 라벨 크기
plt.rc("xtick", labelsize=18) # x축 라벨 크기
plt.style.use("fivethirtyeight")
g = seoul_gu_count.plot.barh(figsize=(15,8))
for i in range(len(seoul_gu_count)): # 0 ~ 개수만큼
    day_count = seoul_gu_count.iloc[i]
    if day_count >= 200:
        g.text(x=day_count, y=i, s=day_count, fontsize=14, c="r")
plt.show()



