'''
    분류(classification)

    1. 결정트리(decision tree)
    2. SVM(Support Vector Machine)
        1) 이진 분류에 최적화
        2) 분류 기준은 각 데이터(Support Vector)와 가장 큰 폭의 거리를 찾는 알고리즘
        3) 분류 되는 선을 hyper plane이라고 부른다.
            => 두 개의 데이터를 구분하기 위한 최적의 구분선을 찾는 알고리즘
        4) 사용하는 모델명
            (1) from sklearn.svm import SVC
            (2) from sklearn.svm import LinearSVC(개량종)
'''

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import  accuracy_score
import matplotlib.pyplot as plt

iris_data = load_iris()

features = iris_data.data[:100, :2]
target = iris_data.target[:100]
print(features)
print(target)

scaler = StandardScaler()
iris_scaled = scaler.fit_transform(features)
print(iris_scaled)
print(iris_scaled.mean()) # 0에 근접
print(iris_scaled.var()) # 1에 근접

# 데이터 생성
x_train, x_test, y_train, y_test = train_test_split(iris_scaled, target, test_size=0.2, random_state=14)

# 모델 생성
model = SVC(C=1.0, gamma='scale', kernel='linear', random_state=14)


# 모델 학습
model.fit(x_train, y_train)

# support vector 식별
print(model.support_vectors_)
print(model.n_support_)