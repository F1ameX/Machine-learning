# Binary Prediction of Poisonous Mushrooms Kaggle Competition

This repository contains a project aimed at classifying mushrooms as edible or poisonous based on various features. The project utilizes the Mushroom Classification dataset and applies a LightGBM model for prediction.

## Project Structure

- `Mushroom-Classification/`
    - `data/`: Contains the training, testing datasets, and sample submission file.
    - `notebooks/`: Jupyter notebooks used for data analysis and model training.
    - `README.md`: Project documentation.

## Project Workflow

1. **Environment Setup**
   - Install the required libraries: NumPy, pandas, seaborn, matplotlib, and LightGBM.

2. **Data Loading**
   - Load the training and testing datasets from the `data/` folder using pandas.

3. **Data Exploration**
   - Display the first few rows and basic information about the dataset to understand its structure.
   - Check the columns to identify categorical and numerical features.

4. **Data Preprocessing**
   - **Handling Missing Values**: 
     - Fill missing values in categorical features with 'missing'.
     - Fill missing values in the 'cap-diameter' feature with the mean value of the column.
   - **Data Type Conversion**:
     - Convert categorical features to the 'category' datatype for efficient memory usage and better model performance.

5. **Feature Engineering**
   - Separate the features (`x`) and target variable (`y`) from the training data.
   - Split the data into training and validation sets using an 80-20 split to evaluate model performance.

6. **Model Training**
   - Train a LightGBM classifier with specific hyperparameters optimized for the dataset.
   - Fit the model using the training data (`x_train`, `y_train`).

7. **Model Evaluation**
   - Predict the target variable for the validation set.
   - Evaluate the model using the Matthews Correlation Coefficient (MCC) metric to assess the performance.

8. **Prediction and Submission**
   - Use the trained model to predict the target variable for the test dataset.
   - Create a submission file by replacing the 'class' column in the sample submission with the predicted values.
   - Save the submission file as `sample_submission.csv` in the `data/` folder.

## Results
- **Validation MCC**: The model's performance on the validation set is evaluated using the Matthews Correlation Coefficient.
- **Competition Result**: Achieved a ranking of 558/2424 in the Kaggle competition with a score of 0.98481.

## Acknowledgments
- **Open-Source Libraries**: Thanks to the open-source community for the valuable libraries such as LightGBM, pandas, and scikit-learn.
- **Dataset Providers**: Special thanks to the data providers for making the Mushroom Classification dataset available.

This project serves as a practical example of applying machine learning techniques to solve classification problems using real-world datasets. Future improvements could include exploring additional feature engineering methods, hyperparameter tuning, and experimenting with different machine learning models to enhance performance.
