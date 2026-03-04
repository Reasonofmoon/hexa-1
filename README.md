# 🏭 hexa-1: 제조업 AX 마스터클래스

> "불량률을 AI가 잡는다" — 제조업 중소기업을 위한 AI 트랜스포메이션 실습 과정

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Reasonofmoon/hexa-1/blob/main/notebooks/M7_MFG_kpi_lab.ipynb)

---

## 🎯 이 과정은?

**대상**: 금속가공, 전자부품, 식품제조, 자동차부품 등 제조업 중소기업 대표 및 관리자  
**목표**: AI를 활용해 품질관리·예지보전·생산보고서 3가지 핵심 업무를 자동화  
**시간**: 6시간 (강의 3h + 실습 3h)

---

## 🎯 수준별 활용 가이드

### 🟢 Starter — "5분 안에 첫 AI 결과물"
1. `labs/M1-diagnosis/README.md` 열기
2. 프롬프트 복사 → ChatGPT/뤼튼에 붙여넣기
3. 공장명·제품·불량 유형만 수정 후 Enter
4. AX 자가진단 보고서 즉시 출력 ✅ (코딩 0줄)

### 🔵 Professional — "Colab으로 배치 자동화"
```python
# Colab Secret에 저장 (이름: GEMINI_API_KEY)
from google.colab import userdata
api_key = userdata.get('GEMINI_API_KEY')
```
1. Colab 뱃지 클릭 → 노트북 오픈
2. 런타임 → 모두 실행
3. 공장 정보 셀만 수정
4. 마지막 셀 → KPI 보고서 자동 다운로드

### 🟣 Enterprise — "멀티 에이전트 파이프라인"
- OMC `/team 3:executor`로 분석→보고서→PR 자동화
- `AGENTS.md` 커스터마이징으로 사내 AI 규칙 내재화
- `scripts/agents_config_validator.py` 셀프 검증

---

## ⚙️ 3모듈 커리큘럼

| 모듈 | 제목 | Colab | Labs |
|---|---|---|---|
| M1 | AX 진단 & 제조업 벤치마킹 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](notebooks/M1_AX_diagnosis.ipynb) | [labs/M1](labs/M1-diagnosis/) |
| M7-MFG | KPI 분석 & 불량률 자동 보고 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](notebooks/M7_MFG_kpi_lab.ipynb) | [labs/M7-MFG](labs/M7-MFG/) |
| M9 | 사내 시스템 연동 & 자동 보고서 배포 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](notebooks/M9_auto_report.ipynb) | [labs/M9](labs/M9-deploy/) |

---

## 📂 프로젝트 구조

```
hexa-1/
├── notebooks/
│   ├── M1_AX_diagnosis.ipynb       ← AX 진단 자동화
│   ├── M7_MFG_kpi_lab.ipynb        ← KPI 불량률 분석 ★
│   └── M9_auto_report.ipynb        ← 엑셀→슬랙 보고서 자동화
├── labs/
│   ├── M1-diagnosis/README.md      ← 진단 프롬프트 모음
│   ├── M7-MFG/README.md            ← 제조업 실습 가이드
│   └── M9-deploy/README.md         ← 배포 체크리스트
├── scripts/
│   ├── kpi_calculator.py           ← 불량률 계산 (실행 가능)
│   ├── auto_report_generator.py    ← 엑셀→콘솔/슬랙
│   └── agents_config_validator.py  ← AGENTS.md 검증
└── shared/
    └── manufacturing_kpi_sample.csv ← 샘플 KPI 데이터 (30행)
```

---

## 🌐 hexa 시리즈
- **hexa-1** (현재): 🏭 제조업
- [hexa-2](https://github.com/Reasonofmoon/hexa-2): 🍽️ 외식/F&B
- [hexa-3](https://github.com/Reasonofmoon/hexa-3): 🛒 소매/유통
- [hexa-4](https://github.com/Reasonofmoon/hexa-4): 📚 교육/에드테크
- [hexa-5](https://github.com/Reasonofmoon/hexa-5): 🏗️ 건설/부동산
- [hexa-6](https://github.com/Reasonofmoon/hexa-6): 💼 전문서비스/IT

Made with ❤️ by [Reasonofmoon × Antigravity](https://github.com/Reasonofmoon)  
중소기업 AX 전환을 위한 실전 교육
