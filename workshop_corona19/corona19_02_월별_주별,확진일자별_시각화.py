'''
  서울시 코로나19  데이터 수집 및 분석
  1. 사이트
   http://www.seoul.go.kr/coronaV/coronaStatus.do

  2. '연번' 기준으로 오름차순 정렬
  3.  확진일의 빈도수 ==> 어느 날짜에 가장 많이 확진이 되었는지 확인 가능
  4.  '확진일자' 컬럼 추가 => 2020-10-11 날짜형식
  5.  '확진일자' 날짜 데이터 컬럼 이용하여 '월' 컬럼 추가
  6.  '확진일자' 날짜 데이터 컬럼 이용하여 '주(week)' 컬럼 추가
  7.  '확진일자' 날짜 데이터 컬럼 이용하여 '월-일' 컬럼 추가
  8. 확진자수가 가장 많은 날 출력
  9. 확진자수가 가장 많은 날 이용하여 발생이력 출력
  10. 일자별 확진자수 선그래프로 시각화
  11. 일자별 확진자수 선그래프로 시각화 + text 추가
  12. 월별 확진자수  막대그래프로 시각화 + text 설정
  13. 가장 최근 데이터만 50개 보기 ==> df["월-일"] 이용하고 선그래프로 시각화 + text 지정
  14. 주별 확진자수  막대그래프로 시각화 + text 설정
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

# 7.  확진자수가 가장 많은 날 출력
day_count = df['월-일'].value_counts().sort_values(ascending=False)
print(day_count)
print(day_count.max())
max_day = day_count[day_count == day_count.max()] # boolean 색인
print("7. 확진자수가 가장 많은 날: \n", max_day.index[0]) # 08-29

# 8. 확진자수가 가장 많은 날 이용하여 발생이력 출력 ==> df 에서 08-29 해당되는 행 출력
max_day_df = df[df["월-일"]==max_day.index[0]]  # boolean 색인
print("8. 확진자수가 가장 많은 날의 발생이력: \n", max_day_df )


'''
   시각화 방법 3가지
   1. matplotlib 만 사용
   2. matplotlib + seaborn 사용 ( matplotlib 기능을 단순화한 것이 seaborn )
   3. matplotlib + pandas  ( pandas내에 matplotlib 기반의 시각화 기능 포함 ) 
'''
import matplotlib.pyplot as plt
plt.rc("font", family="Malgun Gothic") # 한글 처리
# plt.rc("figure", titlesize=4) # title 크기
plt.rc("ytick", labelsize=18) # y축 라벨 크기
plt.rc("xtick", labelsize=18) # x축 라벨 크기

# 9. 일자별 확진자수 선그래프로 시각화
# xxx = df["확진일자"].value_counts().sort_index()
# xxx.plot(title="일자별 확진자수", figsize=(12,8)) # 인덱스값: x 축으로  값: y 축으로
# plt.axhline(100, color="r", linestyle="--") # 라인선 그리기
# plt.show()


# 10. 일자별 확진자수 선그래프로 시각화 + text 추가
# xxx = df["월-일"].value_counts().sort_index()
# g = xxx.plot(title="일자별 확진자수", figsize=(20,8)) # 인덱스값: x 축으로  값: y 축으로
# for i in range(len(xxx)): # 0 ~ 개수만큼
#     day_count = xxx.iloc[i]
#     if day_count >= 100:
#         g.text(x=i, y=day_count, s=day_count, fontsize=14, c="r")
# plt.axhline(100, color="r", linestyle="--") # 라인선 그리기
# plt.show()
# print(help(g.text))

# 11. 월별 확진자수  막대그래프로 시각화 + text 설정
# xxx = df["월"].value_counts().sort_index()
# g = xxx.plot.bar(title="월별 확진자수", figsize=(30,8)) # 인덱스값: x 축으로  값: y 축으로
# for i in range(len(xxx)): # 0 ~ 개수만큼
#     day_count = xxx.iloc[i]
#     if day_count >= 100:
#         g.text(x=i, y=day_count, s=day_count, fontsize=14, c="r")
# plt.axhline(1000, color="r", linestyle="--") # 라인선 그리기
# plt.show()

# 12. 가장 최근 데이터만 50개 보기 ==> df["월-일"] 이용하고 선그래프로 시각화 + text 지정
# xxx = df["월-일"].value_counts().sort_index()
# xxx = xxx[-50:]
# g = xxx.plot(title="최근 데이터만 50개 확진자수", figsize=(20,8)) # 인덱스값: x 축으로  값: y 축으로
# for i in range(len(xxx)): # 0 ~ 개수만큼
#     day_count = xxx.iloc[i]
#     g.text(x=i, y=day_count, s=day_count, fontsize=14, c="r")
# plt.show()

# 13. 주별 확진자수  막대그래프로 시각화 + text 설정
xxx = df["주"].value_counts().sort_index()
g = xxx.plot.bar(title="주별 확진자수", figsize=(30,8)) # 인덱스값: x 축으로  값: y 축으로
plt.axhline(100, color="r", linestyle="--") # 라인선 그리기
plt.show()




