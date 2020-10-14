'''
    분류(classification)

    1. 결정트리(decision tree)
    2. SVM(Support Vector Machine)
    3. kNN(k Nearest Neighbors)
    4. essemble
        1) 여러 개의 classifier
        2) 종류
            (1) voting
                - 하나의 데이터 셋에서 여러 개의 서로 다른 classifier 이용
            (2) bagging
                - 여러 샘플 데이터 셋에서 하나의 classifier 이용(랜덤 포레스트 모델)
                - 동시에 실행
                - 결정트리 기반
            (3) boosting
                - 여러 샘플 데이터 셋에서 하나의 classifier 이용
                - 순차적으로 실행
                - 앞의 classifier에서 틀린 데이터에 대한 예측은 다음 classifier에서 가중치를 부여하면서
                    학습과 예측을 순차적으로 진행한다.
                - 결정트리 기반
'''

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression # 분류 알고리즘
from sklearn.naive_bayes import GaussianNB # 나이브 베이즈

# 1. 데이터 셋
iris_data = load_iris()

# 2. 데이터 분리(학습 데이터와 예측 데이터)
x_train, x_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target, test_size=0.2, random_state=12)

# 3. 서로 다른 classifier 설정
cf1 = LogisticRegression(max_iter=1000, C=0.03)
cf2 = RandomForestClassifier(n_estimators=30, max_depth=2, min_samples_split=4)
cf3 = GaussianNB()
cf4 = KNeighborsClassifier(n_neighbors=8)

# 4. ensemble
encf = VotingClassifier(estimators=[('log',cf1),('ran',cf2),('gau',cf3)], voting="soft")

# 5. 학습 및 예측
encf.fit(x_train, y_train)

pred = encf.predict(x_test)
print(pred)

# 6. 정확도
print(accuracy_score(y_test, pred))

# 반드시 ensemble 모델이 예측 정확도가 높은 것은 아니다. 과적합 방지 기능
# ensemble 방법은 kaggle 사이트 경연대회에서 top 차지

classifiers = [cf1,cf2,cf3,cf4,encf]
for x_classifier in classifiers:
    x_classifier.fit(x_train,y_train)
    pred = x_classifier.predict(x_test)
    classifier_name = x_classifier.__class__.__name__
    print(classifier_name, accuracy_score(y_test,pred))