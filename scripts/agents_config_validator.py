"""AGENTS.md section validator for M10 hands-on practice."""

from __future__ import annotations

from pathlib import Path


REQUIRED_SECTIONS: dict[str, tuple[str, ...]] = {
    "역할": ("역할", "role"),
    "규칙": ("규칙", "rule", "rules"),
    "프로젝트 구조": ("프로젝트 구조", "project structure"),
    "우선순위 과제": ("우선순위 과제", "priority task", "priority tasks"),
}


def validate_agents_md(filepath: str | Path) -> bool:
    """Check whether AGENTS.md contains all required sections."""
    path = Path(filepath)
    if not path.exists():
        print(f"경고: 파일을 찾을 수 없습니다 - {path}")
        return False

    content = path.read_text(encoding="utf-8")
    headings = [
        line.strip().lower()
        for line in content.splitlines()
        if line.strip().startswith("#")
    ]

    missing: list[str] = []
    for section_name, keywords in REQUIRED_SECTIONS.items():
        if not any(any(keyword in heading for keyword in keywords) for heading in headings):
            missing.append(section_name)

    if missing:
        print("경고: 필수 섹션이 누락되었습니다.")
        for section in missing:
            print(f"- {section}")
        return False

    print("검증 통과")
    return True


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        raise SystemExit("Usage: python agents_config_validator.py <AGENTS.md path>")
    validate_agents_md(sys.argv[1])
