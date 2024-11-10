from abc import ABC, abstractmethod

import numpy as np


METRICS = [
    "mean_squared_error",
    "mean_absolute_error",
    "r_squared",
    "accuracy",
    "precision",
    "recall"
]
# add the names (in strings) of the metrics you implement

REGR_METRICS = [
    "mean_squared_error",
    "mean_absolute_error",
    "r_squared",
]

CLAS_METRICS = [
    "accuracy",
    "precision",
    "recall"
]


def get_metric(name: str) -> 'Metric':
    """Factory method.

    Args:
        name (str): Metric name to get.

    Returns:
        Metric: Metric instance.
    """
    # Factory function to get a metric by name.
    # Return a metric instance given its str name.
    if name == "mean_squared_error":
        return MeanSquaredError()
    elif name == "mean_absolute_error":
        return MeanAbsoluteError()
    elif name == "r_squared":
        return RSquared()
    elif name == "accuracy":
        return Accuracy()
    elif name == "precision":
        return Precision()
    elif name == "recall":
        return Recall()


class Metric(ABC):
    """Base class for all metrics."""

    @abstractmethod
    def evaluate(
        self,
        ground_truth: np.ndarray,
        predictions: np.ndarray
    ) -> float:
        """Abstract method to be implemented.

        Args:
            ground_truth (np.ndarray): Ground truths
            predictions (np.ndarray): Predictions

        Returns:
            float: Evaluation score
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """String method.

        Returns:
            str: Text to print.
        """
        pass


# add here concrete implementations of the Metric class
class MeanSquaredError(Metric):
    """Mean Squared Error class."""

    def evaluate(
            self,
            ground_truth: np.ndarray,
            predictions: np.ndarray
    ) -> float:
        """Evaluate using Mean Squared Error."""
        return np.sum((ground_truth - predictions) ** 2) / len(ground_truth)

    def __str__(self) -> str:
        """Return the name of metric"""
        return "MeanSquaredError"


class MeanAbsoluteError(Metric):
    """Mean Absolute Error."""

    def evaluate(
            self,
            ground_truth: np.ndarray,
            predictions: np.ndarray
    ) -> float:
        """Evaluate using Mean Absolute Error."""
        return np.mean(np.abs(ground_truth - predictions))

    def __str__(self) -> str:
        """Return the name of metric"""
        return "MeanAbsoluteError"


class RSquared(Metric):
    """RSquared."""

    def evaluate(
            self,
            ground_truth: np.ndarray,
            predictions: np.ndarray
    ) -> float:
        """Evaluate using R^2."""
        sum_sq_res = np.sum((ground_truth - predictions) ** 2)
        sum_sq_tot = np.sum((ground_truth - np.mean(ground_truth)) ** 2)
        return 1 - (sum_sq_res / sum_sq_tot)

    def __str__(self) -> str:
        """Return the name of metric"""
        return "RSquared"


class Accuracy(Metric):
    """Accuracy."""

    def evaluate(
            self,
            ground_truth: np.ndarray,
            predictions: np.ndarray
    ) -> float:
        """Evaluate using Accuracy."""
        return np.sum(ground_truth == predictions) / len(ground_truth)

    def __str__(self) -> str:
        """Return the name of metric"""
        return "Accuracy"


class Precision(Metric):
    """Precision."""

    def evaluate(
            self,
            ground_truth: np.ndarray,
            predictions: np.ndarray
    ) -> float:
        """Evaluate using Precision for multiclass classification."""
        # Look how much classes we have
        classes = np.unique(ground_truth)
        precision_scores = []

        # Go over classes and find precision score per class
        for cls in classes:
            tp = np.sum((ground_truth == cls) & (predictions == cls))
            fp = np.sum((ground_truth != cls) & (predictions == cls))
            precision = tp / (tp + fp) if (tp + fp) > 0 else 0
            precision_scores.append(precision)

        # We perform macro-averaging
        return np.mean(precision_scores)

    def __str__(self) -> str:
        """Return the name of metric"""
        return "Precision"


class Recall(Metric):
    """Recall."""

    def evaluate(
            self,
            ground_truth: np.ndarray,
            predictions: np.ndarray
    ) -> float:
        """Evaluate using Recall for multiclass classification."""
        # Look how much classes we have
        classes = np.unique(ground_truth)
        recall_scores = []

        # Go over classes and find precision score per class
        for cls in classes:
            tp = np.sum((ground_truth == cls) & (predictions == cls))
            fn = np.sum((ground_truth == cls) & (predictions != cls))
            recall = tp / (tp + fn) if (tp + fn) > 0 else 0
            recall_scores.append(recall)

        # We return the macro-averaging
        return np.mean(recall_scores)

    def __str__(self) -> str:
        """Return the name of metric"""
        return "Recall"
