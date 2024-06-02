# 농산물 가격 예측 프로젝트 🍊


### 개요
프로젝트의 초점은 2021년도에 열렸던 농산물 가격 예측 대회의 데이터를 기반으로 시계열 데이터 분석 및 시계열 예측의 기본기를 다질 수 있도록 구성

### 목표
1. **시계열 데이터 이해와 분석**: 시계열 데이터의 기본 구조와 특성, 그리고 주요 분석 기법(e.g., 이동평균, 지수이동평균, 계절성 분해 등)을 이해하고 적용합니다.
2. **데이터 전처리 및 정상성**: 누락된 데이터, 이상치, 0 값 등을 처리하고, 시계열 데이터의 정상성을 검정합니다.
3. **기초부터 고급 예측 모델까지**: Naive Forecasting으로 시작하여, ARIMA와 LightGBM 같은 고급 예측 모델까지 이해하고 적용합니다.
4. **파라미터 튜닝과 성능 평가**: ACF, PACF 그래프 및 Optuna를 활용하여 모델의 성능을 최적화하고, NMAE 같은 성능 지표로 평가합니다.
5. **Feature Engineering과 모델 고도화**: 다양한 Feature Engineering 기법을 활용하여 모델의 성능을 향상시킵니다.
6. **실전 적용과 결과 해석**: 학습한 모델을 실제 데이터에 적용하여 예측 결과를 생성하고, 이를 시각적으로 분석 및 해석합니다.


## 데이터셋 정보

### 1. public_data: public leaderboard용 데이터
#### 1-1. train.csv: 베이스라인 코드용으로 가공된 학습 데이터
- **date**: 일자
- **요일**: 요일
- **품목_거래량(kg)**: 해당 품목의 거래량
- **품목_가격(원/kg)**: 해당 품목의 kg당 가격
- **품목_가격 산출 방식**: 품목 또는 품종의 총 거래금액/총 거래량 (※취소된 거래내역 제외)

#### 1-2. test_files: 베이스라인 코드용으로 가공된 테스트 데이터 (추론일자별 분리, ex. test_2020-08-29.csv => 2020년 8월 29일 추론에 사용 가능 데이터)

#### 1-3. train_AT_TSALET_ALL: 학습용 전국 도매시장 거래정보 데이터 (train.csv 생성에 사용)
- **SALEDATE**: 경락 일자
- **WHSAL_NM**: 도매시장
- **CMP_NM**: 법인
- **PUM_NM**: 품목
- **KIND_NM**: 품종
- **DAN_NM**: 단위
- **POJ_NM**: 포장
- **SIZE_NM**: 크기
- **LV_NM**: 등급
- **SAN_NM**: 산지
- **DANQ**: 단위중량
- **QTY**: 물량
- **COST**: 단가
- **TOT_QTY**: 총물량 (음수로 집계된 값은 거래 취소 내역)
- **TOT_AMT**: 총금액

#### 1-4. test_AT_TSALET_ALL: 추론용 전국 도매시장 거래정보 데이터 (test_files 생성에 사용)

### 2. private_data: private leaderboard용 데이터, public leaderboard 학습 및 추론 사용 불가
#### 2-1. private.csv: 베이스라인 코드용으로 가공된 데이터

#### 2-2. AT_TSALET_ALL: 2021년 8월까지의 전국 도매시장 거래정보 데이터 (private.csv 생성에 사용)

### 3. sample_submission.csv: 제출 양식
- **예측대상일자**: 예측대상일 (기준일로부터 1, 2, 4주 뒤 일자)
- **품목_가격(원/kg)**: 해당 품목의 kg당 가격

### 4. 추천 외부 데이터
- 농산물 유통 정보: [농산물유통종합정보시스템](https://www.kamis.or.kr/customer/reference/openapi_list.do)
- aT 도매유통 정보시스템: [aT 도매유통 정보](https://at.agromarket.kr/openApi/apiInfoDtl.do?apiSeq=1)
- 농촌진흥청 국립농업과학원 농업기상 데이터: [농업기상 데이터](https://www.data.go.kr/data/15078057/openapi.do)
- 관세청_품목별 수출입 실적: [수출입 실적](https://www.data.go.kr/data/3046122/openapi.do)
- 농식품수출정보: [농식품수출정보](https://www.kati.net/statistics/monthlyPerformanceByProduct.do)
