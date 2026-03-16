import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.title("InVivo AI Platform")

st.write("Interactive platform for exploring compound toxicity data")

#Load Compounds from API
response = requests.get(f"{API_URL}/compounds")

data = response.json()

df = pd.DataFrame(data)

st.subheader("Compound Dataset")

st.dataframe(df)

#Add Toxic Compounds Table
st.subheader("Toxic Compounds")

response = requests.get(f"{API_URL}/toxic")

toxic_df = pd.DataFrame(response.json())

st.dataframe(toxic_df)

#Add Feature Visualization
import matplotlib.pyplot as plt
import seaborn as sns

st.subheader("Molecular Weight Distribution")

fig, ax = plt.subplots()

sns.histplot(df["molecular_weight"], bins=20, ax=ax)

st.pyplot(fig)

#Add Interactive Filter
st.subheader("Filter Compounds by logP")

min_logp = st.slider("Minimum logP", 0.0, 6.0, 2.0)
max_logp = st.slider("Maximum logP", 0.0, 6.0, 4.0)

response = requests.get(
    f"{API_URL}/filter",
    params={"min_logp": min_logp, "max_logp": max_logp}
)

filtered_df = pd.DataFrame(response.json())

st.write("Filtered Results")

st.dataframe(filtered_df)

