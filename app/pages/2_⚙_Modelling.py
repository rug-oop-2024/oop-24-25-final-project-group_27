import streamlit as st
import pandas as pd

from app.core.system import AutoMLSystem
from autoop.core.ml.dataset import Dataset
from autoop.functional.feature import detect_feature_types


st.set_page_config(page_title="Modelling", page_icon="📈")

def write_helper_text(text: str):
    st.write(f"<p style=\"color: #888;\">{text}</p>", unsafe_allow_html=True)

st.write("# ⚙ Modelling")
write_helper_text("In this section, you can design a machine learning pipeline to train a model on a dataset.")

automl = AutoMLSystem.get_instance()

datasets = automl.registry.list(type="dataset")

# your code here
if datasets:
    # Create a list of dataset names
    dataset_names = [dataset.name for dataset in datasets]  # Assuming each dataset has a `name` attribute

    # Display the selectbox for choosing a dataset
    selected_dataset_name = st.selectbox("Select a dataset:", dataset_names)

    # Retrieve the selected dataset from the list
    selected_dataset = next((ds for ds in datasets if ds.name == selected_dataset_name), None)

    if selected_dataset:
        # Retrieve the Data set using id
        retrieved_dataset = automl.registry.get_dataset(selected_dataset.id)

        data = retrieved_dataset.read()

        # Optionally, load the dataset into a DataFrame and display a preview
        try:
            #get a  pandasdataframe here
            st.write("### Dataset Preview")
            st.write(data.head())  # Show only the first few rows
        except Exception as e:
            st.error(f"Could not load data from the artifact. Error: {e}")
        
        #Check feature types so that after user selects features we can detect the task
        detect_features = detect_feature_types(retrieved_dataset)

else:
    # If no datasets are available, show a message
    st.write("No datasets available. Please add a dataset first.")