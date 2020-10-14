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

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# 1. 데이터 셋
iris_data = load_iris()
iris_df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
iris_df['target'] = iris_data.target

# 2. 데이터 분리(학습 데이터와 예측 데이터)
x_train, x_test, y_train, y_test = train_test_split(iris_df, iris_data.target, test_size=0.2, random_state=12)

model = LinearRegression()
model.fit(x_train[['petal width (cm)']], y_train)

print("기울기: ", model.coef_)
print("절편: ", model.intercept_)

pred = model.predict(x_test[['petal width (cm)']])
print(pred)

x=x_test[['petal width (cm)']]
y=1.02010082*x+(-0.20847191165308865)
print(y)

mse = mean_squared_error(y_test, pred)
r2_score = r2_score(y_test, pred)

print("mean_squared_error: ", mse)
print("r2_score: ", r2_score)