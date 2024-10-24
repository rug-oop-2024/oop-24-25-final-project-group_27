from autoop.core.ml.model import Model
import numpy as np
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

class SVR(Model):
    def fit(self, observations: np.ndarray, ground_truth: np.ndarray) -> None:
        return super().fit(observations, ground_truth)

    def predict(self, observations: np.ndarray) -> np.ndarray:
        return super().predict(observations)

