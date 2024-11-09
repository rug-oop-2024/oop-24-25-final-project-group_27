from autoop.core.ml.model import Model
import numpy as np
from sklearn.svm import SVC as SVCWrapper
from typing import Optional


class SVC(Model):
    """A SVC Wrapper."""
    def __init__(
            self,
            parameters: Optional[dict] = None,
            **kwargs
    ) -> None:
        """Initialize SVC Model."""
        if parameters is None:
            parameters = {}
        # Initialize our model as artifact and also parameters in Basemodel
        Model.__init__(
            self,
            name="SVC",
            type="classification",
            parameters=parameters,
            **kwargs
        )
        self.model = SVCWrapper(**self._parameters)

    def fit(self, observations: np.ndarray, ground_truth: np.ndarray) -> None:
        self.model.fit(observations, ground_truth)

    def predict(self, observations: np.ndarray) -> np.ndarray:
        return self.model.predict(observations)
