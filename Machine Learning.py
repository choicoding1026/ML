'''
    Machine Learning

    1. 개념
        데이터를 이용해서 명시적으로 정의되지 않은 패턴을 컴퓨터로 학습하여 결과(예측)를 만들어 내는 학문 분야(insight)
    2. 중요한 요소
        1) 빅데이터
            (1) 방법
                - 레거시 데이터(기존에 가지고 있는 데이터, 파일, DB ..)
                - 네트워크 상의 임의의 데이터 수집( ex)SNS, Opendata ..)
                    => 크롤링(crawling) => 전처리(가공)
                - scikit-learn에서 제공하는 데이터 셋 활용
                - kaggle
        2) 패턴인식
        3) 연산(컴퓨터 성능)
    3. 종류
        1) 지도 학습(supervised learning)
            (1) 데이터와 정답을 같이 제공
            (2) 종류
                - 분류(classification): 종류 예측
                - 회귀(regression): 값 예측
        2) 비지도 학습(unsupervised learning)
            (1) 데이터만 제공
            (2) 제공된 데이터를 학습해서 패턴을 스스로 찾는 방법
            (3) 종류
                - 군집화
                - 차원축소
    4. 용어
        1) 샘플(sample, data point): 하나의 행
        2) 특성(feature): sample의 속성, 열
        3) 레이블(label): 정답
        4) 분류 모델(classification): python의 class
            (1) 결정트리(decision tree)
            (2) 서포트 백터 머신 SVM(Support Vector Machine)
            (3) kNN(k-Nearest Neighbor)
            (4) 랜덤 포레스트(random forest)
            (5) 로지스틱 회귀(logistic regression)
            (6) 어셈블(assemble): 여러 모델을 함께 적용
        5) 회귀 모델(regression): python의 class
            (1) 선형 회귀(linear regression)
    5. 순서
        1) 데이터 수집(레거시 데이터, 인터넷 상의 데이터 ..)
        2) 크롤링(데이터 전처리) => DataFrame
        3) 데이터 학습(기계에게 학습시킨다)
            (1) 모델 선정(분류/회귀)
            (2) 모델에 데이터 학습
                => 예측 성능을 높이기 위해 모델인 클래스의 속성을 변경시키면서 학습 시킨다.
                => 예측 성능을 향상 시킬 수 있는 특별한 파라미터(Hyper Parameter)
            (3) 모델 평가
                => 평가 방법 제공됨
        4) 임의의 데이터
        5) 정확도 검증 -> 예상과 다르면 3) 데이터 학습부터 다시 반복

    6. 머신러닝의 기본적인 2단계
        1) 학습 단계 ( Training )
        2) 예측 단계 ( predition )
            ==> 학습단계에서 사용했던 데이터와
            예측단계에서 사용했던 데이터는 반드시 서로 분리해야 된다.
            ( 오버피팅(overfitting) 방지 )
            * 오버피팅(overfitting):
            학습된 데이터의 정확도는 높으나 임의의 데이터의 정확도는 낮은 상태를 의미.

    7. ML에서 사용되는 주요 패키지
        1) numpy
            https://numpy.org/
            pip install numpy
        2) pandas
            https://pandas.pydata.org/
            pip install pandas
        3) 시각화
            https://matplotlib.org/
            http://seaborn.pydata.org/
            pip install matplotlib
            pip install seaborn

        4) 사이킷런 ( scikit-learn): ML에 특화된 패키지
            https://scikit-learn.org/stable/
            pip install scikit-learn
            https://scikit-learn.org/stable/tutorial/machine_learning_map/
'''