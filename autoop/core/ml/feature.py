
from pydantic import BaseModel, Field
from typing import Literal
import numpy as np

from autoop.core.ml.dataset import Dataset

class Feature(BaseModel):
    # attributes here
    name: str = Field(..., description="The name can be anything.")
    type: str = Field(None, description="Type must be 'numerical' or 'categorical'.")

    def __str__(self):
        raise NotImplementedError("To be implemented.")