from autoop.core.ml.model import Model
import numpy as np
from sklearn.linear_model import LinearRegression
from typing import Optional


class MultipleLinearRegression(Model):
    """A Linear Regression Wrapper."""

    def __init__(
            self,
            parameters: Optional[dict] = None,
            **kwargs
    ) -> None:
        """Initialize Linear Regression Model."""
        if parameters is None:
            parameters = {}
        # Initialize our model as artifact and also parameters in Basemodel
        Model.__init__(
            self,
            name="MLR",
            type="regression",
            parameters=parameters,
            **kwargs
        )
        self.model = LinearRegression(**self.parameters)

    def fit(self, observations: np.ndarray, ground_truth: np.ndarray) -> None:
        """Fit the Data.

        Args:
            observations (np.ndarray): The observations
            ground_truth (np.ndarray): The ground truth
        """
        self.model.fit(observations, ground_truth)

    def predict(self, observations: np.ndarray) -> np.ndarray:
        """Predict the Data.

        Args:
            observations (np.ndarray): The observations

        Returns:
            np.ndarray: The predictions
        """
        return self.model.predict(observations)
