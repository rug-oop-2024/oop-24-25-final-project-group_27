from autoop.core.ml.model import Model
import numpy as np
from typing import Optional
from sklearn.tree import DecisionTreeClassifier


class DTC(Model):
    """A Decision Tree Classifier Wrapper."""

    def __init__(
            self,
            parameters: Optional[dict] = None,
            **kwargs
    ) -> None:
        """Initialize Decision Tree Classifier Model."""
        if parameters is None:
            parameters = {}
        # Initialize our model as artifact and also parameters in Basemodel
        Model.__init__(
            self,
            name="DTC",
            type="classification",
            parameters=parameters,
            **kwargs
        )
        self.model = DecisionTreeClassifier(**self.parameters)

    def fit(self, observations: np.ndarray, ground_truth: np.ndarray) -> None:
        """Fit the data.

        Args:
            observations (np.ndarray): The observations
            ground_truth (np.ndarray): The ground truth
        """
        self.model.fit(observations, ground_truth)

    def predict(self, observations: np.ndarray) -> np.ndarray:
        """Predict the data.

        Args:
            observations (np.ndarray): The observations

        Returns:
            np.ndarray: Array of predictions
        """
        return self.model.predict(observations)
