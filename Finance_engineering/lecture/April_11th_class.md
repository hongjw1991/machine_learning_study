## 1. 시계열 데이터 분석
>###    1. 시계열 자료 분석 목적
        1. 자료의 기술
            - 주어진 시계열 자료의 생성구조를 이해, 기술
        2. 예측
            - 현재까지 관측된 값들로부터 미래의 값 예측
        3. 제어
            - 생성된 시스템 제어
>###    2. 분해법
        - 시계열 기본 변동성 성분
        1. 성분종류
            1. 추세성분(Tt)
                - 시간이 경과함에 따라 증가 / 감소하는 추세를 갖고 움직이는 장기적 변동
            2. 계절성분(St)
                - 일정 주기를 갖고 규칙적으로 반복되는 변동, 보통 1년 이내의 주기적 변동
            3. 순환성분(Ct)
                - 계절성분과 유사, 변화 주기가 장기간일 때의 변동. 경기변동이라 부름. 주기 일정치 않음
            4. 불규칙성분(It)
                - 시간에 무관하게 임의의 원인에 의해 나타나는 변동. 예측 불가
        2. 분해모형
            1. 가법모형
                - 각 성분을 모두 더해서 구함.
            2. 승법모형
                - 각 성분을 모두 곱해서 구함.
                - 변화가 큰 경우 주로 사용.
        3. 정상성(Stationary)
            - 어디에서 살펴보더라도 같은 성질을 가지는 것으로 가정
            - 시계열의 수준과 분산에 체계적인 변화가 없고 엄밀하게 주기적 변화가 없다는 의미
            - 미래는 확률적으로 과거와 동일
            - 정상성을 가지지 않는 자료를 분석할 때는 신뢰도가 떨어지게 된다.
            Yt - 관측된 시계열
            1. 평균이 시간 t에 무관하게 일정
                - E(Yt) = μ_t = μ
            2. 분산이 시간 t에 무관하게 일정
                - Var(Yt) = σ_t = σ
            3. 강한 정상성
                - Yt1 --- Ytn 의 결합확률밀도함수 
            4. 약한 정상성
                앞의 두 가지 조건을 만족하고 공분산이 시간 t에 의존치 않고 오직 시차에만 의존
                - Cov(Yt, Yt_t+k) = Y_k
                - 즉, 시간의 차이에만 의존함.
        4. 시계열 가격과 수익률(주식 예시)
            - 일반적으로 수익률 자료는 정상성을 따름
            - 수익률 계산
                * 단순수익률
                    R = (P_t - P_0) / P_0 * 100
                * 복리수익률
                    R = log((P_t - P_0) / P_0) * 100
                    이자도 재투자된다고 고려함.
            - Value-at-Risk
                * 정상적인 시장 여건 하에서 일정기간 동안 발생할 수 있는 최대 손실금액
>###    3. 선형 시계열 모델과 예측
        1. 선형 시계열 모델
            - 자기 회귀 누적 이동 평균(ARIMA)
            - Box-Jenkins에 의해 제안됨.
            - 현재 값이 오직 과거 자신의 시계열 데이터 값이나 과거 오차 값에만 의존한다고 가정
            - 시계열 자료가 약한 정상성을 가지고 등간격으로 수집된 자료수가 충분해야 함(보통 50개 이상, 성분이 있으면 100개 이상 주장)
        2. 백색잡음과정(White noise process)
            - 잔차간 선형의존성이 있는지 검정(즉, 잔차끼리 관련이 있는지)
            - Y_t = a_t
            - a_t ~ N(0, σ^2), 독립 
            --> 강한 정상성을 갖는다.(정규분포를 따르기 때문)
        3. 자기상관함수(ACF)
            - 정상시계열의 자기공분산
            - Y_k = Cov(Y_t, Y_t+k) = E(Y_t - μ)E(Y_t+k - μ)
                    = E(Y_t+k - μ)E(Y_t - μ) = Y_-k
                * 즉, 기간의 공분산에 의존, 전기, 후기로의 이동 방향에 상관없이 기간 사이의 공분산이 일정
            - k차 자기상관계수(ρ_k)
            - 자기상관도표
                * 시차가 자기자신과 0 이면 자기자신과 일치. 상관관계 1, 그 외 시차의 경우에는 관계가 있을 수 있으나 1은 아님.
                * 만약 시차가 0이 아닐 때, 자기 상관이 0에 가까우면 자기자신과 상관이 없다고 판단할 수 있다.
        4. 편자기상관함수(PACF)
            - 정상계열 Y_t의 시차k의 자기상관계수
            - Y_t-1, --- , T_t-k+1의 성분제거
            - 시차가 t와 t-k사이일 때만 확인함. 나머지 시차에 대해서는 성분 제거
            - 예시
                * Y_t = φ_11Y_t-1 + a_t모형(전기에만 영향을 주는 모형), E(Y_t) =0, a_t와 Y_t-j가정
                * Corr(Y_t,Y_t-2 | Y_t-1) = ρ_02*1 = 0
                --> Y_t-1성분을 제거한 후 Y_t와 Y_t-2는 관련이 없음.
                -- 1기 차이는 상관이 있을 것. 2기는 없음.
        5. ARIMA모델 구성 절차
            1. 모델 판별
                - 모델의 order값(현재 값에 영향 주는 과거 값 또는 오차값의 개수)를 그래프나 정보 기준값을 통해 탐색하는 과정 포함
                - 실제 자료에 따라서는 1기 이전만이 아니고 2기 혹은 그 이전의 자료도 영향을 줄 수 있음.
                - 따라서 어디까지가 영향을 주는지 판단해야 함.
            2. 모델 추정
                - Order값이 정해지고 skuas 일반 모델의 모수 값들을 일반적으로 최소제곱법, 최대 우도 추정 방법으로 추정
                
            3. 모델 적합성 판단
                - 잔차가 백색 잡음을 따르는지 검정(잔차간의 선형의존성이 없음을 의미)
        6. 모델 판별
            - 정보기준값 : 더 적절한 모형 선택 기준 제시
            1. AIC : 두 개 이상의 모델이 있을 때 수치가 더 낮을 수록 좋은 모델
                - 자기 공선성의 패널티를 약하게 줌.
            2. BIC : 두 개 이상의 모델이 있을 때 수치가 더 낮을 수록 좋은 모델
                - 자기 공선성의 패널티를 강하게 줌.
        7. 모델 추정
            - 자기회귀 모형(AR:AutoRegressive)
            - Y_t = φ_1 * Y_t-1 + --- + φ_p * Y_t-p + a_t
            - 최소제곱법, 최대 우도 추정법
            - AR(1) 모형
                * Y_t = φ_1 * Y_t-1 + a_t, -1 < φ < 1
                * 정상성을 가질 필요충분조건 : -1 < φ < 1
                * 만약 해당 값을 벗어날 경우 분산 가정이 충족되지 않음
                * ACF(자기상관)
                    - 처음에는 상관계수가 높더라도 k기가 지나가면서 k제곱 되면서 점점 상관계수가 낮아짐. (tail-off모형)
                * PACF(편자기상관)
                    - 처음에만 상관있고, 나머지는 무관(cut off)
            - AR(2) 모형
                * Y_t = φ_1Y_t-1 + φ_2Y_t-2 + a_t
                * 정상성 필충조건
                    1. φ_1 + φ_2 < 1
                    2. φ_1 - φ_2 < 1
                    3. -1 < φ_2 < 1
                * ACF
                    - φ_k / (1- φ_k)
                    - k>=1 이상에서 모두 동일 적용
                * PACF
                    - φ_1 / (1-φ_2) : (k=1)
                    - φ_2 : (k=2)
                    - 0 : (k>=3)
        8. 모델 정확도
            1. Mean Error : ME(평균오차)
            2. Mean Absolute Error : MAE(평균 절대 오차)
            3. MSE(평균 제곱 오차)
            4. SDE(오차의 표준편차)
            5. PE(오차의 백분율)
            6. MPE(오차 백분율 평균)
            7. MAPE(절대 백분율 오차 평균)
        9. 적합성 검정
            - 자기상관함수
            - 잔차가 백색잡음을 따르는지 확인
            - 변동성 클러스터 : 변동성 사이에 클러스터링(운집) 되어 있는 경우 관계가 있는지 없는지 확인
            - 자기상관의 Ljung-Box 테스트
>###    4. 공적분
        1. 정의
            - 그랜저 앵글에 의해서 공식화
            - 둘 이상의 비정상 시계열을 선형 결합했을 때 그 결과가 정상성 시계열을 따르는 경우
            - 즉, 비정상성 시계열들의 관계가 장기적으로는 안정적인 추세를 따르는 경우
            * 비정상 시계열
                - 시간이 경과함에 따라 시계열의 관측값이 증가하거나 감소
                - 분산이 변하는 경우
                - 시계열 수준이 변함과 동시에 분산이 변하는 경우
                1. 평균이 일정하지 않은 경우
                    1) 결정적 추세
                        - 추세가 시간함수로 결정적이고 영원히 지속되는 것
                        - Y_t = μ_t + a_t,
                        - μ_t = a_0 + a_1*t
                    2) 확률적 추세
                        - 인접한 자료들 간에 강한 양의 상관관계 때문에 어떤 추세가 있는 것처럼 보이는 경우
                        - 미리 정해진 형태가 아니라 자료들 간의 확률적 구조로 인해 생기는 추세
                        * 확률보행모형(Randomwalk) : 확률적 추세를 가진 가장 단순한 모형
                            - Y_t = Y_t-1 + a_t : a_t = 백색잡음과정
                            - 내일의 시계열 값 = 오늘의 시계열 값 + 예측할 수 없는 변화량
                            - E(Y_t|Y_t-1,...) = Y_t-1 : 최적의 예측값은 바로 현재값
                            - Var(Y_t) = Var(Y_t-1) + Var(a_t) : 분산이 시간에 의존
                        * 절편이 있는 확률보행모형
                            - Y_t = θ + Y_t-1 + a_t, a_t :백색잡음과정
                            - 평균과 분산 모두 t의 함수
                            - 보통 θ는 매우 작지만 조금만 크게 되면 Y_t는 θ의 지배를 받음.
                        * 확률적 추세와 단위근
                            * AR(1) 모형
                                - Y_t = θ + φY_t-1 + a_t
                                - 확률보행모형 : AR(1) 에서 φ=1인 특수한 경우
                                - Y_t는 확률적 추세를 가지고 있으며 비정상적
                            * AR(P) 모형
                                - 근이 1인 것을 가지고 있으면 단위근을 가지고 있다고 판단
                                - 단위근을 가지고 있는 경우 Y_t는 확률적 추세를 포함
                                - 확률적 추세와 단위근을 동일한 용어로 사용
                        * 단위근이 있는 경우 문제점
                            - 확률적 추세를 지는 AR모형을 정상 AR모형으로 추정된 최소제곱추정량은 편의 되고 대표본하에서 조차 추정량의 극한분포가 정규분포를 따르지 않아 이에 근거한 검정통계량 신뢰 불가 
                            - 따라서 다른 기준으로 평가(tau)
                            - 단위근을 가지는 서로 독립인 두개의 비정상 시계열이 서로 연관되어 있는 것처럼 보이게 만들어 허구적 회귀를 야기시킴
                2. 분산이 일정하지 않은 경우
                    - 많은 경제 관련 시계열 자료가 시간이 경과함에 따라 관측값이 커지고 변동폭도 커지는 경향
                    - 분산안정화 : 변수변환을 통해 시간에 관계없이 분산이 일정토록 만듦
        2. 비정상성 검정 : 단위근 검정(unit root test = Dickey-Fuller test)
            1. 상수항이 없고 추세가 없는 경우
            2. 상수항은 있으나 추세가 없는 경우
            3. 상수항이 있고 추세가 있는 경우
            4. 귀무가설 : ρ = 1 / 대립가설 : ρ < 1
            5. tau : 임계치를 의미함. 검정 통계량이 임계치보다 더 작은 값이 나오면 귀무가설 기각
        3. 적분차수
            - Y_t = Y_t-1 + a_t : 확률 보행
            - 1차 차분 : ∆Y_t = Y_t - Y_t-1
            - 독립적, (0, σ^2)
            - I(1) : 1차 차분을 취함으로써 안정적이 되는 시계열
            - I(0) : 안정적 시계열 -> 일반적으로 누적 차수는 해당 시계열을 안정적으로 만들기 위해 차분되어져야 하는 숫자
        4. 공적분
            - 두 변수가 I(1)일 때 두 변수의 1차 결합식이 I(0)이 되는 경우
            - Y_t = Y_t-1 + u_t
            - X_t = X_t-1 + v_t
            - 선형결합함수 Y_t - θX_t이 I(0)가 되게 하는 공적분계수 θ
        5. 오차수정모형(ECM)
            - X_t, Y_t 의 1차 차분은 Y_t - θX_t을 추가적인 설명변수로 포함시킨 벡터 자기회귀모형으로 모형화
            - Y_t-1-θX_t-1은 시점 t-1에서 두 시계열의 불균형오차를 나타내며 오차가 조정계수 a를 통해 그 크기가 조정된 후 다음 시점 t에 영향을 줌
            - 각 차분이 자신들의 과거에 영향을 받을 뿐 아니라 두 변수 사이의 불균형오차의 정도에도 영향을 받는다는 의미에서 오차수정모형
            - 단기적으로는 불안정적일 수 있지만, 장기적으로는 안정적임을 증명해주는 모형.
        6. 헤지
            - 헤지 : 환율, 금리 또는 다른 자산에 대한 투자 등을 통해 보유하고 있는 위험자산에 대해 가격변동을 제거하는 것으로 주로 선물 옵션과 같은 파생상품 이용
            - 최적헤지비율 : 위험을 최소화시키기 위해 취한 선물의 규모의 비율을 현물가격의 변동 크기를 선물 가격의 변동 크기로 나누어준 수치
    
        7. 자기회귀조건부 이분산 모형
            - ARIMA 모형에서 잔차의 분산이 균일하다는 전제에서 모형 구성
            - 금융시계열에서는 위험과 불확성의 증가로 인해 분산과 공분산이 시간에 따라 변하는 경우가 많이 발생
            - 실제 시계열 자료에서는 무작위로 일정한 범위로 벗어나는 경우가 발생하며 분산이 불균일하게 됨.
            * Volatility clustering
                - 어떤 외적 요인에 의해 순간적으로 시계열에 큰 값이 생성되면 이 값은 그 시계열에서 일정기간 동안 계속적으로 변동이 큰 값을 만들어 내는 역할
                - 작은 값이 생성되면 이 값 역시 계속해서 작은 값을 유지시켜 결국 변동이 큰 값끼리 작은 값끼리 집락을 이루는 변동 클러스터링이 시계열에 나타남
>###    5. 변동성 모델
        - 변동성 : 수준이 안정적인 시계열에서 분산이 시간에 따라 변하는 것. 그런 현상의 위험을 설명하고 측정하는 수단이 됨.
        - ARIMA는 변동성 군집을 반영하지 못하여 다른 모형이 필요
        - Volatility clustering에 대한 모형
            1. 자기회귀 조건부 이분산(ARCH)
            2. 일반화 자기회귀 조건부 이분산(GARCH) - 과거 분산도
        1. ARCH모형 - Engle에 의해 도입
            * AR(1)모형과 ARCH(1)모형
                - AR(1) : Y_t = Y_t-1 + a_t
                - ARCH(1) : Y_t = Y_t-1 + a_t, a_t^2 = (a_0 + a_1 * (a_t-1) ^2) * u_t, u_t : white noise
                - a_0값이 1이고 a_1값이 0이면 ARCH는 random walk가 된다.
                - u_t-1이 주어질 때 u_t 조건부 분포
                    - u_t | u_t-1 ~ N(0, a_0 + a_1 * (a_t-1)^2)
                - u_t의 조건부 분포에 따른 조건부 분산은 u_t-1에 따른 함수로 표현되며 이를 조건부 불균일이라 함.
            * VaR(Value-at-Risk)
                - 금융기관들은 VaR을 이용해 자신들의 비즈니스 리스크 측정
                - 일반적으로 VaR은 99% 신뢰수준에서 10 영업일 기준으로 측정
                - 이 기간 동안 1% 확률로 일어날 기대 손실 금액 나타냄
        2. GARCH모형
        3. 리스크 모델 백테스팅
            - 히스토리컬 백테스팅 방법 : 모델 성능을 확인할 수 있는 유용한 검정 방법 중 하나
            - 특정기간 동안 추정된 VaR과 실제 값 비교
            * 순서
            * 결과 검증