'''
    data

    가. 범주형 자료: 질적 자료, 정성적
         - 명목형(nominal data)
            : 숫자로 바꾸어도 그 값이 크고 작음을 나타내는 것이 아니라
            단순히 범주를 표시 ( 예>  혈액형, 성별(주민번호)=> 남:1 여:2 )
         - 순서형(ordinal data)
            : 범주의 순서가 상대적으로 비교 가능
              ( 예> 비만도(저체중-0,정상-1,과체중-2,비만-3,고도비만-4) )

    나. 수치형 자료: 양적 자료, 정량적
        - 이산형(discrete data)
            : 셀수 있는 데이터  예> 멤버의 수, 코로나 확진자 수 등...
        - 연속형(continuous data)
            : 셀 수 없는, 연속적인 속성을 갖는 데이터  예> 키, 체중

    * 척도(scale)
     ==> 사람이나 사물과 같은 관측대상의 특성을 수량화하기 위한 방법
     가. 질적 척도
         - 명목척도: 분류 목적. 숫자 자체의 값 의미 없다. ( 남:1 여:2 )
         - 서열척도: 서열이 가능 ( 비만도(저체중-0,정상-1,과체중-2,비만-3,고도비만-4), 랭크:1등,2등 )

     나. 양적 척도
         - 등간척도: 상대적 크기로 나타냄. ( A: 5점, B: 4점 , C: 3점, F: 0점 )
         - 비율척도: 등간척도 + 연산이 가능

     ===> 관측된 데이터를 인코딩(Encoding)방법을 사용하여 수량화한다.
         - LabelEncoder
         - OneHotEncoder
'''

import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# 1. 순서없는 범주형 데이터
items =['TV', '냉장고','믹서','전자레인지','컴퓨터','선풍기','선풍기','믹서']

# 2. DataFrame 변경
df = pd.DataFrame({"상품":items})
print(df)

# 3. OneHotEncoder 생성 및 변환
encoder = OneHotEncoder()
encoder.fit(df)
encoded_labels = encoder.transform(df)
# 4. 변환값 출력
print("OneHotEncoder 변환된 데이터:{}".format(encoded_labels.toarray()))
# [[1. 0. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0. 0.]
#  [0. 0. 1. 0. 0. 0.]
#  [0. 0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 0. 1.]
#  [0. 0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0. 0.]
#  [0. 0. 1. 0. 0. 0.]]
print("원본 범주형 데이터 변수명:{}".format(encoder.get_feature_names()))
# ['x0_TV' 'x0_냉장고' 'x0_믹서' 'x0_선풍기' 'x0_전자레인지' 'x0_컴퓨터']
