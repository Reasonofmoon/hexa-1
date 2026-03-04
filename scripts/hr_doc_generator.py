"""W4 HR document generator (template-based, no API)."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path


TEMPLATES: dict[str, dict[str, str]] = {
    "job": {
        "title": "[{company}] {position} 채용공고",
        "회사소개": "{company}는 데이터 기반 혁신을 통해 고객 문제를 해결하는 조직입니다.",
        "자격요건": "관련 직무 경험 또는 직무 이해도가 있는 분\n원활한 협업/커뮤니케이션 역량을 갖춘 분",
        "업무내용": "{position} 관련 기획/운영/개선 업무 수행\n부서 간 협업을 통한 프로젝트 실행 및 성과 관리",
        "복리후생": "유연근무제, 교육비 지원, 성과 인센티브, 장기근속 포상",
    },
    "work": {
        "title": "[{company}] 작업지시서",
        "지시번호": "WO-{date}-{seq}",
        "작업내용": "{position} 관련 우선 과제를 표준 절차에 따라 수행",
        "담당자": "{position} 담당자",
        "기한": "{deadline}",
        "안전수칙": "작업 전 안전 점검표 확인\n보호장비 착용\n이상 발생 시 즉시 보고",
    },
}


def _build_job_posting(company: str, position: str) -> str:
    t = TEMPLATES["job"]
    lines = [
        t["title"].format(company=company, position=position),
        "=" * 50,
        f"[회사소개]\n{t['회사소개'].format(company=company, position=position)}",
        f"[자격요건]\n{t['자격요건'].format(company=company, position=position)}",
        f"[업무내용]\n{t['업무내용'].format(company=company, position=position)}",
        f"[복리후생]\n{t['복리후생'].format(company=company, position=position)}",
    ]
    return "\n\n".join(lines)


def _build_work_order(company: str, position: str) -> str:
    t = TEMPLATES["work"]
    now = datetime.now()
    issue_no = t["지시번호"].format(date=now.strftime("%Y%m%d"), seq=now.strftime("%H%M"))
    deadline = (now.replace(hour=18, minute=0, second=0, microsecond=0)).strftime("%Y-%m-%d %H:%M")

    lines = [
        t["title"].format(company=company, position=position),
        "=" * 50,
        f"[지시번호]\n{issue_no}",
        f"[작업내용]\n{t['작업내용'].format(company=company, position=position)}",
        f"[담당자]\n{t['담당자'].format(company=company, position=position)}",
        f"[기한]\n{t['기한'].format(company=company, position=position, deadline=deadline)}",
        f"[안전수칙]\n{t['안전수칙'].format(company=company, position=position)}",
    ]
    return "\n\n".join(lines)


def generate_document(doc_type: str, company: str, position: str) -> str:
    if doc_type == "job":
        return _build_job_posting(company, position)
    return _build_work_order(company, position)


def save_text(text: str, output_path: str) -> Path:
    path = Path(output_path)
    if path.suffix.lower() != ".txt":
        path = path.with_suffix(".txt")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="채용공고/작업지시서 템플릿 생성기")
    parser.add_argument("--type", choices=["job", "work"], required=True, help="문서 타입: job 또는 work")
    parser.add_argument("--company", required=True, help="회사명")
    parser.add_argument("--position", required=True, help="직무명")
    parser.add_argument("--output", help="저장 경로(.txt), 생략 시 파일 저장 없음")
    args = parser.parse_args()

    result = generate_document(args.type, args.company, args.position)

    print(result)

    if args.output:
        saved = save_text(result, args.output)
        print(f"\n[저장 완료] {saved}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
