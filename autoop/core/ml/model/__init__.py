
from autoop.core.ml.model.model import Model
from autoop.core.ml.model.regression import SVR, MultipleLinearRegression, RandomForestRegressor
from autoop.core.ml.model.classification import LogisticRegression, RandomForestClassifier, SVC


REGRESSION_MODELS = [
    "SVR",
    "MultipleLinearRegression",
    "RandomForestRegressor"
] # add your models as str here

CLASSIFICATION_MODELS = [
    "LogisticRegression",
    "RandomForestClassifier",
    "SVC"
] # add your models as str here

def get_model(model_name: str) -> Model:
    """Factory function to get a model by name."""
    # Check in regression models
    if model_name in REGRESSION_MODELS:
        if model_name == "SVR":
            return SVR()
        elif model_name == "MultipleLinearRegression":
            return MultipleLinearRegression()
        elif model_name == "RandomForestRegressor":
            return RandomForestRegressor()

    # Check in classification models
    elif model_name in CLASSIFICATION_MODELS:
        if model_name == "LogisticRegression":
            return LogisticRegression()
        elif model_name == "RandomForestClassifier":
            return RandomForestClassifier()
        elif model_name == "SVC":
            return SVC()
    raise NotImplementedError("To be implemented.")

    