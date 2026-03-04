<div align="center">

# 🏭 hexa-1: 제조업 AX 마스터클래스

### *AI로 제조 현장을 혁신하는 12주 실전 과정*

**불량률 분석부터 예지보전까지 — 현장 데이터로 직접 검증하는 AX 커리큘럼**

[![Version](https://img.shields.io/badge/version-1.0.0-6366f1?style=for-the-badge)](https://github.com/Reasonofmoon/hexa-1)
[![Colab](https://img.shields.io/badge/Google_Colab-12개_노트북-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](https://github.com/Reasonofmoon/hexa-1/tree/main/notebooks)
[![Sector](https://img.shields.io/badge/Sector-Manufacturing-2563eb?style=for-the-badge&logo=industry&logoColor=white)](https://github.com/Reasonofmoon/hexa-1)
[![License](https://img.shields.io/badge/License-MIT-a78bfa?style=for-the-badge)](LICENSE)
[![Scripts](https://img.shields.io/badge/CLI_Scripts-8개-22d3ee?style=for-the-badge&logo=python)](scripts/)

> **"제조업 현장에서 AI 도구를 사용할 수 있는 인력은 전체의 3% 미만이다."**  
> hexa-1은 코딩 경험이 없는 현장 관리자·공장장도 Colab 노트북으로  
> 바로 실전 결과를 내도록 설계된 **12주 실무 중심 AX 커리큘럼**입니다.

[📗 커리큘럼 시작](notebooks/) · [🔧 스크립트 도구](scripts/) · [📂 실습 데이터](shared/) · [🐛 이슈](../../issues)

</div>

---

## 🧠 Philosophy — "왜 제조업 AX인가"

기존 제조업 AI 교육의 문제: **이론만 있고 현장 데이터가 없다**.

| 기준 | 기존 AI 교육 | hexa-1 AX 커리큘럼 |
|------|-------------|-------------------|
| 데이터 | 가상의 iris, titanic | **현장 KPI CSV** (불량수, OEE, 납품) |
| 결과물 | 모델 정확도 숫자 | **경영진 보고서 + Slack 알림 자동화** |
| 난이도 | Python 필수 | **Colab 실행만으로 완성** |
| 기간 | 3개월+ 이론 | **Week 1부터 실전 결과** |
| 연결성 | 개별 실습 | **W1→W12 파이프라인으로 연결** |

```mermaid
graph LR
    A[📋 W1-2 진단&분류] --> B[📄 W3-4 문서자동화]
    B --> C[📊 W5-6 KPI시각화]
    C --> D[📨 W7-8 Slack&Sheets]
    D --> E[🔮 W9-10 예지보전]
    E --> F[🎛️ W11-12 통합대시보드]
    
    style A fill:#6366f1,color:#fff
    style F fill:#22d3ee,color:#fff
```

---

## ⚙️ 시스템 레이어

### Layer 1 · Foundation (W1~W4) — AI 기초 도구화
> **Wow**: 불량 설명 텍스트 100건을 AI가 **5초 안에** 자동 분류

| 주차 | 노트북 | 핵심 도구 |
|------|--------|-----------|
| W1 | M1_AX_diagnosis.ipynb | Gemini API, 자가진단 |
| W2 | W02_defect_classifier.ipynb | 불량 5분류, 시각화 |
| W3 | W03_delivery_doc.ipynb | 납품확인서 배치 생성 |
| W4 | W04_HR_automation.ipynb | 채용공고·작업지시서 |

### Layer 2 · Analytics (W5~W8) — 데이터 기반 의사결정
> **Wow**: OEE·불량률·가동률을 **클릭 한 번**에 경영진 차트로 변환

| 주차 | 노트북 | 핵심 도구 |
|------|--------|-----------|
| W5 | W05_KPI_analysis.ipynb | pandas, matplotlib, 3σ |
| W6 | W06_OEE_analysis.ipynb | OEE 자동 계산, 트렌드 |
| W7 | W07_slack_alert.ipynb | Slack Webhook, 배치 발송 |
| W8 | W08_sheets_kpi.ipynb | Google Sheets 실시간 연동 |

### Layer 3 · Intelligence (W9~W12) — 자동화 운영 시스템
> **Wow**: 이상 발생 시 **Slack 자동 알림 → 협력사 메일 → 대시보드 업데이트** 파이프라인

| 주차 | 노트북 | 핵심 도구 |
|------|--------|-----------|
| W9 | W09_predictive.ipynb | 예지보전, 3σ 이상감지 |
| W10 | W10_vendor_comm.ipynb | 협력사 커뮤니케이션 자동화 |
| W11 | W11_mfg_dashboard.ipynb | 종합 AI 대시보드 |
| W12 | W12_cockpit.ipynb | 통합 운영 시스템 발표 |

---

## 🎯 수준별 활용 가이드

### 🟢 Starter — "5분 안에 첫 결과"
1. [W2 노트북](https://colab.research.google.com/github/Reasonofmoon/hexa-1/blob/main/notebooks/W02_defect_classifier.ipynb) 클릭 → Colab에서 열기
2. `FACTORY_INFO`에 회사명·제품명만 입력 (`✏️` 표시 찾기)
3. `Shift+Enter`로 위에서 아래로 실행
4. 불량 분류 차트 + 결과 CSV 자동 다운로드

> ⚠️ API 키 발급: [Google AI Studio](https://aistudio.google.com/apikey) → GEMINI_API_KEY

### 🔵 Professional — "내 공장 데이터로 실전 분석"
1. `shared/manufacturing_kpi_sample.csv` 구조 확인
2. 내 공장 KPI 데이터를 같은 형식으로 준비
3. W5~W6 노트북에서 CSV 업로드 → OEE·불량률 자동 계산
4. W7 노트북에서 Slack Webhook 연결 → 일일 KPI 자동 발송

```bash
# CLI 스크립트 직접 사용
python scripts/kpi_calculator.py --input shared/manufacturing_kpi_sample.csv
python scripts/slack_kpi_sender.py --input data.csv --webhook [WEBHOOK_URL]
python scripts/oee_calculator.py --input data.csv --output results.csv
```

### 🟣 Enterprise — "팀 표준화 & 파이프라인"
1. `scripts/M9_demo_runner.py` 실행 → 전체 파이프라인 원클릭 시연
2. GitHub Actions로 매일 자동 KPI 집계 스케줄링
3. W11~W12를 내부 대시보드로 배포 (Flask/Streamlit)
4. hexa-2, cedu-1과 연계해서 업종 간 벤치마킹

---

## 📂 디렉토리 구조

```
hexa-1/
├── notebooks/          ← 12주 Colab 노트북 (W01~W12)
│   ├── W02_defect_classifier.ipynb    # 불량 AI 분류기
│   ├── W03_delivery_doc.ipynb         # 납품문서 자동화
│   ├── W04_HR_automation.ipynb        # HR 문서 생성
│   ├── W05_KPI_analysis.ipynb         # KPI 분석 (오류수정본)
│   ├── W06_OEE_analysis.ipynb         # OEE 트렌드
│   ├── W07_slack_alert.ipynb          # Slack 알림
│   ├── W08_sheets_kpi.ipynb           # Sheets 연동
│   └── W09_predictive.ipynb           # 예지보전 이상감지
├── scripts/            ← CLI 실행 가능 Python 스크립트
│   ├── kpi_calculator.py              # KPI 불량률 계산기
│   ├── review_auto_reply.py           # 리뷰 자동 답글
│   ├── oee_calculator.py              # OEE 계산기
│   ├── defect_classifier.py           # 불량 분류기
│   ├── slack_kpi_sender.py            # Slack 발송
│   ├── sheets_kpi_template.py         # Sheets 연동
│   ├── hr_doc_generator.py            # HR 문서 생성기
│   ├── oee_sample_data.csv            # OEE 샘플 데이터
│   └── M9_demo_runner.py              # 원클릭 데모 런처
├── shared/             ← 실습 데이터
│   ├── manufacturing_kpi_sample.csv   # KPI 샘플
│   └── delivery_reviews_sample.csv    # 리뷰 샘플
└── labs/               ← 실습 가이드 (M2~M7)
    ├── M2-defect/README.md
    ├── M3-delivery-doc/README.md
    ├── M4-hr/README.md
    └── M7-MFG/README.md
```

---

## 🔧 확장 가이드

| 우선순위 | 커스터마이징 | 난이도 | 영향 범위 |
|----------|--------------|--------|-----------|
| **1st** | `FACTORY_INFO` 딕셔너리 수정 | ⭐ | 회사명·제품·날짜 |
| **2nd** | 샘플 CSV를 실제 데이터로 교체 | ⭐⭐ | 분석 결과 전체 |
| **3rd** | Slack Webhook 연결 | ⭐⭐ | 실시간 알림 |
| **4th** | Sheets API 인증 설정 | ⭐⭐⭐ | 대시보드 자동화 |
| **5th** | W11~W12 대시보드 서버 배포 | ⭐⭐⭐ | 팀 공유 시스템 |

---

## 🚀 빠른 시작

```bash
# 1. 레포 클론
git clone https://github.com/Reasonofmoon/hexa-1.git
cd hexa-1

# 2. 환경 설정 (로컬 실행 시)
pip install google-generativeai pandas matplotlib gspread requests

# 3. 데모 실행
python scripts/M9_demo_runner.py

# 4. KPI 분석 바로 실행
python scripts/kpi_calculator.py --input shared/manufacturing_kpi_sample.csv
```

또는 **Colab에서 바로 실행** (설치 불필요):  
[![W2 열기](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Reasonofmoon/hexa-1/blob/main/notebooks/W02_defect_classifier.ipynb)
[![W5 열기](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Reasonofmoon/hexa-1/blob/main/notebooks/W05_KPI_analysis.ipynb)
[![W9 열기](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Reasonofmoon/hexa-1/blob/main/notebooks/W09_predictive.ipynb)

---

## 🔗 전체 AX 시리즈

| 레포 | 섹터 | 핵심 모듈 |
|------|------|-----------|
| **hexa-1** (현재) | 🏭 제조업 | OEE, 불량분류, 예지보전 |
| [hexa-2](https://github.com/Reasonofmoon/hexa-2) | 🍽️ F&B | 리뷰분석, 메뉴카피, 재고예측 |
| [hexa-3](https://github.com/Reasonofmoon/hexa-3) | 🛒 소매/유통 | 상품카피, CRM, SEO |
| [hexa-4](https://github.com/Reasonofmoon/hexa-4) | 📚 교육 | 교안자동화, 성적분석, 챗봇 |
| [hexa-5](https://github.com/Reasonofmoon/hexa-5) | 🏗️ 건설 | 계약서분석, 공정관리 |
| [hexa-6](https://github.com/Reasonofmoon/hexa-6) | 💼 IT/서비스 | 제안서, 코드리뷰, KPI |

---

## 🌐 다국어 지원

| 항목 | 현황 |
|------|------|
| 노트북 UI | 한국어 |
| 스크립트 출력 | 한국어 (컬럼 자동감지: 한/영) |
| 샘플 데이터 | 한국어 컬럼명 |
| README | 한국어 / English (예정) |

---

*AX Consulting Curriculum © 2026 | Powered by Google Gemini*
