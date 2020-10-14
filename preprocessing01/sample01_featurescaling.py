'''
    feature scaling 정규화
        1) 서로 다른 데이터 값 범위를 일정한 수준으로 맞추는 작업
        2) scikit-learn standardScaler class
            => N(0,1) 평균이 0이고 분산이 1인 데이터로 변환
'''

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

iris_data = load_iris()

# DataFrame 변경
df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)

print(df.mean())
print(df.var())

scaler = StandardScaler()
scaler.fit(df)
iris_scaled = scaler.transform(df)

scaled_df = pd.DataFrame(iris_scaled, columns=iris_data.feature_names)

print(scaled_df.mean())
print(scaled_df.var())