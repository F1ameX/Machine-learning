# YOLO Welding Defect Detection on Eponymous Dataset
This repository contains a project aimed at detecting objects in a custom dataset using the YOLO (You Only Look Once) model. The project involves model training, validation, and evaluation on test images.

## Project Structure
- `Welding-defect-detection/`
    - `sample.ipynb`: Jupyter notebook containing the entire workflow of model training, validation, and evaluation.

## Project Workflow

The following outlines the workflow and key steps within the provided Jupyter notebook:

1. **Import Libraries**
   Import necessary libraries for file handling, image processing, and model training:
    - `os` for file handling
    - `random` for random sampling
    - `PIL` for image display
    - `ultralytics` for YOLO model
    - `IPython.display` for displaying images in the notebook

2. **Model Training**
    - Load the pre-trained YOLOv8n model.
    - Train the model on the custom dataset specified in `data/data.yaml` for a set number of epochs and image size.

3. **Model Validation**
    - Validate the trained model on the validation dataset specified in `data/data.yaml`.

4. **Model Evaluation on Test Images**
    - List images in the test directory.
    - Randomly sample a subset of test images.
    - Define a directory to save detection results.
    - Perform object detection on the sampled test images.
    - Save and display the detection results for visual inspection.

## Results
The trained model is evaluated on randomly selected test images. The detection results are saved and displayed for visual analysis.

## Acknowledgments

- Kaggle for providing datasets
- The open-source community for their valuable libraries and tools