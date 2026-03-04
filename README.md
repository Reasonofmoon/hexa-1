<div align="center">

# 🏭 hexa-1: 제조업 AX 마스터클래스

### *"AI로 제조 현장을 혁신하는 12주 실전 과정"*

**불량률 분석부터 예지보전까지 — 현장 데이터로 직접 검증하는 AX 커리큘럼**

[![Version](https://img.shields.io/badge/version-1.0.0-6366f1?style=for-the-badge)](https://github.com/Reasonofmoon/hexa-1)
[![Colab](https://img.shields.io/badge/Google_Colab-12주_노트북-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](https://github.com/Reasonofmoon/hexa-1/tree/main/notebooks)
[![Sector](https://img.shields.io/badge/Sector-Manufacturing-2563eb?style=for-the-badge&logoColor=white)](https://github.com/Reasonofmoon/hexa-1)
[![Model](https://img.shields.io/badge/AI-Gemini_2.0_Flash-4285F4?style=for-the-badge&logo=google)](https://aistudio.google.com/)
[![License](https://img.shields.io/badge/License-MIT-a78bfa?style=for-the-badge)](LICENSE)

> **"제조업 현장에서 AI 도구를 실전 활용할 수 있는 인력은 전체의 3% 미만이다."**
> hexa-1은 코딩 경험이 없는 현장 관리자·공장장도 Colab 노트북 하나로
> **Week 1부터 실전 결과**를 내도록 설계된 12주 실무 중심 AX 커리큘럼입니다.

[🚀 W1 바로 시작](https://colab.research.google.com/github/Reasonofmoon/hexa-1/blob/main/notebooks/W01_mfg_ax_diagnosis.ipynb) · [📂 전체 노트북](notebooks/) · [🔧 CLI 스크립트](scripts/) · [🐛 이슈](../../issues)

</div>

---

## 🧠 Philosophy — "왜 제조업 AX인가"

기존 제조업 AI 교육의 문제: **이론만 있고 현장 데이터가 없다**.

| 기준 | 기존 AI 교육 | hexa-1 AX 커리큘럼 |
|------|-------------|-------------------|
| 데이터 | 가상의 iris, titanic | **현장 KPI CSV** (불량수, OEE, 납품) |
| 결과물 | 모델 정확도 숫자 | **경영진 보고서 + Slack 알림 자동화** |
| 난이도 | Python 필수 | **Colab 실행만으로 완성** |
| 기간 | 3개월+ 이론 | **W1부터 당일 실전 결과** |
| 연결성 | 개별 실습 | **W1→W12 자동화 파이프라인** |

```mermaid
graph LR
    A[📋 W1-2<br>진단·분류] --> B[📄 W3-4<br>문서자동화]
    B --> C[📊 W5-6<br>KPI시각화]
    C --> D[📨 W7-8<br>Slack·Sheets]
    D --> E[🔮 W9-10<br>예지보전]
    E --> F[🎛️ W11-12<br>통합대시보드]

    style A fill:#6366f1,color:#fff
    style B fill:#8b5cf6,color:#fff
    style C fill:#06b6d4,color:#fff
    style D fill:#10b981,color:#fff
    style E fill:#f59e0b,color:#fff
    style F fill:#22d3ee,color:#fff
```

---

## ⚙️ 12주 커리큘럼

### Layer 1 · Foundation (W1~W4) — AI 기초 도구화

> **Wow**: 불량 설명 텍스트 100건을 AI가 **5초 안에** 자동 분류 → 담당자 하루 2시간 절약

| 주차 | 주제 | 핵심 출력물 | Colab |
|------|------|------------|-------|
| W1 | AX 자가진단 & AI 로드맵 | 10항목 레이더 차트 · 맞춤 12주 로드맵 | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Reasonofmoon/hexa-1/blob/main/notebooks/W01_mfg_ax_diagnosis.ipynb) |
| W2 | AI 불량 분류기 | 5분류 자동 판정 · 불량 분포 막대그래프 | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Reasonofmoon/hexa-1/blob/main/notebooks/W02_defect_classifier.ipynb) |
| W3 | 납품 문서 자동화 | 납품확인서·이메일·검수보고서 ZIP | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Reasonofmoon/hexa-1/blob/main/notebooks/W03_delivery_doc.ipynb) |
| W4 | HR 문서 자동화 | 채용공고·작업지시서·평가서 자동 생성 | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Reasonofmoon/hexa-1/blob/main/notebooks/W04_HR_automation.ipynb) |

### Layer 2 · Analytics (W5~W8) — 데이터 기반 의사결정

> **Wow**: OEE·불량률·가동률을 **클릭 한 번**에 경영진 차트로 변환 → 주간 보고 30분→3분

| 주차 | 주제 | 핵심 출력물 | Colab |
|------|------|------------|-------|
| W5 | KPI 분석 & 이상감지 | 3σ 이상 자동 추출 · KPI 대시보드 PNG | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Reasonofmoon/hexa-1/blob/main/notebooks/W05_KPI_analysis.ipynb) |
| W6 | OEE 자동 계산 & 트렌드 | 가동률·성능률·품질률 자동 분석 | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Reasonofmoon/hexa-1/blob/main/notebooks/W06_OEE_analysis.ipynb) |
| W7 | Slack KPI 알림 자동화 | 일일 KPI 메시지 · Webhook 발송 | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Reasonofmoon/hexa-1/blob/main/notebooks/W07_slack_alert.ipynb) |
| W8 | Google Sheets KPI 연동 | 실시간 Sheets 업데이트 · CSV fallback | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Reasonofmoon/hexa-1/blob/main/notebooks/W08_sheets_kpi.ipynb) |

### Layer 3 · Intelligence (W9~W12) — 자동화 운영 시스템

> **Wow**: 이상 발생 시 **Slack 자동 알림 → 협력사 메일 → 대시보드 업데이트** 파이프라인 원클릭 완성

| 주차 | 주제 | 핵심 출력물 | Colab |
|------|------|------------|-------|
| W9 | 예지보전 & 이상감지 | 3σ 이상감지 · 설비 경보 자동 생성 | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Reasonofmoon/hexa-1/blob/main/notebooks/W09_predictive.ipynb) |
| W10 | 협력사 커뮤니케이션 | 이슈별 공문 3종 · ZIP 다운로드 | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Reasonofmoon/hexa-1/blob/main/notebooks/W10_vendor_comm.ipynb) |
| W11 | 종합 AI 대시보드 | 4패널 경영진 차트 · AI 인사이트 | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Reasonofmoon/hexa-1/blob/main/notebooks/W11_mfg_dashboard.ipynb) |
| W12 | 12주 성과 발표 Cockpit | 도입전후 KPI 비교 · 경영진 보고서 자동 생성 | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Reasonofmoon/hexa-1/blob/main/notebooks/W12_cockpit.ipynb) |

---

## 🎯 수준별 활용 가이드

### 🟢 Starter — "5분 안에 첫 AI 결과"
> AX 진단점수 10~24점 · 코딩 경험 없음

1. [W1 노트북](https://colab.research.google.com/github/Reasonofmoon/hexa-1/blob/main/notebooks/W01_mfg_ax_diagnosis.ipynb) 클릭 → Google Colab에서 열기
2. `GEMINI_API_KEY` 입력 ([발급](https://aistudio.google.com/apikey))
3. `FACTORY_INFO`에 공장명·제품·담당자만 입력 (`✏️` 표시 찾기)
4. `Ctrl+F9` (전체 실행) → 진단 레이더 차트 + 로드맵 자동 생성

### 🔵 Professional — "내 공장 데이터로 실전 분석"
> AX 진단점수 25~39점 · 기초 Excel 가능

1. `shared/manufacturing_kpi_sample.csv` 구조 확인
2. 내 공장 KPI 데이터를 같은 형식으로 준비 (불량수/OEE/납품률)
3. W5~W6 노트북에서 CSV 업로드 → OEE·불량률 자동 계산
4. W7 노트북에서 Slack Webhook 연결 → 일일 KPI 자동 발송

```bash
# CLI 스크립트 직접 사용
python scripts/kpi_calculator.py --input shared/manufacturing_kpi_sample.csv
python scripts/oee_calculator.py --input data.csv --output results.csv
python scripts/slack_kpi_sender.py --webhook [YOUR_WEBHOOK_URL]
```

### 🟣 Enterprise — "12주 파이프라인 완성 & 팀 표준화"
> AX 진단점수 40~50점 · 자동화 확장 목표

1. `scripts/M9_demo_runner.py` 실행 → 전체 파이프라인 원클릭 시연
2. W8 Sheets API 연동으로 실시간 KPI 대시보드 구축
3. W11~W12를 내부 서버(Flask/Streamlit)로 배포 → 팀 공유
4. hexa-2~6과 교차 벤치마킹 → 업종 간 AX 비교 분석

---

## 🔧 확장 우선순위

| 우선순위 | 커스터마이징 | 난이도 | 영향 범위 |
|----------|--------------|--------|-----------|
| **1st** | `FACTORY_INFO` 딕셔너리 수정 | ⭐ | 회사명·제품·날짜 |
| **2nd** | 샘플 CSV를 실제 공장 데이터로 교체 | ⭐⭐ | 분석 결과 전체 |
| **3rd** | Slack Webhook URL 연결 | ⭐⭐ | 실시간 알림 자동화 |
| **4th** | Google Sheets API 인증 설정 | ⭐⭐⭐ | 경영진 대시보드 |
| **5th** | W11~W12 Flask 서버 배포 | ⭐⭐⭐ | 팀 표준 시스템 |

---

## 📂 프로젝트 구조

```
hexa-1/
├── notebooks/              ← 12주 Colab 실습 노트북
│   ├── W01_mfg_ax_diagnosis.ipynb      # W1: AX 자가진단
│   ├── W02_defect_classifier.ipynb     # W2: 불량 AI 분류기
│   ├── W03_delivery_doc.ipynb          # W3: 납품 문서 자동화
│   ├── W04_HR_automation.ipynb         # W4: HR 문서 생성
│   ├── W05_KPI_analysis.ipynb          # W5: KPI 분석
│   ├── W06_OEE_analysis.ipynb          # W6: OEE 트렌드
│   ├── W07_slack_alert.ipynb           # W7: Slack 알림
│   ├── W08_sheets_kpi.ipynb            # W8: Sheets 연동
│   ├── W09_predictive.ipynb            # W9: 예지보전
│   ├── W10_vendor_comm.ipynb           # W10: 협력사 소통
│   ├── W11_mfg_dashboard.ipynb         # W11: 종합 대시보드
│   └── W12_cockpit.ipynb               # W12: 성과 발표
├── scripts/                ← CLI 실행 Python 스크립트
│   ├── kpi_calculator.py               # KPI 불량률 계산기
│   ├── oee_calculator.py               # OEE 자동 계산
│   ├── slack_kpi_sender.py             # Slack KPI 발송
│   ├── defect_classifier.py            # 불량 분류기
│   ├── sheets_kpi_template.py          # Sheets 연동
│   ├── hr_doc_generator.py             # HR 문서 생성
│   └── M9_demo_runner.py               # 원클릭 전체 데모
├── shared/                 ← 실습 데이터
│   ├── manufacturing_kpi_sample.csv    # KPI 샘플 (불량/OEE/납품)
│   └── delivery_reviews_sample.csv     # 협력사 리뷰 샘플
└── labs/                   ← 보조 실습 가이드
```

---

## 🚀 빠른 시작

```bash
# 1. 레포 클론
git clone https://github.com/Reasonofmoon/hexa-1.git && cd hexa-1

# 2. 로컬 환경 설정 (Colab 사용 시 불필요)
pip install google-generativeai pandas matplotlib gspread requests

# 3. W1 바로 시작 (Colab)
```

[![W1 AX진단](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Reasonofmoon/hexa-1/blob/main/notebooks/W01_mfg_ax_diagnosis.ipynb)
[![W5 KPI분석](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Reasonofmoon/hexa-1/blob/main/notebooks/W05_KPI_analysis.ipynb)
[![W9 예지보전](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Reasonofmoon/hexa-1/blob/main/notebooks/W09_predictive.ipynb)
[![W12 성과발표](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Reasonofmoon/hexa-1/blob/main/notebooks/W12_cockpit.ipynb)

---

## 🔗 전체 AX 시리즈 (hexa-1~6)

| 레포 | 섹터 | 핵심 AI 자동화 | 링크 |
|------|------|---------------|------|
| **hexa-1** (현재) | 🏭 제조업 | 불량분류·OEE·예지보전 | — |
| hexa-2 | 🍽️ F&B | 리뷰분석·메뉴카피·재고예측 | [→](https://github.com/Reasonofmoon/hexa-2) |
| hexa-3 | 🛒 소매/이커머스 | 상품카피·CRM·SEO분석 | [→](https://github.com/Reasonofmoon/hexa-3) |
| hexa-4 | 📚 교육/학원 | 교안자동화·성적분석·챗봇 | [→](https://github.com/Reasonofmoon/hexa-4) |
| hexa-5 | 🏗️ 건설/시공 | 계약서·공정KPI·안전점검 | [→](https://github.com/Reasonofmoon/hexa-5) |
| hexa-6 | 💼 IT서비스 | 제안서·코드리뷰·인시던트 | [→](https://github.com/Reasonofmoon/hexa-6) |

---

## 🌐 다국어 지원

| 항목 | 현황 |
|------|------|
| 노트북 UI | 🇰🇷 한국어 |
| 스크립트 출력 | 한국어 (컬럼 한/영 자동감지) |
| 샘플 데이터 | 한국어 컬럼명 |
| README | 한국어 / English (예정) |

---

*AX Consulting Curriculum © 2026 | Powered by Google Gemini 2.0 Flash*
