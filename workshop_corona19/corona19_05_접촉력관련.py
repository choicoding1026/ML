'''
  서울시 코로나19  데이터 수집 및 분석

  20. 접촉력 빈도수 확인 및 시각화
  21. 접촉력 월별 빈도수

     종교시설      count
             1    3
             2    4
             ..
     확인 중  1
             2
             ..
           ===> unstack() ( from row to column )
               1  2   3  4 5
     종교시설

   22. 감염경로 불명  '월'및 '주' 단위 확인
   23.  '주' 단위  전체 확진자수 vs 불명 확진자수 시각화 
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

# 20. 접촉력 빈도수 확인 및 시각화
## 접촉력 컬럼의 빈도수 출력
contact_count = df["접촉력"].value_counts()
print("'접촉력' 빈도수 확인: \n", contact_count)
print(df["접촉력"].unique())

# '대구 거주' 와 '대구 거주자' , '대구 XXX' ==> 대구
'''
   1) df["접촉력"] 컬럼에서 '대구' 값이 들어있는 항목을 필터링해서 '대구'변경
      필터링 = '대구'
      df2 = df['country'].str.contains("ni") 활용
'''
print("변경전\n", df.loc[df["접촉력"].str.contains('대구'), "접촉력"].unique())
# ['대구 거주' '대구 방문' '대구 확진자 접촉' '신천지대구교회 관련' '대구 방문(명성교회)' '대구 거주자']
df.loc[df["접촉력"].str.contains('대구'), "접촉력"] = "대구"
print("변경후:\n", df.loc[df["접촉력"].str.contains('대구'), "접촉력"].unique()) # ['대구']
contact_count = df["접촉력"].value_counts()
# print(df["접촉력"].unique())

'''
   공통단어로 통일
   1) XXX 대구 ==> 대구
   2) XXX 교회,기도,성경,성당 ==> 종교시설
   3) 의료원,요양,병원 ==> 병원/요양
   4) 확인 중,확인중 ==> 확인 중
'''
df.loc[df["접촉력"].str.contains('교회|기도|성경|성당'), "접촉력"] = "종교시설"
df.loc[df["접촉력"].str.contains('의료|요양|병원'), "접촉력"] = "병원/요양"
df.loc[df["접촉력"].str.contains('확인 중|확인중'), "접촉력"] = "확인 중"

contact_count = df["접촉력"].value_counts()
print(contact_count.head(20))

# 접촉력 상위 20개 barh 막대 그래프로 시각화
# import matplotlib.pyplot as plt
# plt.rc("font", family="Malgun Gothic") # 한글 처리
# # plt.rc("figure", titlesize=4) # title 크기
# plt.rc("ytick", labelsize=10) # y축 라벨 크기
# plt.rc("xtick", labelsize=18) # x축 라벨 크기
# plt.style.use("fivethirtyeight")
# contact_count.head(20).sort_values().plot.barh(figsize=(15,8))
# plt.show()

# 21. 상위 15개 접촉력 월별 빈도수
top_contact = df["접촉력"].value_counts().sort_values().tail(15)
print(top_contact.index)

## 상위 15개에 해당되는 데이터 추출 ==> 색인
top_group = df[df["접촉력"].isin(top_contact.index)]
print(top_group)

# 접촉력의 월별 ==> groupby
# NaN ==> 0 으로 변경하고  소수점 ==> 정수로 변경해서 출력
result = top_group.groupby(["접촉력","월"])['연번'].count()\
                            .unstack().fillna(0).astype(int)
print(result)

# 22. 감염경로 불명  '월'및 '주' 단위 확인
# 감염경로 불명인 '접촉력'컬럼에서 '확인 중' 색인 ==> df에서 색인
df_unknown = df[df["접촉력"]=="확인 중"]
print("감염경로 불명인 '접촉력'컬럼에서 '확인 중' 색인: \n", df_unknown)

# 감염경로 불명인 월별,주별 갯수(count) 출력
unknown_weekly_case = df_unknown.groupby(['월','주'])['연번'].count()
print(" 월별,주별 갯수(count) 출력: \n", unknown_weekly_case)

# import matplotlib.pyplot as plt
# plt.rc("font", family="Malgun Gothic") # 한글 처리
# # plt.rc("figure", titlesize=4) # title 크기
# plt.rc("ytick", labelsize=18) # y축 라벨 크기
# plt.rc("xtick", labelsize=18) # x축 라벨 크기
# plt.style.use("fivethirtyeight")
# unknown_weekly_case.plot.barh(figsize=(15,8))
# plt.show()


# 23. 주 단위로 감염경로 확인 vs  불명  비교
'''
    감염경로 확인 된 경우
    
    주    갯수
    9     10
    ..
    
    감염경로 불명인 경우
    
    주    갯수
    19     5
    ..

'''
##  '주'단위 전체 확진자수 구하기
all_weekly_case = df["주"].value_counts().to_frame()
all_weekly_case.columns=["확진자수"]
print(all_weekly_case)

##   '주'단위  불명 확진자수 구하기
unknown_all_weekly_case = df_unknown["주"].value_counts().to_frame()
unknown_all_weekly_case.columns=["불명확 확진자수"]
print(unknown_all_weekly_case)

## 병합
'''
  주   전체확진자수  불명 확진자수
  9       62         11
  ..
'''
all_unknown_merge =\
    pd.merge(all_weekly_case, unknown_all_weekly_case,
             left_index=True, right_index=True)

print("확진자수  불명확 확진자수 \n", all_unknown_merge.sort_index())

import matplotlib.pyplot as plt
plt.rc("font", family="Malgun Gothic") # 한글 처리
# plt.rc("figure", titlesize=4) # title 크기
plt.rc("ytick", labelsize=18) # y축 라벨 크기
plt.rc("xtick", labelsize=18) # x축 라벨 크기
plt.style.use("fivethirtyeight")
all_unknown_merge.plot.barh(figsize=(15,8))
plt.show()





