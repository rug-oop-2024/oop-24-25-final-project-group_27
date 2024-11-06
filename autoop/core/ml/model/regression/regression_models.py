from autoop.core.ml.model import Model
import numpy as np
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

class SVRWrap(Model):

    def __init__(self, parameters: dict) -> None:
        """"Initialize SVR Wrapper Model"""

        super().__init__(parameters)
        self.model = SVR(**self._parameters)
        
    def fit(self, observations: np.ndarray, ground_truth: np.ndarray) -> None:
        self.model.fit(observations, ground_truth)

    def predict(self, observations: np.ndarray) -> np.ndarray:
        return self.model.predict(observations)

class Linear_Regression(Model):
        """Initialize Linear Regression Model"""

    def __init__(self, parameters: dict) -> None:
        super().__init__(parameters)
        self.model = LinearRegression(**self._parameters)

    def fit(self, observations: np.ndarray, ground_truth: np.ndarray) -> None:
        self.model.fit(observations, ground_truth)

    def predict(self, observations: np.ndarray) -> np.ndarray:
        return self.model.predict(observations)

        