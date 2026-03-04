# M3-delivery-doc 실습 가이드: 납품 문서 자동 생성

## 오늘 실습 목표
1. 생산 데이터를 기반으로 납품 문서를 자동 생성한다
2. 규격서와 검사 성적서를 템플릿화한다
3. 고객 요구사항에 맞춰 문서를 커스터마이징한다

---

## 🟢 Starter: 프롬프트만으로 (코딩 없음)

아래를 ChatGPT/뤼튼에 그대로 붙여넣고, `[]` 부분만 바꾸세요:

```
당신은 제조업 품질보증 전문가입니다.
다음 생산 정보로 납품 문서를 작성해주세요.

제품명: [차량용 센서 모듈]
주문번호: [PO-2024-0315]
생산일자: [2024-03-15]
생산량: [5,000]개
검사 항목:
- 외관검사: 합격률 [99.2%]
- 치수검사: 합격률 [98.8%]
- 성능검사: 합격률 [99.5%]

규격서와 검사 성적서 형식으로 정리해주세요.
```

---

## 🔵 Professional: Colab 실행 (5단계)

**1단계**: Colab 뱃지 클릭 → 노트북 오픈  
**2단계**: `DELIVERY_INFO` 셀에서 고객사·제품·규격 정보 수정  
**3단계**: 런타임 → 모두 실행  
**4단계**: 납품 문서 템플릿 자동 생성 확인  
**5단계**: PDF 형식 납품 문서 자동 다운로드 ✅

---

## 🔥 확장 과제 2개

**과제 1 — 다국어 납품 문서 생성**
```python
# 고객사 국적에 맞춰 문서 자동 번역
from googletrans import Translator

translator = Translator()
languages = ['ko', 'en', 'ja', 'zh']
for lang in languages:
    translated_doc = translator.translate(document_content, dest=lang)
    generate_pdf(translated_doc, f"delivery_spec_{lang}.pdf")
```

**과제 2 — 검사 데이터 자동 연동**
```python
# 검사 장비에서 실시간 데이터 수집하여 문서 자동 업데이트
import requests

def fetch_inspection_data(equipment_id):
    response = requests.get(f"http://equipment/api/data/{equipment_id}")
    return response.json()

inspection_data = fetch_inspection_data("EQ-001")
update_delivery_document(inspection_data)
```