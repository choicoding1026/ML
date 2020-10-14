'''
    * 교차 검증 ( cross validataion)

    머신러닝 적용 순서
    1) 수집된 데이터 전처리
      ==> 이상치 검출, 불균형한 클래스 처리(up,down, class_wight 파라미터이용한 가중치 적용),
          범주형 데이터 ===> 수치로 변환( 사이킷런은 수치만 분석 가능 )
                           LabelEncoder, OneHotEncoder
          단위가 다른 값비교 ==> 표준화 필요(스케일링 필요)
                            StandardScaler ( 평균:0, 분산:1 )
                            RobustScaler ( 중앙값:0, IQR:1 )
                            MinMaxScaler ( 최소값:0, 최대값:1 )

    2) 수집된 전체 데이터 ==> 학습 데이터와 테스트 데이터로 분리 ( 8:2 )
      분리목적: 학습 데이터로 테스트하면 과적합(overfitting) 발생하기 때문에
           학습 데이터가 아닌 임의의 데이터로 테스트 할 목적이다.
            ( 테스트 데이터 1 개이기 때문에 한번만 검증된다. )

    3) 교차 검증 ( cross validation )
     ==> 2)에서 분리된 학습 데이터를 내부적으로 폴드(fold) 갯수만큼 분리하여
     자체적으로 폴드 갯수만큼 검증 처리하는 방법
     ==> cross_val_score 함수 적용
     ==> -grid_CV = GridSearchCV(model, param_grid=parameter,
            cv=3) # cv(교차검증, Cross validation)


'''

import  numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
# 1. 데이터셋 가져오기
iris_data = load_iris()

# 2. 데이터 분리 ( 학습 데이터 와 예측 데이터 분리 )
##############################################
x_train,x_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target,
                                                   test_size=0.2, random_state=42)
# 3. 모델 생성
model = DecisionTreeClassifier(random_state=42)
# 4. 모델 학습
model.fit(x_train, y_train)  # 120
# 5. 예측 수행
pred = model.predict(x_test) # 30
# 6. 평가 ( 정확도 ) => accuracy_score(정답, 예측값) , 백분율로
print("예측 정확도: {}".format(accuracy_score(y_test, pred))) #오버피팅 발생 가능성 매우 높다
#############################################################
from sklearn.model_selection import cross_val_score
# 교차 검증
cv_score = cross_val_score(model, x_train, y_train, cv=2)  # k폴드
print("교차 검증별 정확도: ", cv_score ) # [0.91666667 0.93333333]
print("교차 검증별 정확도 평균: ", np.round(np.mean(cv_score), 4) ) # 0.925