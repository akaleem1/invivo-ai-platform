from pydantic import BaseModel

class Compound(BaseModel):
    compound: str
    molecular_weight: float
    logP: float
    h_donors: int
    h_acceptors: int
    tpsa: float
    toxicity_label: int