from pydantic import BaseModel, Field
import base64


class Artifact(BaseModel):
    """Artifact class."""

    # attributes to be implemented
    type: str = Field(None, description="The type of the artifact.")
    name: str = Field(None, description="Name of the artifact.")
    asset_path: str = Field(
        None, description="Path of where the artifact is stored."
    )
    data: bytes = Field(None, description="Data that is given in bytes.")
    version: str = Field(
        "1.0.0", description="Version of the artifact. Default is 1.0.0"
    )
    tags: str = Field(
        None, description="Labels or keywords used to categorize or identify"
                          " artifacts based on certain attributes"
    )
    metadata: dict[str, str] = Field(
        None, description="A dictionary containing metadata for the artifact,"
                          "such as experiment ID and run ID."
    )

    # Unique ID generated based on asset_path and version
    id: str = None

    def __init__(self, **data) -> None:
        """Initialize Artifact."""
        super().__init__(**data)
        self.id = self.generate_id()

    def generate_id(self) -> str:
        """Gemerate ID

        Returns:
            str: ID
        """
        # Encode asset_path in base64 and strip the padding (equal signs)
        encoded_path = base64.b64encode(
            self.asset_path.encode()
        ).decode().rstrip('=')

        # Replace any non-underscore-friendly characters in version
        sanitized_version = self.version.replace(
            '.', '_'
        ).replace(
            ';', '_'
        ).replace(
            ',', '_'
        ).replace(
            '=', '_'
        )

        # Construct the ID by combining the encoded path and sanitized version
        return f"{encoded_path}_{sanitized_version}"

    def read(self) -> bytes:
        """Read data.

        Returns:
            bytes: The data in bytes.
        """
        # Return the data in bytes of this artifact
        return self.data

    def save(self, data: bytes) -> bytes:
        """Save artifact data.

        Args:
            data (bytes): Data to be stored

        Returns:
            bytes: The saved Data
        """
        # Save the data in bytes of this artifact and return the bytes the
        # artifact.
        self.data = data
        return self.data
