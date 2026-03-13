import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/dili.csv")
PROCESSED_PATH = Path("data/processed/toxicity_dataset.csv")

def run_pipeline():

    df = pd.read_csv(RAW_PATH)

    df = df.dropna()

    df.to_csv(PROCESSED_PATH, index=False)

    print("Processed dataset saved")
    print("Shape:", df.shape)


if __name__ == "__main__":
    run_pipeline()