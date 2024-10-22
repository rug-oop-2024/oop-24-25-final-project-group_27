import streamlit as st
import pandas as pd

from app.core.system import AutoMLSystem
from autoop.core.ml.dataset import Dataset

automl = AutoMLSystem.get_instance()

datasets = automl.registry.list(type="dataset")

# your code here
st.write("Upload a CSV for processing.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    #Convert the given CSV into a Pandas DF to work with later
    df = pd.read_csv(uploaded_file)
    st.write(df)


