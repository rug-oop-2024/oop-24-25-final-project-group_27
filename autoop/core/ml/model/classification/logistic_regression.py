from autoop.core.ml.model import Model
import numpy as np
from sklearn.linear_model import LogisticRegression as LogisticRegressionWrapper

class LogisticRegression(Model):
    def __init__(self, parameters: dict) -> None:
        super().__init__(parameters)
        self.model = LogisticRegressionWrapper(**self._parameters)

    def fit(self, observations: np.ndarray, ground_truth: np.ndarray) -> None:
        self.model.fit(observations, ground_truth)

    def predict(self, observations: np.ndarray) -> np.ndarray:
        return self.model.predict(observations)

