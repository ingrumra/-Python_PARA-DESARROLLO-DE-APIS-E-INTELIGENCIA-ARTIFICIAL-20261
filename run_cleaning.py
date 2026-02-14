"""Ejecutable local (Semana 1).

Uso:
    python -m scripts.run_cleaning
"""

from __future__ import annotations

from pathlib import Path

from src.io import read_raw_semicolon_csv, write_csv
from src.cleaning import clean_pipeline


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "cancer_mama_piii_2023_raw.csv"
OUT = ROOT / "data" / "processed" / "cancer_mama_piii_2023_clean.csv"


def main() -> None:
    df_raw = read_raw_semicolon_csv(str(RAW))
    df_clean = clean_pipeline(df_raw)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    write_csv(df_clean, str(OUT))
    print(f"OK: {len(df_clean):,} filas -> {OUT}")


if __name__ == "__main__":
    main()
