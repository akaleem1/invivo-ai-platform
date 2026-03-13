from sqlalchemy import create_engine
import pandas as pd

DATABASE_URL = "postgresql://postgres:postgres123@localhost:5432/invivo_ai"

engine = create_engine(DATABASE_URL)

query = """
SELECT *
FROM compounds
LIMIT 10
"""

df = pd.read_sql(query, engine)

print(df)