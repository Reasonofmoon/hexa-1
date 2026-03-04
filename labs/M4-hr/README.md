# M4-hr 실습 가이드: 채용공고&작업지시서 자동화

## 오늘 실습 목표
1. 생산 라인 특성에 맞는 채용공고를 자동 생성한다
2. 작업자 역량에 기반한 작업지시서를 작성한다
3. HR 문서 템플릿을 표준화한다

---

## 🟢 Starter: 프롬프트만으로 (코딩 없음)

아래를 ChatGPT/뤼튼에 그대로 붙여넣고, `[]` 부분만 바꾸세요:

```
당신은 제조업 HR 전문가입니다.
우리 공장(업종: [금속가공], 라인: [프레스])의 채용공고를 작성해주세요.

직무: [생산 기술원]
근무 조건:
- 근무 시간: [주 5일, 09:00-18:00]
- 급여: [월 250만원]
- 복지: [4대 보험, 퇴직금, 연차]

요청 자격사항:
- [경력: 신입/경력무관]
- [학력: 고졸 이상]
- [우대: 산업안전기사 자격증]

작업지시서도 함께 작성해주세요.
```

---

## 🔵 Professional: Colab 실행 (5단계)

**1단계**: Colab 뱃지 클릭 → 노트북 오픈  
**2단계**: `HR_INFO` 셀에서 직무·근무조건·자격요건 수정  
**3단계**: 런타임 → 모두 실행  
**4단계**: 채용공고와 작업지시서 자동 생성 확인  
**5단계**: 워드/한글 형식 문서 자동 다운로드 ✅

---

## 🔥 확장 과제 2개

**과제 1 — 지원자 자동 스크리닝**
```python
# 이력서 키워드 추출으로 적합도 자동 평가
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match_score(job_desc, resume):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([job_desc, resume])
    return cosine_similarity(vectors[0], vectors[1])[0][0]

applicant_score = calculate_match_score(job_description, resume_text)
```

**과제 2 — 개인화된 작업지시서 생성**
```python
# 작업자 역량별 맞춤 지시서 생성
def generate_personalized_instructions(worker_profile, task_info):
    skill_level = worker_profile['skill_level']
    experience = worker_profile['experience_years']
    
    if skill_level == '초급':
        instructions = generate_detailed_instructions(task_info)
    elif skill_level == '중급':
        instructions = generate_standard_instructions(task_info)
    else:
        instructions = generate_advanced_instructions(task_info)
    
    return instructions
```