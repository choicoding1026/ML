'''
    * 불균형한 데이터 처리 방법
   1) 더 많은 데이터를 수집 (*****)
   2) 가중치를 적용
   3) 클래스 갯수를 맞춘다.
      - 다운 샘플링
      - 업 샘플링
'''

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
features = iris.data
target = iris.target

# 150 개 ==> 40개 삭제 ==> 110개 를 0값의 100개, 1값의 10개

# 1. 40개 삭제
features  = features[40:, :]
target = target[40:]

# 2. 110개 ==>  0과 1로 값 변경
target = np.where((target==0),0, 1)
print(target)


# 3. 인덱스 추출
i_class0 = np.where(target==0)[0]
i_class1 = np.where(target==1)[0]
print(i_class0)
print(i_class1)

# 샘플 갯수
n_class0 = len(i_class0)
n_class1 = len(i_class1)

# 4. 클래스0의 갯수만큼 클래스1에서 랜덤하게 샘플 추출
i_class1_down_sampled = \
np.random.choice(i_class1, size=n_class0, replace=False)
print(i_class1_down_sampled)

# 5. 클래스0의 target과 다운샘플링된 클래스1의 target 병합
target = np.hstack((target[i_class0], target[i_class1_down_sampled]))
print(target)
print(target.shape) # (20,)

features = np.vstack(   (features[i_class0, :] , features[i_class1_down_sampled,:])   )
print(features)
print(features.shape)  # (20, 4)


