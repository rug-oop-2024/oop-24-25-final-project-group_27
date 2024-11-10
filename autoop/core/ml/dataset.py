from autoop.core.ml.artifact import Artifact
import pandas as pd
import io


class Dataset(Artifact):
    """Dataset class.

    Args:
        Artifact (_type_): _description_
    """

    def __init__(self, *args, **kwargs) -> None:
        """Initialize Dataset."""
        super().__init__(type="dataset", *args, **kwargs)

    @staticmethod
    def from_dataframe(
        data: pd.DataFrame,
        name: str,
        asset_path: str,
        tags: str = "",
        metadata: dict = {},
        version: str = "1.0.0"
    ) -> "Dataset":
        """Get a Dataset from pandas dataframe.

        Args:
            data (pd.DataFrame): The dataframe
            name (str): Name of dataset
            asset_path (str): Path where file is stored.
            tags (str, optional): tags about Dataset. Defaults to "".
            metadata (dict, optional): Metadata about Dataset. Defaults to {}.
            version (str, optional): Version of artifact. Defaults to "1.0.0".

        Returns:
            Dataset: A Dataset object.
        """
        return Dataset(
            name=name,
            asset_path=asset_path,
            data=data.to_csv(index=False).encode(),
            version=version,
            tags=tags,
            metadata=metadata
        )

    def read(self) -> pd.DataFrame:
        """Read data.

        Returns:
            pd.DataFrame: Dataframe
        """
        bytes = super().read()
        csv = bytes.decode()
        return pd.read_csv(io.StringIO(csv))

    def save(self, data: pd.DataFrame) -> bytes:
        """Save data.

        Args:
            data (pd.DataFrame): data to save.

        Returns:
            bytes: Bytes of data.
        """
        bytes = data.to_csv(index=False).encode()
        return super().save(bytes)
