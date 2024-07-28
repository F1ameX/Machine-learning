# Digit Recognition neural network model
This repository contains a simple neural network project aimed to recognize the handwritten digits. The project uses the MNIST dataset consists different handwritten images.

## Project structure
- `Digit-recognition/`
  - `sample.ipynb/`: Saved final digit recognition model

## Project Workflow

The following outlines the workflow and key steps within the provided Jupyter notebook:

1. **Import Libraries and Load Model**
    - Import essential libraries like TensorFlow, OpenCV, and Matplotlib.
    - Load a pre-trained Keras model.

2. **Define Functions and Hyperparameters**
    - Define key constants and functions used throughout the notebook, such as `IMG_SIZE`.

3. **Load and Preprocess Data**
    - Load images and preprocess them by resizing, normalizing, and reshaping to fit the model's input requirements.

4. **Model Evaluation**
    - Evaluate the loaded model on test data to check its accuracy and performance.

5. **Load Custom Image**
    - Load a custom image using OpenCV and display it using Matplotlib.

6. **Image Preprocessing**
    - Convert the custom image to grayscale.
    - Resize the image to match the model's input size.
    - Normalize the image and reshape it to the required input shape.

7. **Prediction**
    - Use the model to predict the class of the custom image.
    - Output the predicted class label.

## Results
The model has shown accuracy about average 95% and losses about 7%

## Acknowledgments

- Kaggle and MNIST for providing dataset
- The open-source community for their valuable libraries and tools.