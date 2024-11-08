import streamlit as st
import pandas as pd
import ast  # To safely convert input string to a dictionary
import uuid  # For generating unique IDs

from app.core.system import AutoMLSystem
from autoop.core.ml.dataset import Dataset
from app.core.system import ArtifactRegistry

# Get an instance of AutoMLSystem and access the registry
automl = AutoMLSystem.get_instance()

# Display a prompt to upload a CSV file
st.write("Upload a CSV for processing.")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    # Read the uploaded CSV file into a DataFrame
    data = pd.read_csv(uploaded_file)

    # Input for the dataset name
    name = st.text_input("Enter a name for your dataset")
    
    # Input for tags (simple string)
    tags = st.text_input("Enter the tags for the dataset.")

    # Automatically generate metadata with unique experiment_id and run_id
    metadata = {
        "experiment_id": str(uuid.uuid4()),
        "run_id": str(uuid.uuid4())
    }
    
    # If the user clicks the "Create Dataset" button and provides a name
    if st.button("Create Dataset") and name:
        # Create a new Dataset instance from the uploaded CSV
        new_dataset = Dataset.from_dataframe(data, name=name, asset_path=f"{name}.csv", tags=tags, metadata=metadata)

        # Register the dataset with the registry
        automl.registry.register(new_dataset)
        
        # Display success message
        st.success(f"Dataset '{name}' created and saved successfully!")

        # Optionally, refresh the list of datasets after registration
        datasets = automl.registry.list(type="dataset")
        st.write(datasets)

else:
    st.write("Please upload a CSV to continue.")