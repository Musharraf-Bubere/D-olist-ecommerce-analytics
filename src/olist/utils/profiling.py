import pandas as pd


def profile(df: pd.DataFrame, name: str = "") -> None:
    """Print a quick summary: shape, dtypes, missing values, duplicates."""
    print(f"=== {name} ===")
    print(f"Rows: {df.shape[0]:,} | Columns: {df.shape[1]}")
    print(f"Duplicate rows: {df.duplicated().sum():,}")

    summary = pd.DataFrame({
        "dtype": df.dtypes.astype(str),
        "missing": df.isna().sum(),
        "missing_%": (df.isna().mean() * 100).round(2),
        "unique": df.nunique(),
    })
    print(summary)
    print()