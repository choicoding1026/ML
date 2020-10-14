import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV

# 1. 데이터 셋
iris_data = load_iris()

# 2. 데이터 분리(학습 데이터와 예측 데이터)
x_train, x_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target, test_size=0.2)

# 3. 모델 생성 => decision tree
model = DecisionTreeClassifier(random_state=14, criterion='entropy')

# 4. 최적의 파라미터 추천
parameter = {'max_depth':[1,2,3], 'min_samples_split':[2,3,4]}
grid_CV = GridSearchCV(model, param_grid=parameter, cv=3) # cv: cross validation(교차검증)

grid_CV.fit(x_train, y_train)

print(grid_CV.best_params_) # {'max_depth': 2, 'min_samples_split': 2}
print(grid_CV.best_score_) # 0.9333333333333332