# Cat and Dog Classification using YOLO

This repository contains a project aimed at classifying images of cats and dogs using the YOLO (You Only Look Once) model. The project involves data preparation, model training, and evaluation.

## Project Structure
- `Dog-cat-Classification/`
    - `sample.ipynb`: Jupyter notebook containing the entire workflow of data preparation, model training, and evaluation.

## Project Workflow

The following outlines the workflow and key steps within the provided Jupyter notebook:

1. **Import Libraries**
   Import necessary libraries for data handling, image processing, and model training:
    - `os` for file handling
    - `skimage.io` for image loading and saving
    - `sklearn.model_selection` for data splitting
    - `ultralytics` for YOLO model

2. **Set Up Data Directory and Load Data**
    - Define paths to the cat and dog image directories.
    - Load images from these directories and store them in corresponding lists.

3. **Data Splitting**
    - Split the cat and dog data into training and validation sets using `train_test_split` from `sklearn.model_selection`.
    - Print the number of images in each split to verify.

4. **Save Split Data into Corresponding Directories**
    - Create directories for training and validation data for both cats and dogs.
    - Define a function to save the images into these directories with appropriate prefixes.

5. **Model Definition and Training**
    - Define the YOLO model using a pre-trained YOLOv8n model.
    - Train the model on the prepared data with specified epochs and image size.

6. **Evaluate the Model**
    - Use the best model to make predictions on a custom image.
    - Print and analyze the prediction results.

## Results
The trained model is evaluated using a custom image to predict whether it is a cat or a dog. The results and accuracy of the model are about 98%.

## Acknowledgments

- Kaggle for providing datasets
- The open-source community for their valuable libraries and tools