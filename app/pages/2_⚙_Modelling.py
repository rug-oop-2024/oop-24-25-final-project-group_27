import streamlit as st

from app.core.system import AutoMLSystem
from autoop.functional.feature import detect_feature_types
from autoop.core.storage import NotFoundError
from autoop.core.ml.model import (
    REGRESSION_MODELS,
    CLASSIFICATION_MODELS,
    get_model
)
from autoop.core.ml.metric import (
    REGR_METRICS,
    CLAS_METRICS,
    get_metric
)
from autoop.core.ml.pipeline import Pipeline


st.set_page_config(page_title="Modelling", page_icon="📈")


def write_helper_text(text: str) -> None:
    """Writer helper function.

    Args:
        text (str): Text to write.
    """
    st.write(f"<p style=\"color: #888;\">{text}</p>", unsafe_allow_html=True)


st.write("# ⚙ Modelling")
write_helper_text("In this section, you can design a machine learning pipeline"
                  " train a model on a dataset.")

automl = AutoMLSystem.get_instance()


try:
    datasets = automl.registry.list(type="dataset")

    # Create a list of dataset names
    dataset_names = [dataset.name for dataset in datasets]
    # Display the selectbox for choosing a dataset
    selected_dataset_name = st.selectbox("Select a dataset:", dataset_names)

    # Retrieve the selected dataset from the list
    selected_dataset = next(
        (ds for ds in datasets if ds.name == selected_dataset_name),
        None
    )

    if selected_dataset:
        # Retrieve the Data set using id
        retrieved_dataset = automl.registry.get_dataset(selected_dataset.id)

        data = retrieved_dataset.read()

        # Optionally, load the dataset into a DataFrame and display a preview
        try:
            # Get a  pandasdataframe here
            st.write("### Dataset Preview")
            st.write(data.head())  # Show only the first few rows
        except Exception as e:
            st.error(f"Could not load data from the artifact. Error: {e}")

        # Check feature types so that after user selects features we can
        # detect the task
        detect_features = detect_feature_types(retrieved_dataset)

        # Let user select target feature but this cannot be one of input
        # features
        target_feature = st.selectbox(
            "Select desired target feature:", detect_features
        )

        # Remove our target feature because it cannot also be a input
        # feature
        detect_features.remove(target_feature)

        # let user select input features
        input_features = st.multiselect(
            "Select desired input features:",
            detect_features
        )

        if 'pipeline_created' not in st.session_state:
            st.session_state.pipeline_created = False
        if 'pipeline_executed' not in st.session_state:
            st.session_state.pipeline_executed = False
        if 'pipeline' not in st.session_state:
            st.session_state.pipeline = None
        if 'results' not in st.session_state:
            st.session_state.results = None

        if len(input_features) < 2:
            st.warning("Please select at least 2 input features.")
        else:
            # Check what type of target feature is to determine model type
            if target_feature.type == "categorical":
                model_task = "classification"
                available_models = CLASSIFICATION_MODELS
                available_metrics = CLAS_METRICS
            elif target_feature.type == "numerical":
                model_task = "regression"
                available_models = REGRESSION_MODELS
                available_metrics = REGR_METRICS

            st.write("## Model task:")
            st.markdown(
                "<h2 style='color: green; padding: 10px;'>"
                f"<strong>{model_task}</strong></h2>",
                unsafe_allow_html=True
            )
            # Make user select a model
            st.write("## Choose a model type")
            chosen_model = get_model(
                st.selectbox("Model type:", available_models)
            )

            # Make user select dataset split
            st.write("### Choose dataset split")
            split_ratio = st.slider(
                "Select train-test split (value is train):",
                min_value=0.05,
                max_value=0.95,
                value=0.8,
                step=0.05
            )

            # Make user select metrics to use
            st.write("### Select one or more metrics.")
            chosen_metrics = []
            selected_metrics = st.multiselect(
                "Select one or more metrics",
                available_metrics
            )
            for metric in selected_metrics:
                chosen_metrics.append(get_metric(metric))

            # Let user create Pipeline and create and then print it
            if st.button("Create Pipeline"):
                pipeline = Pipeline(
                    metrics=chosen_metrics,
                    dataset=retrieved_dataset,
                    model=chosen_model,
                    input_features=input_features,
                    target_feature=target_feature,
                    split=split_ratio
                )
                st.session_state.pipeline = pipeline
                st.session_state.pipeline_created = True
                st.success("Pipeline created successfully!")

            if st.session_state.pipeline_created:
                st.write(st.session_state.pipeline)

                if st.button("Evaluate model"):
                    results = st.session_state.pipeline.execute()
                    st.session_state.pipeline_executed = True
                    st.session_state.results = results
                    st.success("Pipeline executed succesfully")

        if st.session_state.pipeline_executed:
            st.write(st.session_state.results)


except NotFoundError:
    st.write("### No datasets found. Please upload a dataset to proceed.")
