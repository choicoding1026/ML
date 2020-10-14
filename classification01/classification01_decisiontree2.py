'''
    분류(classification)

    1. 결정트리(decision tree)
'''

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. 데이터 셋
iris_data = load_iris()

# 2. 데이터 분리(학습 데이터와 예측 데이터)

# 3. 모델 생성 => decision tree
model = DecisionTreeClassifier()

# 4. 데이터 학습: clf.fit(2차원, 1차원))
model.fit(iris_data.data, iris_data.target)

# 5. 예측 수행
pred = model.predict(iris_data.data)

# 6. 평가(정확도): accuracy_score(정답, 예측)
print(format(accuracy_score(iris_data.target, pred)))
