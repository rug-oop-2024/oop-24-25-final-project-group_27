"""File for easy imports."""
from autoop.core.ml.model.classification.decision_tree_classifier import DTC
from autoop.core.ml.model.classification.random_forest_classifier import (
    RandomForestClassifier
)
from autoop.core.ml.model.classification.knn import KNN

CLASSIFICATION_MODELS_DICT = {
    "DTC": DTC,
    "RFC": RandomForestClassifier,
    "KNN": KNN
}
