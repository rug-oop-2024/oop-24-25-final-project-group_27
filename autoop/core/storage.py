from abc import ABC, abstractmethod
import os
from typing import List
from glob import glob


class NotFoundError(Exception):
    """Error class."""

    def __init__(self, path: str) -> None:
        """Init method.

        Args:
            path (str): path that was not found.
        """
        super().__init__(f"Path not found: {path}")


class Storage(ABC):
    """Storage abstract base class."""

    @abstractmethod
    def save(self, data: bytes, path: str) -> None:
        """
        Save data to a given path

        Args:
            data (bytes): Data to save
            path (str): Path to save data
        """
        pass

    @abstractmethod
    def load(self, path: str) -> bytes:
        """
        Load data from a given path

        Args:
            path (str): Path to load data
        Returns:
            bytes: Loaded data
        """
        pass

    @abstractmethod
    def delete(self, path: str) -> None:
        """
        Delete data at a given path

        Args:
            path (str): Path to delete data
        """
        pass

    @abstractmethod
    def list(self, path: str) -> list:
        """
        List all paths under a given path

        Args:
            path (str): Path to list
        Returns:
            list: List of paths
        """
        pass


class LocalStorage(Storage):
    """Local storage that inherits from Storage."""

    def __init__(self, base_path: str = "./assets") -> None:
        """Init method.

        Args:
            base_path (str, optional): Path where storage is.
                                       Defaults to "./assets".
        """
        self._base_path = base_path
        if not os.path.exists(self._base_path):
            os.makedirs(self._base_path)

    def save(self, data: bytes, key: str) -> None:
        """Save method.

        Args:
            data (bytes): data to be saved.
            key (str): key of data.
        """
        path = self._join_path(key)
        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'wb') as f:
            f.write(data)

    def load(self, key: str) -> bytes:
        """Load method.

        Args:
            key (str): path of data

        Returns:
            bytes: data in bytes.
        """
        path = self._join_path(key)
        self._assert_path_exists(path)
        with open(path, 'rb') as f:
            return f.read()

    def delete(self, key: str = "/") -> None:
        """Delete method.

        Args:
            key (str, optional): path. Defaults to "/".
        """
        self._assert_path_exists(self._join_path(key))
        path = self._join_path(key)
        os.remove(path)

    def list(self, prefix: str) -> List[str]:
        """List keys

        Args:
            prefix (str): path where we want to list all.

        Returns:
            List[str]: List of existing paths
        """
        path = self._join_path(prefix)
        self._assert_path_exists(path)
        keys = glob(path + "/**/*", recursive=True)
        return list(filter(os.path.isfile, keys))

    def _assert_path_exists(self, path: str) -> None:
        if not os.path.exists(path):
            raise NotFoundError(path)

    def _join_path(self, path: str) -> str:
        return os.path.join(self._base_path, path)
