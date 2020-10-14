'''
    feature scaling 정규화
        1) 서로 다른 데이터 값 범위를 일정한 수준으로 맞추는 작업
        2) scikit-learn standardScaler class
            => N(0,1) 평균이 0이고 분산이 1인 데이터로 변환
'''

import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import MinMaxScaler

cancer = load_breast_cancer()

x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.2, random_state=14)

scaler = MinMaxScaler()
scaler_df = scaler.fit_transform(x_train)

print(np.median(x_train.min(axis=0)))
print(np.median(x_train.max(axis=0)))
print(np.median(scaler_df.min(axis=0)))
print(np.median(scaler_df.max(axis=0)))
