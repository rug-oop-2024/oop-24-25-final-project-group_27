
from typing import List
from autoop.core.ml.dataset import Dataset
from autoop.core.ml.feature import Feature

def detect_feature_types(dataset: Dataset) -> List[Feature]:
    """Assumption: only categorical and numerical features and no NaN values.
    Args:
        dataset: Dataset
    Returns:
        List[Feature]: List of features with their types.
    """
    features = []
    # Input is a Dataset
    # Use read function to get pandas data frame
    pandas_frame = dataset.read()
    # Use dtypes function to get types of features
    for column in pandas_frame.columns:
        checked_feature = Feature(name=column)
        if pandas_frame[column].dtype in ['int64', 'float64']:
            # use setter of Feature class to set type to numerical
            checked_feature.type = "numerical"
        else:
            # use setter of Feature class to set type to categorical
            checked_feature.type = "categorical"
        features.append(checked_feature)
    # Return List with features
    return (features)

