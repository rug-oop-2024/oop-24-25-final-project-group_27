from pydantic import BaseModel, Field
import base64


class Artifact(BaseModel):
    # attributes to be implemented
    type: str = Field(None, description="The type of the artfiact.")
    name: str = Field(None, description="Name of the artifact.")
    asset_path: str = Field(None, description="Path of where the artifact is stored.")
    data: bytes = Field(None, description="Data that is given in bytes.")
    version: str = Field(None, description="Version of the artifact. Default is 1.0.0")

    # methods to be implemented

    def read(self) -> bytes:
        # return the data in bytes of this artifact
        return self.data

    def save(self, data: bytes) -> bytes:
        # save the data in bytes of this artifact and return the bytes of whole artifact.
        self.data = data
        return self.data
