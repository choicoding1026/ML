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
'''

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import tree
import matplotlib.pyplot as plt

# 1. 데이터 셋
iris_data = load_iris()

# 2. 데이터 분리(학습 데이터와 예측 데이터)
x_train, x_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target, test_size=0.2)
print(len(iris_data.data))
print(pd.Series(y_train).value_counts())
print(pd.Series(y_test).value_counts())
print(len(x_train))
print(len(x_test))

# 3. 모델 생성 => decision tree
model = DecisionTreeClassifier(random_state=14, criterion='entropy')

# 4. 데이터 학습: clf.fit(2차원, 1차원))
model.fit(x_train, y_train)

# 5. 예측 수행
pred = model.predict(x_test)

# 6. 평가(정확도): accuracy_score(정답, 예측)
print(format(accuracy_score(y_test, pred)))

# 7. 임의의 데이터로 예측
user_pred = model.predict([[4.9, 3.3, 1.7, 0.5], [5.5, 2.4, 3.8, 1.1]])
print(user_pred)
print(iris_data.target_names[user_pred])

# 8. 시각화
tree.plot_tree(model.fit(x_train,y_train))
plt.show()