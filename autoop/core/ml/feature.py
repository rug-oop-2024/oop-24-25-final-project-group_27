
from pydantic import BaseModel, Field


class Feature(BaseModel):
    """Feature class."""

    # attributes here
    name: str = Field(..., description="The name can be anything.")
    type: str = Field(
        None,
        description="Type must be 'numerical' or 'categorical'."
    )

    def __str__(self) -> str:
        """text when printed.

        Returns:
            str: Name of feature.
        """
        return f"{self.name}"
