"""M9 one-click demo runner for AX hands-on sessions."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

from openpyxl import Workbook


SCRIPTS_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPTS_DIR.parent


def _resolve_sample_path(preferred_rel: str, filename: str) -> Path:
    preferred = PROJECT_ROOT / preferred_rel
    if preferred.exists():
        return preferred

    candidates = [
        SCRIPTS_DIR / filename,
        PROJECT_ROOT / "hexa-1" / "shared" / filename,
        PROJECT_ROOT / "hexa-2" / "shared" / filename,
    ]
    for path in candidates:
        if path.exists():
            return path

    raise FileNotFoundError(f"샘플 파일을 찾을 수 없습니다: {filename}")


def _run_command(args: list[str]) -> int:
    result = subprocess.run(args, cwd=str(PROJECT_ROOT))
    return result.returncode


def _run_demo_1() -> int:
    print("=== [제조 KPI 분석 데모] 시작 ===", flush=True)
    sample_csv = _resolve_sample_path("shared/manufacturing_kpi_sample.csv", "manufacturing_kpi_sample.csv")
    cmd = [sys.executable, str(SCRIPTS_DIR / "kpi_calculator.py"), "--input", str(sample_csv)]
    print("실행:", " ".join(cmd), flush=True)
    return _run_command(cmd)


def _run_demo_2() -> int:
    print("=== [F&B 리뷰 자동답글 데모] 시작 ===", flush=True)
    sample_csv = _resolve_sample_path("shared/delivery_reviews_sample.csv", "delivery_reviews_sample.csv")
    cmd = [sys.executable, str(SCRIPTS_DIR / "review_auto_reply.py"), str(sample_csv)]
    print("실행:", " ".join(cmd), flush=True)
    return _run_command(cmd)


def _create_temp_excel() -> Path:
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")
    tmp_path = Path(tmp.name)
    tmp.close()

    wb = Workbook()
    ws = wb.active
    ws.title = "Report"
    ws.append(["날짜", "매출", "비용"])
    ws.append(["2026-03-01", 1200, 800])
    ws.append(["2026-03-02", 1450, 900])
    ws.append(["2026-03-03", 1380, 860])
    wb.save(tmp_path)
    wb.close()

    return tmp_path


def _run_demo_3() -> int:
    print("=== [M9 자동 리포트 데모] 시작 ===", flush=True)
    excel_path = _create_temp_excel()
    try:
        cmd = [
            sys.executable,
            str(SCRIPTS_DIR / "auto_report_generator.py"),
            str(excel_path),
            "--sheet",
            "Report",
        ]
        print("실행:", " ".join(cmd), flush=True)
        return _run_command(cmd)
    finally:
        excel_path.unlink(missing_ok=True)


def _run_demo_4() -> int:
    print("=== [AGENTS 설정 검증 데모] 시작 ===", flush=True)
    target = PROJECT_ROOT / "M2_AI_Benchmarking" / "case_studies" / "AGENTS_MFG.md"
    if not target.exists():
        raise FileNotFoundError(f"AGENTS_MFG.md 파일을 찾을 수 없습니다: {target}")
    cmd = [sys.executable, str(SCRIPTS_DIR / "agents_config_validator.py"), str(target)]
    print("실행:", " ".join(cmd), flush=True)
    return _run_command(cmd)


def main() -> int:
    print("M9 Demo Runner")
    print("1: kpi_calculator.py --input shared/manufacturing_kpi_sample.csv")
    print("2: review_auto_reply.py shared/delivery_reviews_sample.csv")
    print("3: auto_report_generator.py (샘플 데이터)")
    print("4: agents_config_validator.py (AGENTS_MFG.md)")
    choice = input("실행할 데모 번호를 선택하세요 (1-4): ").strip().lstrip("\ufeff")

    actions = {
        "1": _run_demo_1,
        "2": _run_demo_2,
        "3": _run_demo_3,
        "4": _run_demo_4,
    }
    action = actions.get(choice)
    if action is None:
        print("잘못된 선택입니다. 1~4 중 하나를 입력하세요.")
        return 1
    try:
        return action()
    except Exception as exc:
        print(f"[오류] 데모 실행 실패: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
