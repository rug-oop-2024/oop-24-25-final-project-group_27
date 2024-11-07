import streamlit as st
import pandas as pd

from app.core.system import AutoMLSystem
from autoop.core.ml.dataset import Dataset

automl = AutoMLSystem.get_instance()

datasets = automl.registry.list(type="dataset")

# your code here
st.write("Upload a CSV for processing.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

name = input("")
new_dataset = Dataset()
Dataset.from_dataframe(uploaded_file, name=name, )

