import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

DATA_PATH = Path("data/processed/toxicity_dataset.csv")

DATABASE_URL = "postgresql://postgres:postgres123@localhost:5432/invivo_ai"

def load_dataset():

    df = pd.read_csv(DATA_PATH)

    print("Dataset shape:", df.shape)

    return df


def connect_db():

    engine = create_engine(DATABASE_URL)

    print("Connected to database")

    return engine


def upload_table(df, engine):

    df.to_sql(
        "compounds",
        engine,
        if_exists="replace",
        index=False
    )

    print("Data uploaded to Postgres table: compounds")


def main():

    df = load_dataset()

    engine = connect_db()

    upload_table(df, engine)


if __name__ == "__main__":
    main()