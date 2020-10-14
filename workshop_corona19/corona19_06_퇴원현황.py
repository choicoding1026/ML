'''
  서울시 코로나19  데이터 수집 및 분석

  24.

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

# 24. 퇴원 현환
print(df["퇴원현황"])
print(df["퇴원현황"].unique())
print(df["퇴원현황"].value_counts())

## nan ==> "치료중" 으로 변경
df["퇴원현황"].fillna("치료중", inplace=True)
print("퇴원현황 빈도수: \n", df["퇴원현황"].value_counts())
# 퇴원     4894
# 치료중     606
# 사망       64
print("퇴원현황 빈도수 비율: \n", df["퇴원현황"].value_counts(normalize=True))
# 퇴원     0.879583
# 치료중    0.108914
# 사망     0.011503

# 퇴원현황 시각화
import matplotlib.pyplot as plt
plt.rc("font", family="Malgun Gothic") # 한글 처리
# plt.rc("figure", titlesize=4) # title 크기
plt.rc("ytick", labelsize=8) # y축 라벨 크기
plt.rc("xtick", labelsize=8) # x축 라벨 크기
plt.style.use("fivethirtyeight")
g = df["퇴원현황"].value_counts().sort_values().plot.barh(figsize=(6,4))
xxx = df["퇴원현황"].value_counts().sort_values()
yyy = df["퇴원현황"].value_counts(normalize=True).sort_values()
for i in range(len(xxx)): # 0 ~ 개수만큼
    day_count = xxx.iloc[i]
    day_count_p = str(np.round(yyy.iloc[i] * 100,1))+"%"
    g.text(x=day_count, y=i, s=day_count_p, fontsize=14, c="r")
plt.show()