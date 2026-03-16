from fastapi import FastAPI
from sqlalchemy import create_engine
from .schemas import Compound
import pandas as pd

DATABASE_URL = "postgresql://postgres:postgres123@localhost:5432/invivo_ai"

engine = create_engine(DATABASE_URL)

app = FastAPI(title="InVivo AI Data Platform")

@app.get("/")
def home():
    return {"message": "InVivo AI Data Platform API running"}

#Create Endpoint to Retrieve Compounds
@app.get("/compounds", response_model=list[Compound])
def get_compounds():

    query = "SELECT * FROM compounds LIMIT 50"

    df = pd.read_sql(query, engine)

    return df.to_dict(orient="records")

#Create Toxicity Endpoint
@app.get("/toxicity/{compound_name}")
def get_compound(compound_name: str):

    query = f"""
    SELECT *
    FROM compounds
    WHERE compound = '{compound_name}'
    """

    df = pd.read_sql(query, engine)

    return df.to_dict(orient="records")

#Filtering Endpoint
@app.get("/filter")
def filter_compounds(min_logp: float = 0, max_logp: float = 10):

    query = f"""
    SELECT *
    FROM compounds
    WHERE logP BETWEEN {min_logp} AND {max_logp}
    """

    df = pd.read_sql(query, engine)

    return df.to_dict(orient="records")

#Toxic Compounds Endpoint
@app.get("/toxic")
def toxic_compounds():

    query = """
    SELECT *
    FROM compounds
    WHERE toxicity_label = 1
    """

    df = pd.read_sql(query, engine)

    return df.to_dict(orient="records")