"""This file contains the base class for Model."""
from abc import abstractmethod
from autoop.core.ml.artifact import Artifact
import numpy as np
from typing import Optional
from pydantic import BaseModel, Field
import pickle


class Model(Artifact, BaseModel):
    """Abstract base class for models."""

    parameters: Optional[dict] = Field(default_factory=dict)
    model: object = None

    def __init__(self, name: str, *args, **kwargs) -> None:
        """Initialize model with call to Basemodel and Artifact."""
        BaseModel.__init__(self, **kwargs)
        Artifact.__init__(
            self,
            name=name,
            asset_path=f"models/{name}.pkl",
            *args,
            **kwargs
        )

    @abstractmethod
    def fit(self, observations: np.ndarray, ground_truth: np.ndarray) -> None:
        """Return the fit data."""
        pass

    @abstractmethod
    def predict(self, observations: np.ndarray) -> np.ndarray:
        """Return the predicted data."""
        pass

    def read(self) -> 'Model':
        """Read a stored model."""
        model_bytes = super().read()
        return pickle.loads(model_bytes)

    def save(self) -> bytes:
        """Save model data."""
        model_bytes = pickle.dumps(self.model)
        # Store the serialized bytes in the artifact (save them)
        # The artifact data (model) is now stored as bytes
        return super().save(model_bytes)

    def to_artifact(self, name: str) -> Artifact:
        """Return model artifact."""
        return Artifact(
            type=self.type,
            name=name,
            asset_path=self.asset_path,
            data=self.save(),
            version=self.version,
            tags=self.tags,
            metadata=self.metadata
        )
