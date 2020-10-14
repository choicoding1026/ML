'''
  서울시 코로나19  데이터 수집 및 분석

  15. 모든 날짜 출력 ( 확진자가 없는 날짜도 포함 )
  16. NaN값을 0으로 변경 및 누적 확진자수 추가
  17. 일자별 확진자 수 및 누적확진자수 시각화

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

# 15. 모든 날짜 출력 ( 확진자가 없는 날짜도 포함 )
'''
   1) 확진자 발생된 처음 날짜 ~ 확진자 발생된 마지막 날짜  ==> 모든 날짜 표기, 확진자가 없을 수도 있다.
      ==> df_days
       (인덱스) 확진일자
        0   2020-01-24
        1   2020-01-25
        2   2020-01-26
        3   2020-01-27
        4   2020-01-28
        
   2) 확진자 발생된 날짜 df    
      ==>  df_daily_case
      
       (인덱스)       확진수
      2020-01-24    1
      2020-01-30    3
      2020-01-31    3
      
    3) df_days 와 df_daily_case 병합 ==> outer 병합, index 병합
'''

# 가. 처음날짜와 마지막 날짜를 구해서, 이 범위의 날짜를 반환 ==> pd.date_range 활용
'''
 2020-01-24
 ..
 2020-10-11
'''
print(df.columns) # Index(['연번', '환자', '확진일', '거주지', '여행력', '접촉력', '퇴원현황', '확진일자', '월', '주',
# 전체 날짜 만들기
first_day = df.iloc[-1, 7]  # 확진자 발생된 처음 날짜
last_day = df.iloc[0, 7]   # 확진자 발생된 마지막 날짜
print(first_day, last_day)
days = pd.date_range(first_day, last_day)
df_days = pd.DataFrame({"확진일자":days})
print("전체 날짜:\n", df_days.head())

# 확진일자별로 빈도수 구하기
daily_case = df["확진일자"].value_counts().sort_index()
df_daily_case = daily_case.to_frame() # Series ==> DataFrame 변경
df_daily_case.columns =["확진수"]
print("확진일자별로 빈도수: \n",df_daily_case)

# df_days 와 df_daily_case 병합 ==> 일치하지 않으면 NaN
# all_day = pd.merge(df_days, df_daily_case, left_on="확진일자",
#                    right_index=True, how="left")
all_day = pd.merge(df_days, df_daily_case, left_on="확진일자",
                   right_on=df_daily_case.index, how="left")
print("15. 모든 날짜 출력 ( 확진자가 없는 날짜도 포함 ) \n", all_day)

# NaN값을 0으로 변경 및 누적 확진자수 추가
all_day = all_day.fillna(0)
all_day['확진수'] = all_day['확진수'].astype(int)
all_day['누적확진자수'] = all_day['확진수'].cumsum()
print("16. 누적 확진자수 추가  \n", all_day)


# 일자별 확진자 수 및 누적확진자수 시각화
'''
    1) all_day의 '확진일자' 이용하여  '일자' 컬럼 추가
        확진일자  확진수  누적확진자수 일자
    0   2020-01-24    1       1    01-24
     ..
    2) 일자, 확진수, 누적확지자수 만 추출하고 일자를 인덱스로 변경
       cum_all_day = None
'''
all_day["일자"] = all_day["확진일자"].astype(str).map(lambda x:x[-5:])
print(all_day)
# 일자, 확진수, 누적확진자수 만 추출하고 일자를 인덱스로 변경해서 출력
all_day = all_day[["일자","확진수","누적확진자수"]]
cum_all_day = all_day.set_index("일자")
print(cum_all_day.head())

# cum_all_day 이용해서 선 그래프로 시각화
import matplotlib.pyplot as plt
plt.rc("font", family="Malgun Gothic") # 한글 처리
# plt.rc("figure", titlesize=4) # title 크기
plt.rc("ytick", labelsize=18) # y축 라벨 크기
plt.rc("xtick", labelsize=18) # x축 라벨 크기
plt.style.use("fivethirtyeight")
cum_all_day.plot(figsize=(15,8))
plt.show()

print(help(plt.style.use))
print(plt.style.available)
# ['Solarize_Light2', '_classic_test_patch', 'bmh',
#  'classic', 'dark_background', 'fast', 'fivethirtyeight',
#  'ggplot', 'grayscale', 'seaborn', 'seaborn-bright',
#  'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette',
#  'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted',
#  'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel',
#  'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white',
#  'seaborn-whitegrid', 'tableau-colorblind10']












