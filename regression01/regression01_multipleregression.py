'''
    regression
        1. 여러 개의 독립변수와 한 개의 종속변수 간의 상관관계를 모델링하는 기법
        2. 종류
            1) 단순 회귀(simple regression)
                하나의 종속변수와 하나의 독립변수 사이의 관계 분석
            2) 다중회귀(multiple regression)
                하나의 종속변수와 여러 개의 독립변수 사이의 관계 분석
            3) 선형회귀(linear regression)
                회귀계수가 선형인 경우
            4) 비선형회귀(non-linear regression)
                회귀계수가 비선형인 경우
        3. 목적
            1) 종속변수와 독립변수 간의 선형관계 여부 확인 가능 => 회귀모형
            2) 도출된 회귀모형을 활용해 종속변수의 값을 예측할 수 있다.
'''

import  numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. 데이터 셋 로드
boston = load_boston()

#2. DataFrame 변경
bostonDF = pd.DataFrame(boston.data, columns=boston.feature_names)
# CRIM    ZN  INDUS  CHAS    NOX  ...  RAD    TAX  PTRATIO       B  LSTAT
# 0  0.00632  18.0   2.31   0.0  0.538  ...  1.0  296.0     15.3  396.90   4.98
# 1  0.02731   0.0   7.07   0.0  0.469  ...  2.0  242.0     17.8  396.90   9.14

# bostonDF['price'] = boston.target
# print(bostonDF.head())

# 3. 데이터 분리
x_train,x_test, y_train, y_test = train_test_split(bostonDF, boston.target,
                                                   test_size=0.2, random_state=42)

# 2. 데이터 분리(학습 데이터와 예측 데이터)
x_train, x_test, y_train, y_test = train_test_split(bostonDF, boston.target, test_size=0.2, random_state=12)

model = LinearRegression()
model.fit(x_train, y_train)

print("기울기: ", model.coef_)
print("절편: ", model.intercept_)

pred = model.predict(x_test)
print(pred)

# 회귀식의 평가지표 ==> 결정계수 R2 ( 1에 가까울수록 정확도가 높다 )
mse = mean_squared_error(y_test, pred)
r2_score = r2_score(y_test, pred)

print("mean_squared_error: ", mse)
print("r2_score: ", r2_score)