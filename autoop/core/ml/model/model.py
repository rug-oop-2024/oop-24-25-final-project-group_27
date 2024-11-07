
from abc import ABC, abstractmethod
from autoop.core.ml.artifact import Artifact
import numpy as np
from copy import deepcopy
from typing import Literal, Optional
from pydantic import BaseModel, Field

class Model(Artifact, BaseModel):
    """Abstract base class for models."""
    parameters: Optional[dict] = Field(default_factory=dict)
    model: Optional[object] = None

    def __init__(self, parameters: dict = None):
        super().__init__(parameters=parameters or {})

    @abstractmethod
    def fit(self, observations: np.ndarray, ground_truth: np.ndarray) -> None:
        """Return the fit data."""
        pass

    @abstractmethod
    def predict(self, observations: np.ndarray) -> np.ndarray:
        """Return the predicted data."""
        pass