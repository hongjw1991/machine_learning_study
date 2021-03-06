## pandas 모듈
------------------------------
>###    1. pandas 
        - 고수준의 자료 구조 제공
        - 파이썬을 통한 빠르고 쉬운 데이터 분석 도구 제공
        - Numpy 기반에서 개발됨
>###    2. pandas의 자료구조
        1. Series (vector와 비슷)
            - 일련의 객체를 담을 수 있는 1차원 배열 같은 자료 구조
            - 색인(index)라고 하는 배열의 데이터에 연관된 이름 가지고 있음
            - 배열 데이터로부터 가장 간단한 것 생성 가능
            - 좌측에 index를 출력, 우측에 index에 해당하는 값 출력
            - index의 이름도 지정할 수 있다.
            - dictionary 내장 자료구조 함수를 이용해서도 만들 수 있다.
            - index는 unique하지 않아도 상관없다. 그러나 값을 대입할 때는 전체의 index를 다 바꿔줘야 한다.
            - unique하지 않아도 되기 때문에 자기 자신끼리의 연산에서는 같은 unique끼리 같은 위치에 있는 서로의 값에 대해 연산한다.
            - 만약 다른 객체라면 인덱스의 수를 양쪽 인덱스의 같은 인덱스 수만큼 곱해서 반환한다.
        2. DataFrame
            - 표 같은 스프레드시트 형식의 자료 구조로 여러 개의 칼럼이 있음
            - 각 칼럼은 서로 다른 종류의 값을 담을 수 있다.
            - 로우와 칼럼에 대한 색인이 있음
            - 즉, 색인의 모양이 같은 Series 객체를 담고 있는 파이썬 사전
        3. 색인 객체
            - 표 형식의 데이터에서 각 로우와 칼럼에 대한 이름과 다른 메타데이터를 저장하는 객체
            - 변경 불가능하다.
>###    3. 핵심기능
        1. 재색인
            - reindex는 새로운 색인에 맞도록 객체를 새로 생성하는 기능
            - 기존의 원본은 그대로 내버려두고 새로운 색인으로 만든 객체를 만들어 재배열하고 없는 값은 비어있는 값을 추가
            - fill_value의 값을 주면 빈 값에 해당 값을 insert
            - method=ffill 혹은 pad 메서드를 이용시에는 앞의 값으로 채움.
            - bfill 또는 backfill은 뒤의 값으로 채움
            - 보간은 column에 대해서는 적용되지 않는다.
        2. 로우 또는 컬럼 삭제
            1. drop 메서드
                - 선택한 값이 삭제된 상태의 새로운 객체로 복사 가능
        3. 색인하기, 선택하기, 자르기
            - Numpy배열과 유사하게 동작
            - Series색인은 정수가 아니어도 된다.
            - label을 이용한 indexing이 가능 
                - 이 경우 end point의 값도 출력됨
            * ix를 이용한 indexing 
                - Numpy와 비슷한 방식에 추가적으로 축의 라벨을 사용해 로우와 칼럼을 선택해 indexing가능
                - python3부터는 loc사용 권장
        4. 산술연산과 데이터 정렬
            - 색인이 다른 객체 간의 산술연산의 경우 결과에 두 색이 통합된다.
            * 메서드에 채워 넣을 값 지정할 수 있다.
                - fill_value에 값을 넣으면 된다.
                - columns 속성에 list형으로 값을 넣으면 분리되어 column의 label이 지정됨
            * 데이터프레임과 Series간의 연산
                - 브로드캐스팅 규칙에 의해 연산됨                
        5. 함수적용과 매핑
            - pandas 객체도 Numpy의 유니버설 함수(배열의 각 원소에 적용되는 메서드)를 적용할 수 있다.
            - 각 로우나 칼럼의 1차원 배열에 함수를 적용할 수 있다. apply메서드 통해 수행 가능
            * dataframe의 경우는 로우나 컬럼을 잘라서 함수에 적용시킨 다음 결과를 Series 혹은 dataframe으로 만들어 반환한다.
                - 함수가 scalar를 내보내는 경우 Series로 내보낸다.
                - 어떤 축을 기준으로 할지는 axis parameter값을 주면 지정할 수 있다.
            * Series의 경우는 Series의 값들을 함수적용해서 Series 혹은 dataframe으로 반환한다.
            * applymap
                - applymap함수는 apply기능과 map함수의 기능이 들어가 있음
                - dataframe에 대해서 각 Series의 각 원소에 적용할 함수를 지정하고 모아서 dataframe으로 return하낟.
            * map함수
                * 파이썬의 map함수를 리뷰해보자
                    - 파이썬은 R처럼 recycling규칙이 없어서 list에 대해 각각의 연산을 단순 수행할 수 없다.
                    - 따라서 for loop를 이용하거나 map함수를 이용해야 한다.
            - 정리
                - apply()함수는 Dataframe, Series를 모두 반환할 수 있다.
                        - 인자로 받는 함수 : 집계 또는 통계 계열 함수
                - applymap()함수는 dataframe을 반환한다.
                        - 인자로 받는 함수 : 일반 함수
                - map함수는 Series를 반환한다.
        6. 정렬과 순위
            - sort_index메서드 : 로우나 칼럼의 색인이 알파벳 순으로 정렬된 새로운 객체 반환
            * 순위
                - rank()
                    - 같은 값의 경우는 등수에 평균을 내서 계산함
                    - method='first'로 지정시, 같은 값이 있으면 먼저 나온 값이 우선 등수를 차지함
        7. 중복색인
            - 색인은 반드시 유니크하지 않아도 된다. 즉 강제사항이 아님
            - 이에 따라 여러 중복색인이 있을 때, 특정 index의 값을 출력하면 그 경우 반환 타입도 Series이다.
>###    4. 기술통계 계산과 요약
        - pandas 개게는 일반적 수학 메서드와 통계 메서드를 가짐
        - 처음부터 누락 데이터는 제외하여 연산함
        1. 상관관계와 공분산
            - pandas_datareader 패키지(외부 확장 모듈)을 설치해야 한다.
            - As of v0.6.0 Yahoo!, Google Options, Google Quotes and EDGAR have been immediately deprecated due to large changes in their API and no stable replacement.
            - 위 설명에 따라, 0.6.0버젼부터 Google, Yahoo등 관련 라이브러리가 완전 deprecated되었음
            - 따라서 교재에 있는 데이터를 사용해서 예제를 활용할 수가 없다.
            - corr()은 상관계수, cov()는 공분산을 반환한다.
            - corrwith()는 다른 Series나 DataFrame과의 상관관계를 계산함. Series를 넘기면 각 칼럼에 대해 계산한 상관관계를 담은 Series를 반환
        2. 유일 값, 값 세기, 멤버쉽
            - Series에 담긴 값의 정보 추출 하는 메서드 사용
>###    5. 누락 데이터 처리
        - pandas 모듈은 누락 데이터를 전부 NaN으로 취급함.
        - None값 또한 NaN으로 취급한다.
        1. 누락 데이터 골라내기
            - dropna를 사용하는 것이 매우 유용함
            - Series에 대해 dropna를 적용시 실제 데이터가 들어있는 색인 값과 데이터를 Series값으로 반환
        2. 누락 값 채우기
            - fillna메서드를 활용해 구멍을 메울 수 있다.
            - 새로운 객체를 반환함. inplace를 사용하면 기존 객체 변환.
>###    6. 계층적색인
        - 축에 대해 다중 색인 단계를 지정할 수 있다.
        - 차원이 높은 데이터를 낮은 차원의 형식으로 다룰 수 있다.
        * stack, unstack
            - row, column의 index를 양쪽으로 위치 변경함.
            - level=-1이 default이며 이는 가장 하위 인덱스를 의미한다.
        1. 계층 순서 바꾸고 정렬하기
            - swaplevel : 넘겨받은 2개의 계층 번호나 이름이 뒤바뀐 새로운 객체 반환(데이터는 변경되지 안흥ㅁ)
        2. 단계별 요약통계      
            - 기술통계, 요약통계는 level옵션을 가짐. 이는 어떤 한 축에 대해 합을 구하고 싶은 단계를 지정할 수 있는 옵션임.
        3. 데이터프레임의 칼럼 사용하기
            - index를 칼럼으로, 혹은 반대로 이동가능.
>###    7. pandas와 관련된 기타 주제
            1. 정수색인
                - 정수가 인덱스일 때 단순히 정수를 이용해 색인하면 에러가 발생할 수 있다. 레이블로 인식하기 때문
                - 정수가 인덱스가 아니라면 문제가 없다.
            2. panel 데이터
                - panel : 3차원 데이터 프레임
                - 더 이상 지원되지 않음.