
from abc import ABC, abstractmethod
from autoop.core.ml.artifact import Artifact
import numpy as np
from copy import deepcopy
from typing import Literal
from pydantic import PrivateAttr

class Model(ABC, Artifact):
    """Abstract base class for models."""

    _parameters: dict = PrivateAttr(default=dict)

    def __init__(self, parameters: dict) -> None:
        """Initialize parameters."""
        self.parameters = parameters

    @property
    def parameters(self) -> dict:
        """Return deepcopy of parameters to prevent leakage."""
        return deepcopy(self._parameters)

    @parameters.setter
    def parameters(self, value: dict) -> None:
        if self._validate_parameters(value):
            self._parameters = value
        else:
            raise ValueError("Invalid parameters, should be a Dict.")

    def _validate_parameters(self, parameters: dict) -> bool:
        """Validate parameter type."""
        return isinstance(parameters, dict)

    @abstractmethod
    def fit(self, observations: np.ndarray, ground_truth: np.ndarray) -> None:
        """Return the fit data."""
        pass

    @abstractmethod
    def predict(self, observations: np.ndarray) -> np.ndarray:
        """Return the predicted data."""
        pass