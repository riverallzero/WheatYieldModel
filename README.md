# 밀 생산량 예측을 위한 머신러닝 기반 생육 데이터 중요도 분석 및 주요 조사항목 선정

## 설명
- 2022 추계 작물학회 고려대학교(10/13~14)
- 이용 기술 : pandas, scikit-learn, matplotlib
- 데이터 보안을 위해 Input 폴더 삭제

## 코드 설명
### 1_Clean Data
모델링을 위한 데이터 전처리 과정
-  <strong>전처리 전과정 수행 | <a href="https://github.com/riverallzero/Wheat_unbong/blob/main/1_Clean%20Data/preprocess_all.py">preprocess_all.py</a></strong> 
    * <a href="https://github.com/riverallzero/Wheat_unbong/blob/main/1_Clean%20Data/preprocess_unbong.py">preprocess_unbong.py</a>
  : 받아온 생육조사데이터 엑셀파일을 csv 형식으로 변환
    * <a href="https://github.com/riverallzero/Wheat_unbong/blob/main/1_Clean%20Data/preprocess_seed.py">preprocess_seed.py</a>
  : 개화기(4.28~5.3)부터 5.31까지 종자의 건물중, 생체중, 수분함량
    * <a href="https://github.com/riverallzero/Wheat_unbong/blob/main/1_Clean%20Data/preprocess_timedata.py">preprocess_timedata.py</a>
  : 정리된 데이터 시계열화
    * <a href="https://github.com/riverallzero/Wheat_unbong/blob/main/1_Clean%20Data/preprocess_data.py">preprocess_data.py</a>
  : 정리된 데이터 세로화
  
### 2_Model
XGBoost, Linear Regression, RandomForest를 이용한 모델링
- <a href="https://github.com/riverallzero/Wheat_unbong/blob/main/2_Model/correlation.py">correlation.py</a>: 데이터 간 상관관계 분석
    * 생체중과 건조중의 상관성이 있어 생체중만 사용하기로 결정
- <strong>XGBoost</strong> | <a href="https://github.com/riverallzero/Wheat_unbong/blob/main/2_Model/correlation.py">xgb_model.py</a>
<img src="https://user-images.githubusercontent.com/93754504/197714758-2399a576-b9ca-499f-8493-997ee0e270c2.png" width="300px">
- <strong>RandomForest</strong> | <a href="https://github.com/riverallzero/Wheat_unbong/blob/main/2_Model/randomforest_model.py">randomforest_model.py</a>
<img src="https://user-images.githubusercontent.com/93754504/197716144-3a4288de-9e02-4b00-8310-02c1d0a52839.png" width="300px">
- <strong>Linear Regression</strong> | <a href="https://github.com/riverallzero/Wheat_unbong/blob/main/2_Model/linear_model.py">linear_model.py</a>
<img src="https://user-images.githubusercontent.com/93754504/197717934-ddaea639-e146-496e-bdfa-e8e0154806a1.png" width="300px">

### 3_EDA
- 2022-05-03, 2022-05-17, 2022-05-31단위로 데이터의 분포 stripplot
<img src="https://user-images.githubusercontent.com/93754504/197717026-f49e0d78-7a3e-493c-9cf0-85c9b94695ca.png" width="700px">

## 결론
생산량 예측모델 중 XGBoost모델(MAE 163.44)은 개화기 이후 4주차의 SPAD 및 잎의 너비, 개화기의 잎 너비, LAI, 개화기 이후 2주차의 LAI가 중요한 변수로 나타났다. RandomForest모델(MAE 184.11)은 개화기 이후 4주차의 잎의 너비, SPAD, LAI, 개화기 LAI, 개화기 이후 2주차의 잎의 너비가 중요한 변수로 나타났다. Linear Regression모델(MAE 191.22)은 개화기 이후 2주차 수분함량과 LAI, 개화기의 LAI와 잎의 길이가 중요한 변수로 나타났다. 본 연구에서 생육조사를 통해 밀의 생육단계별 작황에 따라 주요한 조사항목을 선별한 의미가 있다. 하지만 대상지역이 한 지역으로 한정되어 기상, 토양 등 환경요인을 반영하지 못한 점이 한계로 생각되는 바, 향후 연구에서는 지속적인 모니터링과 다른 지역의 생육자료를 확보하여, 환경조건, 생육조건을 모두 고려할 계획이다.
