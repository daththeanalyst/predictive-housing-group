"""
Aggregate scoring data from rubric CSV into summary tables.
Reads rubric/scoring_template.csv (filled in) and produces:
  - Per-tool mean scores across all tasks
  - Per-task mean scores across all tools
  - Overall summary table (the required report artefact)
"""
import pandas as pd
import numpy as np
import sys
from pathlib import Path

DIMENSIONS = [
    "correctness",
    "statistical_validity",
    "reproducibility",
    "code_quality",
    "efficiency",
    "safety",
]

SUB_CRITERIA = ["sub1", "sub2", "sub3", "sub4", "sub5", "sub6"]


def load_scores(path: str = "rubric/scoring_template.csv") -> pd.DataFrame:
    df = pd.read_csv(path)
    for col in DIMENSIONS + SUB_CRITERIA:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def compute_consistency(df: pd.DataFrame) -> pd.DataFrame:
    """Compare Run 1 vs Run 2 scores per tool-task pair.
    Returns consistency % (fraction of sub-criteria with identical scores)."""
    records = []
    for (tool, task), grp in df.groupby(["tool", "task"]):
        if len(grp) < 2:
            continue
        run1 = grp[grp["run"] == "run1"][SUB_CRITERIA].values
        run2 = grp[grp["run"] == "run2"][SUB_CRITERIA].values
        if run1.size == 0 or run2.size == 0:
            continue
        matches = np.sum(run1 == run2)
        total = run1.size
        records.append(
            {"tool": tool, "task": task, "consistency": matches / total * 100}
        )
    return pd.DataFrame(records)


def summary_by_tool(df: pd.DataFrame) -> pd.DataFrame:
    """Mean scores per tool across all tasks (averaging both runs)."""
    return df.groupby("tool")[DIMENSIONS].mean().round(2)


def summary_by_task(df: pd.DataFrame) -> pd.DataFrame:
    """Mean scores per task across all tools (averaging both runs)."""
    return df.groupby("task")[DIMENSIONS].mean().round(2)


def overall_summary(df: pd.DataFrame) -> pd.DataFrame:
    """The report table: per-tool means + overall + consistency."""
    tool_means = summary_by_tool(df)
    tool_means["overall"] = tool_means[DIMENSIONS].mean(axis=1).round(2)

    consistency = compute_consistency(df)
    if not consistency.empty:
        tool_consistency = (
            consistency.groupby("tool")["consistency"].mean().round(1)
        )
        tool_means["consistency_%"] = tool_consistency
    else:
        tool_means["consistency_%"] = np.nan

    return tool_means


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "rubric/scoring_template.csv"
    df = load_scores(path)

    # Check if any scores are filled in
    if df[DIMENSIONS].dropna(how="all").empty:
        print("No scores found in the CSV. Fill in the scoring template first.")
        return

    print("=" * 60)
    print("SUMMARY BY TOOL (mean across all tasks)")
    print("=" * 60)
    print(summary_by_tool(df).to_string())

    print("\n" + "=" * 60)
    print("SUMMARY BY TASK (mean across all tools)")
    print("=" * 60)
    print(summary_by_task(df).to_string())

    print("\n" + "=" * 60)
    print("OVERALL SUMMARY TABLE (for report)")
    print("=" * 60)
    summary = overall_summary(df)
    print(summary.to_string())

    # Save to CSV
    out_path = Path(path).parent.parent / "analysis" / "summary_table.csv"
    summary.to_csv(out_path)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
