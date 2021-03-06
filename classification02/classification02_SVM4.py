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
        5) parameter
            (1) kernel="linear/Polynomial/Sigmoid/rbf(default)"
                - linear: 데이터를 직선으로 분리
                - rbf: radial basis function(가우시안 커널)
                       곡선으로 분리 가능(현재도 많이 사용) kernel trick(커널 기법)
            (2) C=1.0
                - Cost(비용): 비용이 작으면 분류의 정확도가 떨어짐 -> 곡선 나올 확률이 거의 없다.(직선)
                             비용이 크면 세밀하게 분류 -> 곡선이 나올 확률이 높다.
            (3) gamma
                - hyper plane(초평면,결정경계)의 굴곡에 영향을 주는 데이터의 범위
                - gamma 값이 크면 굴곡이 더 심해지고, 값이 작을 수록 선형에 가까워진다.

            ==> overfitting(과적합)에 영향을 주는 parameter
'''

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
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
# (1) model = SVC(C=1.0, gamma='scale', kernel='linear', random_state=14)
model = LinearSVC(C=1.0, random_state=14)

# 모델 학습
model.fit(x_train, y_train)

# 예측
pred = model.predict(x_test)

# 정확도
print(y_test, pred)
print(accuracy_score(y_test, pred))

# 임의의 값으로 예측
user_pred = model.predict([[-2,3],[13,4]])
print(user_pred)

# 시각화
color = ["green" if c==0 else "orange" for c in target]
plt.scatter(iris_scaled[:,0], iris_scaled[:,1], c= color)
plt.show()