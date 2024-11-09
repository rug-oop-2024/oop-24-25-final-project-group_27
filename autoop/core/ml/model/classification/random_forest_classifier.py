from autoop.core.ml.model import Model
import numpy as np
from sklearn.ensemble import RandomForestClassifier as RFC
from typing import Optional


class RandomForestClassifier(Model):
    """A Random Forest Classifier Wrapper."""
    def __init__(
            self,
            parameters: Optional[dict] = None,
            **kwargs
    ) -> None:
        """Initialize Random Forest Classifier Model."""
        if parameters is None:
            parameters = {}
        # Initialize our model as artifact and also parameters in Basemodel
        Model.__init__(
            self,
            name="RFC",
            type="classification",
            parameters=parameters,
            **kwargs
        )
        self.model = RFC(**self._parameters)

    def fit(self, observations: np.ndarray, ground_truth: np.ndarray) -> None:
        self.model.fit(observations, ground_truth)

    def predict(self, observations: np.ndarray) -> np.ndarray:
        return self.model.predict(observations)
