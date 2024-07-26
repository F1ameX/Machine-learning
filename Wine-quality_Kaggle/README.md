# Red Wine Quality Analysis Project

This repository contains a data analysis project aimed at found the best model finding quality of red wine based on various chemical properties. The project uses the Wine Quality dataset from the UCI Machine Learning Repository.

## Project Structure

- `Wine-quality_Kaggle/`
    - `data/`: Contains the wine features dataset.
    - `sample.ipynb/`: Saved data analysis project.
    - `README.md`: Project documentation.

## Project Workflow

1. **Data Exploration**
   - Load the Wine Quality dataset.
   - Analyze the dataset to understand the structure and relationships.
   - Visualize key features and their distributions.
   
2. **Data Preprocessing**
   - Standardize the features to improve model performance.
   
3. **Models Training**
   - Split the data into training and testing sets.
   - Train several machine learning models:
      - Logistic Regression
      - Decision Tree Classifier
      - Random Forest Classifier
      - CatBoost Regressor
     
4. **Models Evaluation And Compare**
   - Evaluate models using accuracy.
   - Compare the performance of different models.

## Results
**The performance of the models is compared using accuracy scores:**
- Logistic Regression: 56%
- Decision Tree Classifier: 57%
- Random Forest Classifier: 65%
- Catboost Regressor: 47%

The Random Forest Classifier achieved the highest accuracy of 65%. The performance can be further improved by experimenting with different feature engineering techniques and advanced machine learning models.

## Acknowledgments

- **UCI Machine Learning Repository for providing the Wine Quality dataset.**

- **The open-source community for their valuable libraries and tools.**