"""Implementation of KNN model."""
from autoop.core.ml.model import Model
import numpy as np
from typing import Optional
from sklearn.neighbors import KNeighborsClassifier


class KNN(Model):
    """A KNN Wrapper."""

    def __init__(
            self,
            parameters: Optional[dict] = None,
            **kwargs
    ) -> None:
        """Initialize KNN Model."""
        if parameters is None:
            parameters = {}
        # Initialize our model as artifact and also parameters in Basemodel
        Model.__init__(
            self,
            name="KNN",
            type="classification",
            parameters=parameters,
            **kwargs
        )
        self.model = KNeighborsClassifier(**self.parameters)

    def fit(self, observations: np.ndarray, ground_truth: np.ndarray) -> None:
        """Fit the data."""
        self.model.fit(observations, ground_truth)

    def predict(self, observations: np.ndarray) -> np.ndarray:
        """Predict the data."""
        return self.model.predict(observations)
