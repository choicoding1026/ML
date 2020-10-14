'''
    분류(classification)

    1. 결정트리(decision tree)
    2. 학습 데이터(training data)와 테스트 데이터(test data) 분리
        from sklearn.model_selection import train_test_split
        x_train, x_test, y_train, y_test = train_test_split(2차원, 1차원)
    3. 시각화
        from sklearn import tree
        import matplotlib.pyplot as plt
        tree.plot_tree(model.fit(x_train,y_train))
        plt.show()
    4. feature 중요도
'''

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import tree
import matplotlib.pyplot as plt
import seaborn as sb

# 1. 데이터 셋
iris_data = load_iris()

# 2. 데이터 분리(학습 데이터와 예측 데이터)
x_train, x_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target, test_size=0.2)

# 3. 모델 생성 => decision tree
model = DecisionTreeClassifier(random_state=42)

# 4. 데이터 학습: clf.fit(2차원, 1차원))
model.fit(x_train, y_train)

# DecisionTreeClassifier 클래스 정보
# print(help(DecisionTreeClassifier))
# DecisionTreeClassifier의 Hyper Parameter
# max_depth 트리 최대 깊이, max_features 최대 feature 수, min_sample_split 노드를 분할하기 위한 최소의 샘플 수
print(np.round(model.feature_importances_,2))
# [0.01 0.05 0.55 0.4] = [sepal length, sepal width, petal length, petal width]

# 추가 메서드
print(model.get_depth())
print(model.get_n_leaves())
print(model.get_params())
print(model.decision_path(x_train))
print(model.score(x_test, y_test)) # accuracy_score와 같은 기능