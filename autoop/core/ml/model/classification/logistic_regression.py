from autoop.core.ml.model import Model
import numpy as np
from sklearn.linear_model import (
    LogisticRegression as LogisticRegressionWrapper
)
from typing import Optional


class LogisticRegression(Model):
    """A Logistic Regression Wrapper."""
    def __init__(
            self,
            parameters: Optional[dict] = None,
            **kwargs
    ) -> None:
        """Initialize Logistic Regression Model"""
        if parameters is None:
            parameters = {}
        # Initialize our model as artifact and also parameters in Basemodel
        Model.__init__(
            self,
            name="LR",
            type="classification",
            parameters=parameters,
            **kwargs
        )
        self.model = LogisticRegressionWrapper(**self._parameters)

    def fit(self, observations: np.ndarray, ground_truth: np.ndarray) -> None:
        self.model.fit(observations, ground_truth)

    def predict(self, observations: np.ndarray) -> np.ndarray:
        return self.model.predict(observations)
