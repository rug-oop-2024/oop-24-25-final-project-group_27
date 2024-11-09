
from pydantic import BaseModel, Field


class Feature(BaseModel):
    # attributes here
    name: str = Field(..., description="The name can be anything.")
    type: str = Field(
        None,
        description="Type must be 'numerical' or 'categorical'."
    )

    def __str__(self):
        return f"{self.name}"
