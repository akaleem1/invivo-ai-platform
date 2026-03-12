import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/tggates_subset.csv")
PROCESSED_PATH = Path("data/processed/tggates_clean.csv")

def load_data():
    print("Loading TG-GATEs subset...")
    df = pd.read_csv(RAW_PATH)
    return df

def clean_data(df):
    print("Cleaning dataset...")

    # Drop duplicates
    df = df.drop_duplicates()

    # Ensure column names are lowercase
    df.columns = df.columns.str.lower()

    # Convert toxicity label to int
    df["toxicity_label"] = df["toxicity_label"].astype(int)

    return df

def save_data(df):
    df.to_csv(PROCESSED_PATH, index=False)
    print(f"Saved cleaned dataset to {PROCESSED_PATH}")

def run_pipeline():
    df = load_data()
    df = clean_data(df)
    save_data(df)
    print("ETL pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()