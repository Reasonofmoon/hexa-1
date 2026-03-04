# M2-defect 실습 가이드: 불량 유형 AI 분류기

## 오늘 실습 목표
1. 생산 불량 데이터를 AI가 자동으로 분류한다
2. 이미지 기반 불량 탐지 모델을 이해한다
3. 분류 결과를 기반으로 개선 방안을 도출한다

---

## 🟢 Starter: 프롬프트만으로 (코딩 없음)

아래를 ChatGPT/뤼튼에 그대로 붙여넣고, `[]` 부분만 바꾸세요:

```
당신은 제조업 품질관리 AI 전문가입니다.
우리 공장(업종: [전자부품], 제품: [PCB 기판])의 불량 데이터를 분석해주세요.

불량 유형:
- [스크래치]: 35건 (2.1%)
- [찍힘]: 28건 (1.7%)
- [이물질]: 42건 (2.5%)
- [변색]: 15건 (0.9%)

각 불량 유형별 특징과 주요 원인을 분석하고,
우선순위별 개선 대책을 3가지씩 제안해주세요.
```

---

## 🔵 Professional: Colab 실행 (5단계)

**1단계**: Colab 뱃지 클릭 → 노트북 오픈  
**2단계**: `DEFECT_INFO` 셀에서 공장명·제품·불량 유형 수정  
**3단계**: 런타임 → 모두 실행  
**4단계**: 불량 분류 모델 학습 및 정확도 확인  
**5단계**: 혼동 행렬과 분류 리포트 자동 다운로드 ✅

---

## 🔥 확장 과제 2개

**과제 1 — 멀티클래스 분류 모델 개선**
```python
# 더 정교한 분류를 위해 클래스 가중치 조정
from sklearn.utils.class_weight import compute_class_weight
class_weights = compute_class_weight('balanced', classes=np.unique(y), y=y)
model.fit(X_train, y_train, sample_weight=class_weights[train_idx])
```

**과제 2 — 분류 임계값 동적 조정**
```python
# 생산 라인별로 최적 임계값 자동 설정
from sklearn.metrics import precision_recall_curve

for line in production_lines:
    precision, recall, thresholds = precision_recall_curve(y_true, y_pred_proba[line])
    f1_scores = 2 * (precision * recall) / (precision + recall)
    optimal_threshold = thresholds[np.argmax(f1_scores)]
```