from abc import ABC, abstractmethod
from typing import Any
import numpy as np

METRICS = [
    "mean_squared_error",
    "mean_absolute_error",
    "r_squared",
    "accuracy",
    "precision",
    "f1_score"
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
    elif name == "f1_score":
        return F1Score()

class Metric(ABC):
    """Base class for all metrics.
    """
    # your code here
    # remember: metrics take ground truth and prediction as input and return a real number
    def __call__(self):
        pass

    # wordt evaluate genoemd in pipeline.py dus aanpasssen en dan evaluate abstract en toepassen in concrete metrics

# add here concrete implementations of the Metric class
class MeanSquaredError(Metric):


class MeanAbsoluteError(Metric):


class RSquared(Metric):


class Accuracy(Metric):


class Precision(Metric):

class F1Score(Metric):

    