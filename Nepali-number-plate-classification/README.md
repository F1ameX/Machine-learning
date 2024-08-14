# Nepali number plate classification
This repository contains a simple classification model project aimed to classify the letters on Nepali number plates. The project uses the eponymous dataset consists different Nepali number plates.

## Project structure
- `Nepali-number-plate-classification/`
    - `sample.ipynb/`: Saved final classification model

## Project Workflow

The following outlines the workflow and key steps within the provided Jupyter notebook:

1. **Import Libraries**
   Import necessary libraries for data handling, image processing, and model training.
2. **Set Up Data Directory and Categories**
   Define the path to the data directory and list of categories for classification.

3. **Load and Preprocess Data**
    - Load images from the directory.
    - Preprocess images: convert to grayscale, resize to standard size, and prepare labels.

4. **Prepare Data for Model**
    - Convert the image data and labels to numpy arrays.
    - Reshape image data for model compatibility.
    - Split the data into training and testing sets.

5. **Define Model and Hyperparameters**
    - Define the Support Vector Classifier (SVC) model.
    - Set up hyperparameters for grid search.

6. **Train the Model**
    - Perform grid search with cross-validation to find the best model parameters.
    - Fit the model to the training data.
    - 
7. **Evaluate the Model**
    - Predict on the test set using the best model.
    - Calculate and print the accuracy of the model.

## Results
The model has shown accuracy about average 96% 

## Acknowledgments

- Kaggle providing dataset
- The open-source community for their valuable libraries and tools.
