# Box Office Prediction Project
This repository contains a prediction machine learning project aime at predicting the revenue of movies. The project uses the TMDB dataset provided by the Kaggle eponymous competition.

## Project Structure
- ``Box-office-prediction_Kaggle/``
  - ``data/``: Contains TMDB dataset
  - ``sample.ipynb``: Saved EDA and ML project
  - ``README.md``: Current project documentation

## Project Workflow

1. **Data Exploration**
    - Load the TMDB dataset.
    - Analyze the dataset to understand the structure and relationships.
    - Visualize key features and their distributions.

2. **Data Preprocessing**
    - Handle missing values in the dataset.
    - Engineer new features to improve model performance.

3. **Model Training**
    - Split the data into training and testing sets.
    - Train Catboost Regressor machine learning model.

4. **Model Evaluation**
    - Evaluate models using RMSE and RMSLE.

5. **Prediction**
    - Use the selected model to make predictions on the test dataset.
    - Prepare the submission file for the Kaggle competition.

## Results
The final model achieved and RMSLE(Root-Mean-Squared-Logarithmic-Error) of 3.92. The perfomance can be further improved by experimenting with different feature engineering techniques. Actually, there are good EDA and not enough feature engineering. Project not for beginners, but I tried :)

## Acknowledgements
- Kaggle for providing TMDB (The Movie DataBase) dataset
- The open-source community for their valuable libraries and tools