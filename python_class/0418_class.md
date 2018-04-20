# Numpy
================================
## Numpy start
>###    1. Numpy 시작
        * 기능
            - 빠르고 메모리 효율적으로 사용
            - 벡터 산술연산, 세련된 브로그 캐스팅 기능 제공 -- ndarray
            - 반복문 작성 필요 없이 전체 데이터 배열에 대해 빠른 연산 제공
            - 선형대수, 난수 발생기, 푸리에 변환 가능
            - C, C++, 포트란으로 쓰인 코드 통합
            - 배열 데이터를 디스크에 쓰거나 읽을 수 있는 도구와 메모리에 올려진 파일을 사용하는 도구
        * https://docs.scipy.org/doc/ >> numpy, scipy documentation
>###    2. Numpy ndarray 자료형
        * 교재 120p 참조
>###    3. 배열 생성 함수
        - array : 배열 생성, ndarray타입으로 변환하며 dtype이 명시되지 않은 경우 자료형 추론에 저장
        - asarray : 입력 데이터 ndarray로 변환, 이미 ndarray인 경우 복사 하지 않음
        - arange : 내장 range와 비슷하지만 리스트 대신 ndarray반환
        - ones, ones_like : 내용 전체 1로 초기화하고, 주어진 모양으로 행렬 생성
        - zeros, zeros_like : 내용 전체 0로 초기화하고, 주어진 모양으로 행렬 생성
        - empty, empty_like : 메모리 할당해 새로운 배열 생성, 값 초기화는 하지 않음
        - eye, identity : 단위 행렬 생성
>###    4. 배열과 스칼라 간의 연산
        - 배열은 for 반복문 없이 데이터 일괄처리 가능. --> Vectorization
        - 같은 크기의 배열 간 산술연산은 배열의 각 요소 단위로 적용됨
        - 크기가 다른 배열 간의 연산은 브로드캐스팅이라고 함. 이에 대한 규칙이 있음
        - 스칼라 값과 배열을 연산할 때 브로드캐스팅 룰에 따라 연산됨. 코드 참조
        - 복사를 하고 싶은 경우 copy() 함수를 이용해 명시적 복사
>###    5. 인덱싱, 슬라이싱
        - numpy는 원래 다량의 데이터 처리를 가정하고 만든 패키지라서 객체를 복사하면 많은 메모리 자원을 사용하게 될 가능성이 있다.
        - 따라서 numpy의 배열은 slicing하면 원본 그대로를 참조한 상태에서 일부만 가져오기 때문에 원본 데이터가 변경될 수 있다.
        - numpy의 배열은 차원이 늘어나면 추가된 차원은 앞 쪽에 추가됨.
        * boolean indexing 
            - 1, 2, 3, 4와 같은 index를 리턴하는 것이 아닌, true/false로 리턴함
            - boolean 배열에서는 예약어인 and, or를 사용할 수 없다. 따라서 & 와 |를 사용
>###    6. fancy 색인
        - 정수 배열을 사용한 색인
        - 정수 배열을 이용해 좌표값을 설정
        - ix_ 는 index의 의미로 좀 더 편하게 사용할 수 있는 함수 제공
>###    7. 배열 전치, 축 바꾸기
        - 데이터 복사하지 않고 모양 바뀐 뷰를 반환하는 특별한 기능
        
## 유니버셜 함수
>###    1. ufunc
        1. 정의
            - ndarray 안에 있는 데이터 원소별로 연산을 수행하는 함수
            - 하나 이상의 스칼라 값을 받아 하나 이상의 스칼라 결과 값을 반환하는 간단한 함수를 고속으로 수행 가능한 벡터화된 래퍼 함수
        
        2. 단항 유니버설 함수
            - abs, fabs
            - sqrt
            - square
            - exp
            - ...
        3. 이항 유니버설 함수
            - add
            - subtract
            - multiply
            - divide, floor_divide
            - power
            - maximum, fmax
            - ...
## 배열을 사용한 데이터 처리
>###    1. 배열사용 데이터 처리
        - 반복문 작성하지 않고 간결한 배열연산으로 많은 종류의 데이터 처리 작업 가능
>###    2. 배열연산으로 조건절 표시
        1. numpy.where함수
            - x if 조건 else y 와 같은 삼항식의 벡터화된 버젼
            - condition, true exp, false exp를 각각 인자로 받음
>###    3. 수학메서드, 통계메서드
        1. 수학, 통계 메서드를 통한 데이터 분석
            - 배열 전체 혹은 배열의 한 축에 따르는 자료에 대한 통계를 계산키 위한 수학 함수는 배열 메서드로 사용가능
            - Numpy의 최상위 함수를 사용하거나 배열의 인스턴스 함수 사용할 수 있음
>###    4. 불리언 배열을 위한 메서드
        