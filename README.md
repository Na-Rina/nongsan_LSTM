# 농산물 가격 예측 프로젝트 🍊
https://dacon.io/competitions/official/236176/talkboard/410492?page=1&dtype=recent

![image](https://github.com/Na-Rina/nongsan_LSTM/assets/91365023/df0b5c0d-3fef-4654-a187-0b67f36046bd)

### 목표
1. **시계열 데이터 이해와 분석**: 시계열 데이터의 기본 구조와 특성, 그리고 주요 분석 기법(e.g., 이동평균, 지수이동평균, 계절성 분해 등)을 이해하고 적용합니다.
2. **데이터 전처리 및 정상성**: 누락된 데이터, 이상치, 0 값 등을 처리하고, 시계열 데이터의 정상성을 검정합니다.
3. **기초부터 고급 예측 모델까지**: Naive Forecasting으로 시작하여, ARIMA와 LightGBM 같은 고급 예측 모델까지 이해하고 적용합니다.
4. **파라미터 튜닝과 성능 평가**: ACF, PACF 그래프 및 Optuna를 활용하여 모델의 성능을 최적화하고, NMAE 같은 성능 지표로 평가합니다.
5. **Feature Engineering과 모델 고도화**: 다양한 Feature Engineering 기법을 활용하여 모델의 성능을 향상시킵니다.
6. **실전 적용과 결과 해석**: 학습한 모델을 실제 데이터에 적용하여 예측 결과를 생성하고, 이를 시각적으로 분석 및 해석합니다.


## 데이터셋 정보

## Dataset Info
### 1. train.csv
- **train 데이터**: 2019년 01월 01일부터 2023년 03월 03일까지의 유통된 품목의 가격 데이터
- **컬럼 설명**:
  - `item`: 품목 코드
    - TG : 감귤
    - BC : 브로콜리
    - RD : 무
    - CR : 당근
    - CB : 양배추
  - `corporation`: 유통 법인 코드 (법인 A부터 F 존재)
  - `location`: 지역 코드
    - J : 제주도 제주시
    - S : 제주도 서귀포시
  - `supply(kg)`: 유통된 물량, kg 단위
  - `price(원/kg)`: 유통된 품목들의 kg 마다의 가격, 원 단위

### 2. international_trade.csv
- 관련 품목 수출입 정보
- 중량 단위 kg
- 금액 단위 천 달러

### 3. test.csv
- **test 데이터**: 2023년 03월 04일부터 2023년 03월 31일까지의 데이터

### 4. 추천 외부 데이터
- 농산물 유통 정보: [농산물유통종합정보시스템](https://www.kamis.or.kr/customer/reference/openapi_list.do)
- aT 도매유통 정보시스템: [aT 도매유통 정보](https://at.agromarket.kr/openApi/apiInfoDtl.do?apiSeq=1)
- 농촌진흥청 국립농업과학원 농업기상 데이터: [농업기상 데이터](https://www.data.go.kr/data/15078057/openapi.do)
- 관세청_품목별 수출입 실적: [수출입 실적](https://www.data.go.kr/data/3046122/openapi.do)
- 농식품수출정보: [농식품수출정보](https://www.kati.net/statistics/monthlyPerformanceByProduct.do)
