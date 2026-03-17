"""
Analyse inter-run consistency: compare Run 1 vs Run 2 for each tool-task pair.
Reports which tools are most/least consistent and which tasks show most variance.
"""
import pandas as pd
import numpy as np
import sys

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


def analyse_consistency(df: pd.DataFrame):
    """Compare Run 1 vs Run 2 across all tool-task pairs."""
    records = []

    for (tool, task), grp in df.groupby(["tool", "task"]):
        run1 = grp[grp["run"] == "run1"]
        run2 = grp[grp["run"] == "run2"]

        if run1.empty or run2.empty:
            continue

        # Dimension-level consistency
        r1_dims = run1[DIMENSIONS].values.flatten()
        r2_dims = run2[DIMENSIONS].values.flatten()
        dim_match = np.sum(r1_dims == r2_dims)
        dim_total = len(DIMENSIONS)

        # Sub-criteria consistency
        r1_subs = run1[SUB_CRITERIA].values.flatten()
        r2_subs = run2[SUB_CRITERIA].values.flatten()
        sub_match = np.sum(r1_subs == r2_subs)
        sub_total = len(SUB_CRITERIA)

        # Mean absolute difference in dimension scores
        mad = np.nanmean(np.abs(r1_dims - r2_dims))

        records.append({
            "tool": tool,
            "task": task,
            "dim_consistency_%": round(dim_match / dim_total * 100, 1),
            "sub_consistency_%": round(sub_match / sub_total * 100, 1),
            "mean_abs_diff": round(mad, 2),
        })

    return pd.DataFrame(records)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "rubric/scoring_template.csv"
    df = load_scores(path)

    if df[DIMENSIONS].dropna(how="all").empty:
        print("No scores found. Fill in the scoring template first.")
        return

    consistency = analyse_consistency(df)

    if consistency.empty:
        print("Need both Run 1 and Run 2 scores to analyse consistency.")
        return

    print("=" * 70)
    print("INTER-RUN CONSISTENCY (per tool-task pair)")
    print("=" * 70)
    print(consistency.to_string(index=False))

    print("\n" + "=" * 70)
    print("CONSISTENCY BY TOOL (mean across tasks)")
    print("=" * 70)
    by_tool = consistency.groupby("tool").agg({
        "dim_consistency_%": "mean",
        "sub_consistency_%": "mean",
        "mean_abs_diff": "mean",
    }).round(1)
    print(by_tool.to_string())

    print("\n" + "=" * 70)
    print("CONSISTENCY BY TASK (mean across tools)")
    print("=" * 70)
    by_task = consistency.groupby("task").agg({
        "dim_consistency_%": "mean",
        "sub_consistency_%": "mean",
        "mean_abs_diff": "mean",
    }).round(1)
    print(by_task.to_string())

    # Most and least consistent
    print("\n" + "=" * 70)
    best = consistency.loc[consistency["dim_consistency_%"].idxmax()]
    worst = consistency.loc[consistency["dim_consistency_%"].idxmin()]
    print(f"Most consistent:  {best['tool']} on {best['task']} ({best['dim_consistency_%']}%)")
    print(f"Least consistent: {worst['tool']} on {worst['task']} ({worst['dim_consistency_%']}%)")


if __name__ == "__main__":
    main()
