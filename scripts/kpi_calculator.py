"""Manufacturing KPI calculator for M7 hands-on practice.

사용법:
  # 인터랙티브 모드 (직접 입력)
  python kpi_calculator.py

  # CSV 자동 분석 모드
  python kpi_calculator.py --input shared/manufacturing_kpi_sample.csv --period 2025-07-01
"""

from __future__ import annotations

import argparse
from pathlib import Path


def calc_defect_rate(total: int | float, defective: int | float) -> float:
    """Return defect rate percentage (0-100)."""
    if total <= 0:
        raise ValueError("total must be greater than 0")
    if defective < 0:
        raise ValueError("defective must be 0 or greater")
    if defective > total:
        raise ValueError("defective cannot be greater than total")
    return round((defective / total) * 100.0, 2)


def analyze_csv(csv_path: str | Path, period_date: str | None = None) -> None:
    """CSV 파일에서 도입 전/후 불량률을 자동 분석하여 보고서를 출력.
    
    CSV 컬럼: 날짜, 총_생산량, 불량_수 (또는 date, total, defective)
    """
    import csv
    from datetime import datetime

    rows = []
    path = Path(csv_path)
    with path.open("r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        # 컬럼 자동 감지
        col_date   = next((c for c in fieldnames if c in ("날짜", "date", "Date")), None)
        col_total  = next((c for c in fieldnames if c in ("총_생산량", "total", "Total")), None)
        col_defect = next((c for c in fieldnames if c in ("불량_수", "defective", "Defective")), None)

        if not all([col_date, col_total, col_defect]):
            print(f"[오류] 필요한 컬럼을 찾을 수 없습니다. 발견된 컬럼: {fieldnames}")
            return
        for row in reader:
            rows.append(row)

    if period_date:
        cutoff = datetime.strptime(period_date, "%Y-%m-%d")
        before = [r for r in rows if datetime.strptime(r[col_date].strip(), "%Y-%m-%d") < cutoff]
        after  = [r for r in rows if datetime.strptime(r[col_date].strip(), "%Y-%m-%d") >= cutoff]
    else:
        mid = len(rows) // 2
        before, after = rows[:mid], rows[mid:]

    def totals(group):
        t = sum(float(r[col_total]) for r in group)
        d = sum(float(r[col_defect]) for r in group)
        return t, d

    bt, bd = totals(before)
    at, ad = totals(after)
    before_rate = calc_defect_rate(bt, bd)
    after_rate  = calc_defect_rate(at, ad)
    delta       = round(before_rate - after_rate, 2)
    reduction   = round(delta / before_rate * 100, 1) if before_rate > 0 else 0.0

    print("=" * 40)
    print("  📊 AI 도입 전/후 불량률 분석 보고서")
    print("=" * 40)
    print(f"  데이터 파일 : {path.name}")
    print(f"  분석 기준일 : {period_date or '자동(중간 분할)'}")
    print(f"  도입 전 기간: {len(before)}행 / 총생산 {bt:,.0f}개 / 불량 {bd:,.0f}개")
    print(f"  도입 후 기간: {len(after)}행 / 총생산 {at:,.0f}개 / 불량 {ad:,.0f}개")
    print("-" * 40)
    print(f"  도입 전 불량률 : {before_rate:.2f}%")
    print(f"  도입 후 불량률 : {after_rate:.2f}%")
    print(f"  개선 (p.p.)   : -{delta:.2f}%p")
    print(f"  개선율        : {reduction:.1f}% 감소")
    print("=" * 40)


def report_improvement() -> None:
    """인터랙티브 모드: 직접 숫자를 입력해서 전/후 불량률 비교."""
    print("=== 제조업 불량률 개선 보고서 (수동 입력) ===")
    before_total     = float(input("도입 전 - 총 생산량: ").strip())
    before_defective = float(input("도입 전 - 불량 수  : ").strip())
    after_total      = float(input("도입 후 - 총 생산량: ").strip())
    after_defective  = float(input("도입 후 - 불량 수  : ").strip())

    before_rate  = calc_defect_rate(before_total, before_defective)
    after_rate   = calc_defect_rate(after_total,  after_defective)
    delta_pp     = round(before_rate - after_rate, 2)
    reduction    = round(delta_pp / before_rate * 100, 1) if before_rate > 0 else 0.0

    print()
    print("----- 결과 -----")
    print(f"도입 전 불량률 : {before_rate:.2f}%")
    print(f"도입 후 불량률 : {after_rate:.2f}%")
    print(f"개선 (p.p.)   : -{delta_pp:.2f}%p")
    print(f"개선율        : {reduction:.1f}%")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="제조업 KPI 불량률 분석기")
    parser.add_argument("--input", "-i", help="CSV 파일 경로 (없으면 인터랙티브 모드)")
    parser.add_argument("--period", "-p", help="AI 도입 기준일 (YYYY-MM-DD)")
    args = parser.parse_args()

    if args.input:
        analyze_csv(args.input, args.period)
    else:
        report_improvement()
