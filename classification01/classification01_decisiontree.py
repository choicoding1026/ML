'''
    분류(classification)

    1. 결정트리(decision tree)
'''

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

# 1. 데이터 셋
iris_data = load_iris()
print(type(iris_data)) # <class 'sklearn.utils.Bunch'>
'''
    scikit-learn에서 제공하는 모든 데이터 구조는 동일
    {'data':2차원 배열, 'target':1차원 배열, 'frame':None, 'target_names':1차원배열, 'DESCR':정보}
    print(iris_data)
    {'data': 학습할 꽃의 데이터 [꽃받침 길이, 꽃받침 넓이, 꽃잎 길이, 꽃잎 넓이], 'target': 꽃의 종류 ..}
'''
print(iris_data.data)
print(iris_data.feature_names)
print(iris_data.target)
print(iris_data.target_names)
print(iris_data.frame)
print(iris_data.DESCR)

# 2. 데이터 셋을 DataFrame으로 변경
iris_df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
iris_df['target'] = iris_data.target
iris_df['target_names'] = iris_data.target_names[iris_data.target]
print(iris_df)
print(iris_df.info())
print(iris_df.describe())

# 3. 수집된 데이터로 만든 DataFrame을 활용해 ML에 적용