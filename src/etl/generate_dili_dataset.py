import pandas as pd
import numpy as np
from pathlib import Path

OUTPUT_PATH = Path("data/raw/dili.csv")

np.random.seed(42)

n_samples = 500

compounds = [f"compound_{i}" for i in range(n_samples)]

data = pd.DataFrame({
    "compound": compounds,
    "molecular_weight": np.random.normal(350, 80, n_samples),
    "logP": np.random.normal(3, 1, n_samples),
    "h_donors": np.random.randint(0, 6, n_samples),
    "h_acceptors": np.random.randint(1, 10, n_samples),
    "tpsa": np.random.normal(90, 30, n_samples)
})

# simulate toxicity probability

toxicity_score = (
    0.4 * (data["logP"] > 3).astype(int) +
    0.4 * (data["molecular_weight"] > 380).astype(int) +
    0.2 * (data["tpsa"] > 100).astype(int) +
    np.random.normal(0,0.15,n_samples)
)

data["toxicity_label"] = (toxicity_score > 0.4).astype(int)

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

data.to_csv(OUTPUT_PATH, index=False)

print("Dataset saved to:", OUTPUT_PATH)
print("Shape:", data.shape)
print("\nClass balance:")
print(data["toxicity_label"].value_counts())