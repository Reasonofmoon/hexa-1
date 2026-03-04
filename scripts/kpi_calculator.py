"""Manufacturing KPI calculator for M7 hands-on practice."""

from __future__ import annotations


def calc_defect_rate(total: int, defective: int) -> float:
    """Return defect rate percentage (0-100)."""
    if total <= 0:
        raise ValueError("total must be greater than 0")
    if defective < 0:
        raise ValueError("defective must be 0 or greater")
    if defective > total:
        raise ValueError("defective cannot be greater than total")
    return (defective / total) * 100.0


def report_improvement() -> None:
    """Prompt before/after inputs and print an improvement report."""
    print("=== Manufacturing Defect Rate Improvement Report ===")
    before_total = int(input("Before - total units: ").strip())
    before_defective = int(input("Before - defective units: ").strip())
    after_total = int(input("After  - total units: ").strip())
    after_defective = int(input("After  - defective units: ").strip())

    before_rate = calc_defect_rate(before_total, before_defective)
    after_rate = calc_defect_rate(after_total, after_defective)
    delta_pp = before_rate - after_rate
    reduction_pct = (delta_pp / before_rate * 100.0) if before_rate > 0 else 0.0

    print()
    print("----- Result -----")
    print(f"Before defect rate : {before_rate:.2f}%")
    print(f"After defect rate  : {after_rate:.2f}%")
    print(f"Improvement (p.p.) : {delta_pp:.2f}p")
    print(f"Reduction (%)      : {reduction_pct:.2f}%")


if __name__ == "__main__":
    report_improvement()
