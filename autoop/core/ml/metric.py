from abc import ABC, abstractmethod
from typing import Any
import numpy as np
from sklearn.metrics import mean_squared_error


METRICS = [
    "mean_squared_error",
    "mean_absolute_error",
    "r_squared",
    "accuracy",
    "precision",
    "recall"
] # add the names (in strings) of the metrics you implement

def get_metric(name: str):
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
    """Base class for all metrics. """
    
    @abstractmethod
    def evaluate(self, ground_truth: np.ndarray, predictions: np.ndarray) -> float:
        pass

    # your code here
    # remember: metrics take ground truth and prediction as input and return a real number

    # wordt evaluate genoemd in pipeline.py dus aanpasssen en dan evaluate abstract en toepassen in concrete metrics

# add here concrete implementations of the Metric class
class MeanSquaredError(Metric):
    def evaluate(self, ground_truth: np.ndarray, predictions: np.ndarray) -> float:
        """"Evaluate using Mean Squared Error."""
        return np.sum((ground_truth - predictions) ** 2) / len(ground_truth)

class MeanAbsoluteError(Metric):
    def evaluate(self, ground_truth: np.ndarray, predictions: np.ndarray) -> float:
        """"Evaluate using Mean Absolute Error."""
        return np.mean(np.abs(ground_truth - predictions))

class RSquared(Metric):
    def evaluate(self, ground_truth: np.ndarray, predictions: np.ndarray) -> float:
        """Evaluate using R^2."""
        return 1 - np.sum((ground_truth - predictions) ** 2) / np.sum((ground_truth - np.mean(ground_truth)) ** 2)

class Accuracy(Metric):
    def evaluate(self, ground_truth: np.ndarray, predictions: np.ndarray) -> float:
        """Evaluate using Accuracy."""
        return np.sum(ground_truth == predictions) / len(ground_truth)

class Precision(Metric):
    def evaluate(self, ground_truth: np.ndarray, predictions: np.ndarray) -> float:
        """Evaluate using Precision metric."""
        tp = np.sum((ground_truth == 1) & (predictions == 1))
        fp = np.sum((ground_truth == 0) & (predictions == 1))
        return tp / (tp + fp) if (tp + fp) > 0 else 0

class Recall(Metric):
    def evaluate(self, ground_truth: np.ndarray, predictions: np.ndarray) -> float:
        """Evaluate using Recall metric."""
        tp = np.sum((ground_truth == 1) & (predictions == 1))
        fn = np.sum((ground_truth == 1) & (predictions == 0))
        return tp / (tp + fn) if (tp + fn) > 0 else 0