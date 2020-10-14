'''
    outlier
    - 다른 데이터 값 분포와 동 떨어진 값
    - outlier 때문에 데이터가 왜곡된다

    검출방법
    - IQR(사분위 범위): sorted() -> np.percentile()
    - Binning(범위를 지정)
        ex) 중학교 2학년 학생들의 키 값
            키: 167,156,162,174,154...230
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. 사분위
m = np.array([18,5,10,26,-50,45,34,0,3,8,5,9,23,7,-92,41,12,-23])

print(sorted(m))
print(np.percentile(m,25))
print(np.percentile(m,50)) # 중앙값
print(np.percentile(m,75))
print(np.percentile(m,75)-np.percentile(m,25)) # IQR

# 시각화
df = pd.DataFrame(m, columns=['value'])
df.boxplot(column=['value'])
plt.show()

