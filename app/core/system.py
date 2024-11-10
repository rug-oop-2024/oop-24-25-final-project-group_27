from autoop.core.storage import LocalStorage
from autoop.core.database import Database
from autoop.core.ml.dataset import Dataset
from autoop.core.ml.artifact import Artifact
from autoop.core.storage import Storage
from typing import List


class ArtifactRegistry():
    """Arifact Registry class."""

    def __init__(self,
                 database: Database,
                 storage: Storage) -> None:
        """Initialize Registry.

        Args:
            database (Database): the database
            storage (Storage): the storage
        """
        self._database = database
        self._storage = storage

    def register(self, artifact: Artifact) -> None:
        """Register an Artifact.

        Args:
            artifact (Artifact): Artifact to be stored.
        """
        # save the artifact in the storage
        self._storage.save(artifact.data, artifact.asset_path)
        # save the metadata in the database
        entry = {
            "name": artifact.name,
            "version": artifact.version,
            "asset_path": artifact.asset_path,
            "tags": artifact.tags,
            "metadata": artifact.metadata,
            "type": artifact.type,
        }
        self._database.set("artifacts", artifact.id, entry)

    def list(self, type: str = None) -> List[Artifact]:
        """List al artifacts with type.

        Args:
            type (str, optional): type of artifact. Defaults to None.

        Returns:
            List[Artifact]: List of that type artifact.
        """
        entries = self._database.list("artifacts")
        artifacts = []
        for id, data in entries:
            if type is not None and data["type"] != type:
                continue
            artifact = Artifact(
                name=data["name"],
                version=data["version"],
                asset_path=data["asset_path"],
                tags=data["tags"],
                metadata=data["metadata"],
                data=self._storage.load(data["asset_path"]),
                type=data["type"],
            )
            artifacts.append(artifact)
        return artifacts

    def get(self, artifact_id: str) -> Artifact:
        """Get artifact from database.

        Args:
            artifact_id (str): Artifact id

        Returns:
            Artifact: The artifact.
        """
        data = self._database.get("artifacts", artifact_id)
        return Artifact(
            name=data["name"],
            version=data["version"],
            asset_path=data["asset_path"],
            tags=data["tags"],
            metadata=data["metadata"],
            data=self._storage.load(data["asset_path"]),
            type=data["type"],
        )

    def get_dataset(self, artifact_id: str) -> Dataset:
        """Get dataset with id.

        Args:
            artifact_id (str): Artifact ID.

        Returns:
            Dataset: Returns the dataset.
        """
        data = self._database.get("artifacts", artifact_id)
        return Dataset(
            name=data["name"],
            version=data["version"],
            asset_path=data["asset_path"],
            tags=data["tags"],
            metadata=data["metadata"],
            data=self._storage.load(data["asset_path"]),
        )

    def delete(self, artifact_id: str) -> None:
        """Delete Artifact from Storage and Database.

        Args:
            artifact_id (str): ID of Artifact.
        """
        data = self._database.get("artifacts", artifact_id)
        self._storage.delete(data["asset_path"])
        self._database.delete("artifacts", artifact_id)


class AutoMLSystem:
    """AutoMLSystem instance."""

    _instance = None

    def __init__(self, storage: LocalStorage, database: Database) -> None:
        """Initialize AutoMLSystem.

        Args:
            storage (LocalStorage): The local storage.
            database (Database): The database.
        """
        self._storage = storage
        self._database = database
        self._registry = ArtifactRegistry(database, storage)

    @staticmethod
    def get_instance() -> None:
        """Get instance.

        Returns:
            AutoMLSystem: return an instance.
        """
        if AutoMLSystem._instance is None:
            AutoMLSystem._instance = AutoMLSystem(
                LocalStorage("./assets/objects"),
                Database(
                    LocalStorage("./assets/dbo")
                )
            )
        AutoMLSystem._instance._database.refresh()
        return AutoMLSystem._instance

    @property
    def registry(self) -> ArtifactRegistry:
        """Getter function for registry."""
        return self._registry
