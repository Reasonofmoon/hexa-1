# M6-oee 실습 가이드: OEE & 생산성 트렌드 분석

## 오늘 실습 목표
1. 설비종합효율(OEE)을 계산하고 분석한다
2. 생산성 트렌드를 시각화하고 예측한다
3. 병목 현상을 식별하고 개선안을 제시한다

---

## 🟢 Starter: 프롬프트만으로 (코딩 없음)

아래를 ChatGPT/뤼튼에 그대로 붙여넣고, `[]` 부분만 바꾸세요:

```
당신은 제조업 생산성 분석 전문가입니다.
우리 공장(업종: [자동차부품], 라인: [조립라인 1])의 OEE 데이터를 분석해주세요.

OEE 구성요소:
- 가동률: [85%] (계획 중단 제외)
- 성능률: [78%] (이상 속도/공정 손실)
- 양품률: [96%] (불량/재작업 제외)

월별 생산성 트렌드:
- 1월: [82%]
- 2월: [84%]
- 3월: [87%]

병목 현상과 개선 대책을 제안해주세요.
```

---

## 🔵 Professional: Colab 실행 (5단계)

**1단계**: Colab 뱃지 클릭 → 노트북 오픈  
**2단계**: `OEE_INFO` 셀에서 공장명·라인·데이터 기간 수정  
**3단계**: 런타임 → 모두 실행  
**4단계**: OEE 대시보드와 트렌드 차트 자동 생성 확인  
**5단계**: 분석 보고서와 개선 제안서 자동 다운로드 ✅

---

## 🔥 확장 과제 2개

**과제 1 — 실시간 OEE 모니터링**
```python
# 생산 데이터 스트리밍으로 실시간 OEE 계산
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def update_oee_dashboard(frame):
    current_data = fetch_production_data()
    oee_score = calculate_oee(current_data)
    
    # 실시간 대시보드 업데이트
    plt.clf()
    plt.bar(['가동률', '성능률', '양품률'], 
            [current_data['availability'], 
             current_data['performance'], 
             current_data['quality']])
    
ani = FuncAnimation(fig, update_oee_dashboard, interval=60000)  # 1분 간격
```

**과제 2 — 생산성 예측 모델**
```python
# 시계열 분석으로 미래 생산성 예측
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error

# 과거 OEE 데이터로 ARIMA 모델 학습
model = ARIMA(oee_history, order=(1,1,1))
model_fit = model.fit()

# 30일 후 생산성 예측
forecast = model_fit.forecast(steps=30)
confidence_interval = model_fit.get_forecast(steps=30).conf_int()

# 예측 결과 기반 개선 목표 설정
target_oee = forecast.mean() * 1.05  # 5% 향상 목표
```