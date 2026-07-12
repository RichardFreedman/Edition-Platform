"""
Generates one Jekyll collection page (_works/<id>.md) per row in the
metadata CSV. Run this before `jekyll build` / `jekyll serve`.

Usage:
    python scripts/generate_works.py
"""

import pandas as pd
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = REPO_ROOT / "_data" / "metadata.csv"
WORKS_DIR = REPO_ROOT / "_works"


def escape_yaml(value: str) -> str:
    """Wrap a value in double quotes and escape any internal quotes."""
    return '"' + str(value).replace('"', '\\"') + '"'


def get_value(row, *names):
    for name in names:
        if name in row.index:
            value = row[name]
            if pd.notna(value):
                text = str(value).strip()
                if text:
                    return text
    return ""


def main():
    df = pd.read_csv(CSV_PATH, dtype=str).fillna("")
    WORKS_DIR.mkdir(exist_ok=True)

    for _, row in df.iterrows():
        composer = get_value(row, "composer", "composer_name")
        title = get_value(row, "title", "work_title")
        editor = get_value(row, "editor", "editors")
        mei_file = get_value(row, "mei_file", "filename")
        page_id = get_value(row, "id")

        if not page_id and mei_file:
            page_id = Path(mei_file).stem

        if not page_id:
            page_id = f"work-{len(df)}"

        front_matter = "\n".join(
            [
                f"composer: {escape_yaml(composer)}",
                f"title: {escape_yaml(title)}",
                f"editor: {escape_yaml(editor)}",
                f"mei_file: {escape_yaml(mei_file)}",
            ]
        )

        page_content = f"---\n{front_matter}\n---\n"
        out_path = WORKS_DIR / f"{page_id}.md"
        out_path.write_text(page_content, encoding="utf-8")

    print(f"Generated {len(df)} work pages in {WORKS_DIR}")


if __name__ == "__main__":
    main()
