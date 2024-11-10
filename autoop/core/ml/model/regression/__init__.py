"""File for easy imports."""
from autoop.core.ml.model.regression.linear_regression import (
    MultipleLinearRegression
)
from autoop.core.ml.model.regression.svr import SVR
from autoop.core.ml.model.regression.random_forest_regressor import (
    RandomForestRegressor
)

REGRESSION_MODELS_DICT = {
    "SVR": SVR,
    "MLR": MultipleLinearRegression,
    "RFR": RandomForestRegressor
}
