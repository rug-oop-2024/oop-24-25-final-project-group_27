from autoop.core.ml.model import Model
import numpy as np
from sklearn.svm import SVR as SVRWrapper
from typing import Optional


class SVR(Model):
    """A SVR Wrapper."""

    def __init__(
            self,
            parameters: Optional[dict] = None,
            **kwargs
    ) -> None:
        """Initialize SVR Model."""
        if parameters is None:
            parameters = {}
        # Initialize our model as artifact and also parameters in Basemodel
        Model.__init__(
            self,
            name="SVR",
            type="regression",
            parameters=parameters,
            **kwargs
        )
        self.model = SVRWrapper(**self.parameters)

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
