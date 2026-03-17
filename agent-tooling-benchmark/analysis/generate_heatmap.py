"""
Generate a colour-coded heatmap of tool performance across dimensions.
Reads the summary table from aggregate_scores.py output or directly
from the scoring CSV.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
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

DISPLAY_LABELS = [
    "Correctness",
    "Stat. Validity",
    "Reproducibility",
    "Code Quality",
    "Efficiency",
    "Safety",
]

TOOL_DISPLAY = {
    "claude_code": "Claude Code",
    "chatgpt": "ChatGPT/Codex",
    "copilot": "GitHub Copilot",
    "antigravity": "Antigravity",
    "gemini": "Gemini",
}


def load_summary(path: str) -> pd.DataFrame:
    """Load summary table CSV (output of aggregate_scores.py)."""
    df = pd.read_csv(path, index_col=0)
    return df


def generate_heatmap(df: pd.DataFrame, output_path: str = "report/figures/heatmap.png"):
    """Create and save the heatmap figure."""
    # Extract just the dimension columns
    data = df[DIMENSIONS].copy()

    # Rename for display
    tools = [TOOL_DISPLAY.get(t, t) for t in data.index]
    data.index = tools
    data.columns = DISPLAY_LABELS

    fig, ax = plt.subplots(figsize=(10, 5))

    # Custom colourmap: red (0) -> yellow (1.5) -> green (3)
    cmap = mcolors.LinearSegmentedColormap.from_list(
        "rubric", ["#d32f2f", "#fbc02d", "#388e3c"], N=256
    )

    im = ax.imshow(data.values, cmap=cmap, vmin=0, vmax=3, aspect="auto")

    # Axis labels
    ax.set_xticks(range(len(DISPLAY_LABELS)))
    ax.set_xticklabels(DISPLAY_LABELS, rotation=45, ha="right", fontsize=11)
    ax.set_yticks(range(len(tools)))
    ax.set_yticklabels(tools, fontsize=11)

    # Annotate cells with values
    for i in range(len(tools)):
        for j in range(len(DISPLAY_LABELS)):
            val = data.values[i, j]
            if not np.isnan(val):
                text_color = "white" if val < 1.0 or val > 2.5 else "black"
                ax.text(j, i, f"{val:.1f}", ha="center", va="center",
                        fontsize=12, fontweight="bold", color=text_color)

    # Colourbar
    cbar = plt.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label("Score (0-3)", fontsize=11)
    cbar.set_ticks([0, 1, 2, 3])
    cbar.set_ticklabels(["0 (Fail)", "1 (Poor)", "2 (Adequate)", "3 (Strong)"])

    ax.set_title("Agent Tool Performance by Evaluation Dimension", fontsize=14, pad=15)
    plt.tight_layout()

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    print(f"Heatmap saved to {output_path}")
    plt.close()


def main():
    summary_path = sys.argv[1] if len(sys.argv) > 1 else "analysis/summary_table.csv"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "report/figures/heatmap.png"

    if not Path(summary_path).exists():
        print(f"Summary table not found at {summary_path}.")
        print("Run aggregate_scores.py first to generate it.")
        return

    df = load_summary(summary_path)
    generate_heatmap(df, output_path)


if __name__ == "__main__":
    main()
