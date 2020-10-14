'''
    분류(classification)

    1. 결정트리(decision tree)
    2. SVM(Support Vector Machine)
    3. kNN(k Nearest Neighbors)
        1) 임의의 값과 가장 가까운 k(2n-1)개를 선택해서 빈도 수가 많은 label로 분류하는 알고리즘
        2) 학습 불필요
        3) k = 2n-1
        4) 거리 측정 알고리즘 기반으로 동작(단위가 중요) => 표준화
'''

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from collections import Counter
import matplotlib.pyplot as plt

# 1. 데이터 얻기
iris_data = load_iris()

# 2. 두 개의 데이터로 전처리
features = iris_data.data[:100,:2]
target = iris_data.target[:100]
print(features.shape)
print(target.shape)

# 3. 표준화
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# 4. 데이터 분리
x_train, x_test, y_train, y_test = train_test_split(scaled_features,target,test_size=0.2, random_state=12)

# 5. 모델 생성
model = KNeighborsClassifier(n_neighbors=5)

# 6. 임의의 파라미터 생성
params = {
    'n_neighbors':range(1,11),
    'weights':['uniform','distance'],
    'metric':['minkowski','euclidean','manhattan']
}
gs = GridSearchCV(model, param_grid=params, cv=3, n_jobs=-1) # n_job: 실행되는 PC의 프로세서
gs_result = gs.fit(scaled_features, target)
print(gs_result.best_params_)
print(gs_result.best_score_)