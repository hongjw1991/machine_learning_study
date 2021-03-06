
## Currying 복습
>###    1. 익명함수
>###    2. partial
        - partial을 이용시 순서대로 값을 넣으면 각각의 parameter에 자동으로 바인딩 됨
        - 만약 y=3과 같이 keyword를 이용해서 값을 지정하면 해당 키워드만 바인딩 됨

# Numpy 이어서
===============================

## Sorting
>###    1. 정렬
        - sort메서드를 이용해 정렬 가능
        - 원본은 정렬되지 않음. 즉, 원본에 영향 없음.
## 집합 함수(Unique and other set logic)
>###    1. 집합 함수
        - 집합연산이 numpy에 의해 제공됨
        * np.unique는 배열 내 중복 원소를 제거하고 남은 원소를 정렬함.
            - 알고리즘의 단순성을 위해서 원소를 정렬하고 중복 원소 제거함.
        - np.in1d는 2개의 배열을 인자로 받고 첫 번째 배열의 각 원소가 두 번째 배열의 원소를 포함하는지를 나타내는 불리언 배열 반환
        - intersect1d(x, y) : 배열 x, y에 공통적으로 존재하는 원소 정렬해 반환
        - union1d(x, y) : 두 배열 합집합 반환
        - setdiff1d(x, y) : 두 배열 차집합 반환
        - setxor1d(x, y) : 한 배열에는 포함하나 두 배열 모두에는 포함되지 않는 원소의 집합인 대칭자집합 반환
## 배열의 파일 입출력
    - Numpy는 디스크에서 텍스트/바이너리 형식의 파일부터 데이터를 불러오거나 저장 가능
>###    1. 배열 바이너리 형식 디스크 저장
        1. 바이너리 형식 저장
            - np.save : 배열 데이터 효과적으로 디스크에 저장
            - np.load : 불러옴.
            - np.savez : 압축하여 저장
                - npz형식의 파일은 각각의 배열을 언제든 읽을 수 있도록 사전 형식의 객체에 저장함.
>###    2. 텍스트 파일 불러오기 및 저장하기
        1. 불러오기
            - 일반적으로 pandas에서 제공하는 함수 사용
            - np.loadtxt함수 사용
        2. 저장
            - np.savetxt함수 사용
## 선형대수
>###    1. 행렬 연산
        1. 곱셈
            - np.dox(x, y) 혹은 x.dot(y) 함수 사용
            - T는 전치행렬을 구함
            - inv함수는 역행렬 구함
        2. 자주 사용하는 numpy.linalg함수
            - numpy.diag : 정사각 행렬의 대각, 비대각 원소를 1차원 배열로 반환하거나 1차원 배열을 대각선 원소로 하고 나머지는 0으로 채운 단위 행렬 반환
            - numpy.dot : 행렬 곱셈
            - numpy.trace : 행렬 대각 원소의 합 계싼
            - numpy.linalg.det : 행렬식 계산
            - numpy.linalg.eig : 정사각 행렬의 고유 값, 고유 벡터 계산
            - numpy.linalg.inv : 정사각 행렬의 역행렬
            - numpy.linalg.pinv : 행렬의 무어-펜로즈 유사역원 역행렬 구함
            - numpy.linalg.qr : QR 분해
            - numpy.linalg.svd : 특이값 분해 계산(머신러닝에서 사용)
            - numpy.linalg.solve : A가 정사각 행렬 시, Ax = b를 만족하는 x값 구함
            - numpy.linalg.lstsq : y=xb만족하는 최소제곱해를 구함
## 난수생성
>###    1. numpy.random 모듈
        1. normal
            - 표준정규분포로부터 일정 크기의 표본 생성 가능
        2. 내장모듈 random
            - 이 모듈과 numpy의 모듈을 비교하면 시간차가 매우 큰 것을 알 수 있다.
            - numpy가 수십 배 이상 빠름.
        * %timeit 
            - 임의의 문장을 수행하고 매우 정확한 평균 수행 시간을 반환
            - 이런 함수처럼 profiling을 할 수 있는 툴을 다 제공한다. 프로그램의 최적화 수준, 성능 수준을 고려할 때 사용할 수 있다.
            - 프로파일링에 관련해선 교재 102페이지 참조
        3. numpy.random모듈의 함수
            - seed : 난수 발생기의 시드 생성
            - shuffle : 리스트, 배열 순서 뒤섞음
            - permutation : 순서를 임의로 바꾸거나 임의의 순열 반환
            - rand : 균등분포에서 표본 추출
            - randint : 주어진 최소/최대 범위에서 임의의 난수 추출
            - randn : 표준편차1, 평균 0인 정규분포에서 표본 추출
            - ...
## 계단오르기 예제
>###    1. 계단오르기
        - 배열연산의 활용을 보여줄 수 있는 간단한 애플리케이션임.
        
        
        
# 고급 Numpy        
=====================================================

## 배열 재형성
>###    1. 배열 재형성
        - reshape 함수를 통해 shape를 변경할 수 있다.
        - 변경할 크기는 list형태로 주어질 수도 있지만 일반적으로 tuple사용
        - reshape를 하더라도 기존 원본은 변경하지 않음
        - 특정 ndarray배열을 넣게 되면 해당 parameter로 받은 배열의 크기로 reshape
>###    2. 평탄화
        - ravel, flatten함수 사용해서 낮은 차원 반환
        - ravel은 원본을 사용하며
        - flatten은 데이터 복사본 사용
## C와 Fortran순서
        - Numpy는 메모리 상의 데이터 배치에 대한 유연하고 다양한 제어 기능 제공
        - 기본적으로 Numpy는 로우 우선순위로 생성됨.
        - 2차원 배열이 있다면 배열의 각 로우에 해당하는 데이터들은 공간적으로 인접한 메모리에 적재됨/
>###    1. C
        - 로우 우선순위
        - 상위 차원 우선 탐색(1번 축이 0번 축에 우선)
>###    2. Fortran
        - 컬럼 우선순위
        - 상위 차원 나중 탐색(0번 축이 1번 축에 우선)
## 배열 이어붙이고 나누기
>###    1. concatenate
        - 좀 더 많은 기능이 있음.
>###    2. hstack, vstack
        - 단순 이어붙이기인 경우 이 함수를 사용하는 것이 편함.
>###    3. 쌓기
        - r_, c_를 이용해 배열 쌓기를 편하게 할 수 있음.
        - r_는 로우를 기준으로 쌓고
        - c_는 컬럼 기준으로 쌓음.
## 원소 반복
>###    1. repeat
>###    2. tile
## 브로드캐스팅
>###    1. 개념
        - 다른 모양의 배열 간 산술연산 수행방법에 대한 설명
        * 규칙(순서)
            1. 차원이 적은 쪽의 차원을 추가(새로 추가되는 차원 크기는 1)
                - 만약 ndarray와 scalar의 곱셈을 하는 경우 : 스칼라의 차원을 ndarray객체에 맞춰서 곱셈
                - 2차원배열 * 1차원배열 : 1차원 배열이 차원이 작으므로 즉시 연산이 안됨. 따라서 차원을 추가해서 2차원으로 만든 다음 연산함.
            2. 크기가 1인 차원은 매칭되는 상대 차원의 크기와 일치시킴(복사)
                - 3*2 행렬의 배열에 [10, 20] 1차원 배열을 곱하는 경우 : [10, 20]을 그대로 복사해서 3*2 형태로 만들어 줌.
            ex)
                [[1, 2], [3, 4], [5, 6]]의 3*2 크기의 2차원 배열에 [10, 20]인 크기2의 1차원 배열을 곱한다면?
                    - 우선 dimension을 맞춘다. 따라서 [10, 20]의 차원을 추가한다. 추가되는 차원의 크기는 1
                    - 따라서 [[10, 20]]이 된다.
                    - 크기가 1인 차원 즉, 2차원의 새로 추가된 크기가 1이므로 그 크기를 변경
                    - 1 * 2의 크기가 되었다. 크기를 변경해서 3 * 2로 만들어 준다. 그리고 연산
                    
            ex)
                [[1, 2], [3, 4], [5, 6]]의 3*2 크기의 2차원 배열에 스칼라 4의 0차원 수를 곱한다.
                    - 스칼라에 차원을 추가한다. 1차원이 됨 - [4]
                    - 크기가 1인 차원은 상대 차원의 크기 즉, 3*2와 맞추어 주어야한다.
                    --> [[4, 4], [4, 4], [4, 4]]가 된다.
                
>###    2. 브로드캐스팅을 이용해 값 대입
        - 규칙이용해서 배열을 슬라이싱 하여 값을 대입시킬 수 있다.