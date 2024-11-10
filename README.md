# AutOOP your first AutoML library

🎉🥳 Congratulations on making it to this final project! We are excited to see what you can do.

## Introduction

The objective of this assignment is to create a Streamlit application that allows users to train models by uploading a CSV and choosing the target column. The assignment is designed to be completed within a month (`Deadline`, CHECK BRIGHTSPACE)
The intention is to simulate a real-world scenario where you are given a set of requirements and a codebase to start from. Furthermore, you will gain a better understanding of how ML applications are organised in industry which leverages standard OOP patters.

## Problem Space

The problem space is where you will be working. However, we have already implemented some of the features for you.
We highly encourage you to go beyond the requirements and implement additional features that you think would be useful for the user to showcase your skills. **The world is your oyster.**

### 📝 General principles

> "Simplicity is a great virtue but it requires hard work to achieve it and education to appreciate it. And to make matters worse: complexity sells better.”
― Edsger Wybe Dijkstra"

1. `Modifiability`: The code should be easy to modify and extend. You should be able to add new features without having to rewrite the entire codebase or heavy refactoring.
   *Important*: We prefer that you do not use libraries or frameworks for this reason. We want to see how you structure your code and how you solve problems. Furthermore, many of the tools available may not be customisable enough for our needs.
   Hence, if you want to include a library, please make sure to justify it.

2. `Testability`: The code should be easy to test. You should be able to write unit tests for the code.
3. `Readability`: The code should be easy to read. You should be able to understand what the code does without having to spend a lot of time on it.
4. `Performance`: The code should be fast. You should be able to run the code on a low-end machine without any problems.
5. `Intuitiveness`: The code should be easy to understand. You should be able to understand what the code does without having to spend a lot of time on it. But also the controls and interactions should be simple for the user.
6. `Security`: The code should be secure. Isolate your secrets and keys from the codebase. Do not commit your secrets and keys to the repository. Avoid XSS and CSRF attacks. Enforce the principle of least privilege. Validate user input, etc.

We encourage you to learn from the best practices and design patterns (e.g., https://refactoring.guru/design-patterns/python)

### 👨‍💻User stories
In an industry setting, you will be given user stories or requirements that need to be translated to functional requirements by you. Luckily, you will not have to do this but we left it for inspiraton.

1. OOP-001: As a datascientist, I want to be able to upload a CSV file so that I can begin my ML workflow.
2. OOP-002: As a datascientist, I want to be able to choose the target column so that I can achieve a certain task.
3. OOP-003: As a datascientist, I want to make slices on my dataset based on some criteria (e.g., age > 18, 80% split, etc.) so that I can train a model on a subset of the data.
4. OOP-004: As a datascientist, I want to be able to choose the type of model I want to train (e.g., classification, regression, etc.) so that I can achieve a certain task.
5. OOP-005: As a datascientist, I would like to start training and get results of different metrics.
6. OOP-006: As a datascientist, I would like to be able to download the model so that I can use it in production.
7. OOP-007: As a datascientist, I would like to create dataset artifacts from CSV files with respective names so that I can use it to train on them later.
8. OOP-008: As a datascientist, I would like to create predictions on a specific model to analyse the results.
9. OOP-009: As a datascientist, I would like to be able to download the predictions as a CSV file.
10. OOP-010: As a datascientist, I would like to view my predictions.
11. OOP-011: As a datascientist, I would like to create a model run where I can fine-tune an existing model on a new dataset.

More detailed instructions are provided in `INSTRUCTIONS.md` to guide you through these user stories.


#### 🥷 I-am-not-done-yet suggestions
You can try implementing the one of the following, we will give a max of 2 points based on the complexity of your addition.
* Generate experiment reports with graphs, metrics, and other relevant information.
* Create model runs that can be reproduced and compared against other ones with different strategies.
* Explain the model predictions.
* Implement SHAP, XEMP, or other algorithms for explainability.
* Sensitivity analysis.
* Topology planner for different ways to create a prediction pipeline (e.g., try different feature extractors on the same model).
* Show a graph of how the data flows through the pipeline.
* Support feature types of image, text, video, audio.
* Support target types of image, text, video, audio.
* Support time-series data (with the aforementioned column types) where a user can choose the time column.
* Support what-if analysis (e.g., user can change the input and see the output).
* Support metric optimization (e.g., select certain inputs to be adjusted to maximise the target column (e.g., maximise conversion).
* Create a prediction code generator for a specific model.
* Auto hyperparameter search/tuning.

### ⚒ Non-functional requirements

1. Create a streamlit app.
2. You **must not use automl libraries** (e.g., auto-sklearn, auto-keras, etc.). But you are allowed to use libraries for the ML models (e.g., sklearn, tensorflow, torch, keras, etc.).
3. Feature column types should be automatically inferred from the data.
4. Task type should be automatically inferred from the data.
5. Different models should be trained in parallel to evaluate the best model.
6. The code should infere wether a target column is valid for prediction given the capabilities of your algorithm.

### 📝 Documentation & Workflow
* The code should be documented. You should be able to understand what the code does without having to spend a lot of time on it.
* Significant design decisions should be documented as well. Each decision should be given an ID. Example:

```
# DSC-0001: Use TypeScript
# Date: 2021-09-01
# Decision: Use TypeScript for the project
# Status: Accepted
# Motivation: Lack of type safety in JavaScript
# Reason: TypeScript is a superset of JavaScript that adds type safety
# Limitations: TypeScript is not supported by all browsers
# Alternatives: propTypes
```
You can place your decisions in a docs folder in the root of the project.
E.g. docs/decisions/DSC-0001-use-typescript.md

### 📈 Testing
* Showcase the capability of your streamlit app with at least 3 different usecases on real datasets (from Kaggle). 
Some examples include housing prices, second-hand cars, etc.

### Checklist
- [ ] I have read the instructions carefully.
- [ ] I have filled my personal rubric.
- [ ] The code is refactored to style standards.
- [ ] I have passed my tests.
- [ ] I have documented my code and decisions.

# Grading & Submission (IMPORTANT)

We have experienced students who do not read the instructions and do not understand how they are graded. You can include `screenshots` in the repo. However, screenshots can be there as a back up incase something goes wrong while executing your code.

Grading will be based on the following criteria:

1. **Functionality**: Does the code work as expected? Does it meet the requirements?
2. **Code Quality**: Is the code clean and well-structured? Is it easy to read and understand? Are OOP principles followed?
3. **Documentation**: Is the code well-documented? Are design decisions explained?

Regarding the grading composition:

1. Implementing functionally correct code for Part I and Part II (compulsory requirements - see [Instructions](INSTRUCTIONS.md)) will give you 6 points.
2. The extra requirements of Part II will give extra 2 points.
3. Style (flake8, no code smells...) will give you 2 points.
4. HTML Documentation produced as explained in [Lecture 10](https://brightspace.rug.nl/content/enforced/356131-WBAI045-05.2024-2025.1/10%20-%20Libraries%20and%20Documentation.pdf) will give you extra 0.5 points. This bonus will be accessible only if the sum of the grade is >= 7.0.
   * You should use docstrings (in any format you want to) even if you don't intend on generating HTML documentation.

Concerning the criteria you should focus on, remember to keep in mind the usual concepts from the previous assignments, i.e., curate your style and docstrings, follow OOP principles, avoid code smells...
You can check for presence/absence of type hints and docstrings with `flake8` using the plugins `flake8-annotations` and `flake8-docstrings` (configure them to filter out the error messages you are not interested in).

## Workload

You are expected to carry out this assignment by **keeping the workload equal** between the two teammates.
You are also allowed to work collaboratively on some of all points.
In the final part of this markdown, you will see a table where you can keep track of who did what.
In case the workload will be imbalanced, **we reserve the option to deduct points** according to the disproportion in workload.
Notice that, in case two students claim to have worked together on the same point, we will assume that the workload has been split equally between the two on that specific requirement.

## How to get your submission accepted

1. **ALL** Tests must pass, we will not grade code bases the do not pass. Should you have any trouble, please contact our help desk in a timely manner. For helping with this point, we have set up two extra Q&A Labs during the exam week, check the schedule in brightspace.
2. Mark down in the following table which features that you have implemented. We will not check features that have not been marked as complete. So please fill your `Personal Rubric`. This way we do not miss any of your special additions.
3. If needed, include instructions if there are specific ways to run your code.

### Additional notes on submission acceptance

1. If your code does not run (because of bad imports, non-existing files, etc.), the project will **not** be graded further and a 1.0 will be given.
   * Thus, remember to push your .csv datasets.
2. Blatant disregard of OOP principles (e.g., using a largely imperative-style programming in the `autooop` library, consistently not using type hints...) will also result in the project being given a 1.0.

## Personal Rubric

These are from `INSTRUCTIONS.md`. Please read this carefully to ensure you can cover all the required requirements.

Also, mark down the person who implemented the feature. This information will be used for grading purposes.
If the feature has been implemented by both students, write `both`.

If you did not implement the feature

| Requirement                           | Type (FN/NF) | Implemented by | Implementation Completed | Comment |
|-------------------------------------- |--------------|--------|--------------------------|-------|         
| Up-to-date requirements.txt           | NF           |  both                |x         |
| `ML/detect-features`                  | FN           |  both                |x         |The detect_feature_types function assumes the dataset only contains categorical and numerical features, with no missing values. It uses pandas' dtypes to classify features as either numerical (int64, float64) or categorical, creating a Feature object for each and setting its type accordingly. This approach is efficient and leverages pandas' built-in functionality for type detection |
| `ML/artifact`                         | NF           |  both                |x         |The Artifact class uses pydantic for structured data validation, enforcing types and constraints on fields like type, name, and version. The generate_id method creates a unique ID by encoding asset_path in base64 and combining it with a sanitized version, ensuring consistency and compatibility across systems. The read and save methods manage data retrieval and updates in bytes, enhancing the class's functionality as a flexible container for artifact metadata and content. |
| `ML/feature`                          | NF           |  both                |x         |The Feature class uses Pydantic to ensure that fields like name and type are correctly typed and described. The type attribute is restricted to either numerical or categorical, keeping the classification consistent. The str method returns the feature’s name when printed, making it easier to read and identify each feature in outputs. ||
| `ML/metric`                           | NF           |  both                |x         |The Metric class defines a template for evaluation metrics, ensuring that each subclass implements the evaluate method to compute a score based on ground truth and predictions, and the string method to return the metric's name. This abstract base class structure enforces consistency across different metric implementations, supporting easy integration and reuse.|
| `ML/model`                            | NF           |  both                |x         |The ML/model has been implemented in t |
| `ML/model/extensions`                 | FN           |  both                |x         |The ml/models directory organizes machine learning models by task, with two folders for classification and regression. The classification folder includes models like Decision Tree Classifier, K Nearest Neighbors, and Random Forest Classifier. The regression folder contains models for Linear Regression, Random Forest Regressor, and Support Vector Regressor, supporting a variety of predictive modeling tasks. |
| `ML/pipeline/evaluation`              | FN           |  both                |x         |The evaluate function was already implemented with X and Y being test_X and test_Y. We have implemented a second method, train_evaluate for the x and y being for train_x and train_y. | 
| `ST/page/datasets`                    | NF           |  both                |x         |The datasets page allows the user to upload a CSV file, which is then processed and cleaned by dropping NaN values. The user can input a name and tags for the dataset, while unique experiment and run IDs are auto-generated as metadata. Upon clicking "Create Dataset", a new Dataset instance is created from the uploaded CSV and registered with the AutoML system. A success message is displayed, and the updated list of datasets is shown for confirmation. |
| `ST/datasets/management/create`       | FN           |  both                |x         |If the user clicks the "Create Dataset" button and provides a name, a new Dataset instance is created from the uploaded CSV. The dataset is initialized with the provided name, a file path where it will be stored, the tags entered by the user, and automatically generated metadata. This new dataset is then prepared for registration or further use. |
| `ST/datasets/management/save`         | FN           |  both                |x         |The CSV is saved with using the register method that is in the ArtifcatRegistry class which was given. |
| `ST/page/modelling`                   | NF           |  both                |x         |The Modelling page provides a user interface for designing and training machine learning models using datasets. It allows the user to select a dataset, choose input and target features, and determine whether the task is classification or regression based on the target feature type. Users can create machine learning pipelines, select metrics, and evaluate the model using various configurations. |
| `ST/modelling/datasets/list`          | FN           |  both                |x         |This section displays a list of available datasets from the AutoML registry. Users can select a dataset from the list, which will then be used for training. The dataset is loaded and previewed, showing the first few rows of data for the user's review. |
| `ST/modelling/datasets/features`      | FN           |  both                |x         |In this section, users can select input features and a target feature for the machine learning model. The target feature is selected from the available features, and it is automatically removed from the input features list to avoid duplication. The feature types are detected to help the system determine the task type (classification or regression). |
| `ST/modelling/models`                 | FN           |  both                |x         |This section allows users to choose a machine learning model based on the task type (classification or regression). After selecting a model, users can configure dataset splits and choose evaluation metrics. The user can then create a machine learning pipeline, which, once created, can be executed to train the model and evaluate its performance. The results are displayed upon execution. |
| `ST/modelling/pipeline/split`         | FN           |  both                |x         |This section allows users to select the split ratio for dividing the dataset into training and testing subsets. The split ratio is a float value between 0.05 and 0.95, where the value represents the proportion of data used for training (the remainder is used for testing). The selected ratio is passed to the pipeline, influencing how the data is partitioned for model training and evaluation. |
| `ST/modelling/pipeline/metrics`       | FN           |  both                |x         |Users can select one or more evaluation metrics that will be used to assess the performance of the selected model. These metrics are essential for understanding how well the model generalizes to unseen data and are passed to the pipeline for use during evaluation. The selected metrics will be applied to both the training and testing data to measure the model's accuracy. |
| `ST/modelling/pipeline/summary`       | FN           |  both                |x         |This section provides a summary of the pipeline configuration, including the selected model type, input features, target feature, metrics, and the dataset split ratio. |
| `ST/modelling/pipeline/train`         | FN           |  both                |x         |This section is responsible for training the model. After the dataset is split into training and testing sets and preprocessing is completed, the model is trained on the training data (input features and target).|
| `ST/modelling/pipeline/save`          | FN           |                      |          | |
| `ST/page/deployment`                  | FN           |                      |          | |
| `ST/deployment/load`                  | FN           |                      |          | |
| `ST/deployment/predict`               | FN           |                      |          | |

If you add extra features, please indicate them below:
| Requirement                           | Type (FN/NF) | Implemented by       | Implementation Completed (add X if done) | Comment |
|-------------------------------------- |--------------|----------------------|---------|-----|
|           |            |                      |         | |


Below, it can be seen that we have 3 different datasets working. The first one is the California Housing Dataset, the second one the Wine dataset and the third one the Gym Member Exercise dataset. 

