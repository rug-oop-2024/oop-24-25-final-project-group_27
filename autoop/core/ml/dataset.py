from autoop.core.ml.artifact import Artifact
from typing import Optional
import base64
import pandas as pd
import io

class Dataset(Artifact):
    def __init__(self, *args, **kwargs):
        super().__init__(type="dataset", *args, **kwargs)
        
    @staticmethod
    def from_dataframe(data: pd.DataFrame, name: str, asset_path: str, version: str = "1.0.0", tags: str, metadata: dict):
        return Dataset(
            name=name,
            asset_path=asset_path,
            data=data.to_csv(index=False).encode(),
            version=version,
            tags=tags,
            metadata=metadata
        )
        
    def read(self) -> pd.DataFrame:
        bytes = super().read()
        csv = bytes.decode()
        return pd.read_csv(io.StringIO(csv))
    
    def save(self, data: pd.DataFrame) -> bytes:
        bytes = data.to_csv(index=False).encode()
        return super().save(bytes)