"""
Generates one Jekyll collection page (_works/<id>.md) per row in the
metadata CSV. Run this before `jekyll build` / `jekyll serve`.

Usage:
    python scripts/generate_works.py

If your CSV uses different column names, just update COLUMNS below —
no other changes needed.
"""

import pandas as pd
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = REPO_ROOT / "_data" / "metadata.csv"
WORKS_DIR = REPO_ROOT / "_works"

# Map your CSV's actual column names here if they differ from these.
COLUMNS = {
    "id": "id",
    "composer": "composer",
    "title": "title",
    "editor": "editor",
    "date": "date",
    "source": "source",
    "mei_file": "mei_file",
}


def escape_yaml(value: str) -> str:
    """Wrap a value in double quotes and escape any internal quotes."""
    return '"' + str(value).replace('"', '\\"') + '"'


def main():
    df = pd.read_csv(CSV_PATH, dtype=str).fillna("")

    WORKS_DIR.mkdir(exist_ok=True)

    for _, row in df.iterrows():
        front_matter = "\n".join(
            f"{key}: {escape_yaml(row[csv_col])}"
            for key, csv_col in COLUMNS.items()
            if key != "id"
        )

        page_content = f"---\n{front_matter}\n---\n"

        out_path = WORKS_DIR / f"{row[COLUMNS['id']]}.md"
        out_path.write_text(page_content, encoding="utf-8")

    print(f"Generated {len(df)} work pages in {WORKS_DIR}")


if __name__ == "__main__":
    main()
