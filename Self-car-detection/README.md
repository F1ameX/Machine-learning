# Car Detection and Visualization Project

This project focuses on visualizing bounding boxes around various objects detected in images from a car camera. The objects include cars, trucks, pedestrians, bicycles, and traffic lights. The project leverages OpenCV for image processing and matplotlib for visualization.

## Project Structure

- `Car-Detection/`
    - `sample.ipynb`: Jupyter notebook for the project code.
    - `README.md`: Project documentation.

## Project Workflow

1. **Environment Setup**
   - Install the required libraries: NumPy, pandas, OpenCV, and matplotlib.

2. **Data Loading**
   - Load the training labels from `labels_train.csv` using pandas. This file contains bounding box coordinates and class IDs for each detected object.

3. **Data Exploration**
   - Generate a summary of the dataset including data types, number of unique values, and count of missing values for each column to understand its structure.

4. **Class Identification**
   - Identify and list all unique classes (`class_id`) present in the dataset. This helps in categorizing objects for visualization.

5. **Image and Bounding Box Extraction**
   - For each unique class, randomly select a row from the dataset and extract the corresponding image using OpenCV.
   - Extract the bounding box coordinates (`xmin`, `xmax`, `ymin`, `ymax`) for the selected object.

6. **Labels Mapping**
   - Create a dictionary to map `class_id` to descriptive labels such as 'Car', 'Truck', 'Pedestrian', 'Bicycle', and 'Traffic Light'.

7. **Visualization**
   - For each class, display the corresponding image with the bounding box overlaid.
   - Use matplotlib to draw rectangles around detected objects using the bounding box coordinates, with labels displayed in the plot title.

## Results
- The project successfully loads and visualizes images with bounding boxes for different object classes detected in car camera photos.

## Acknowledgments
- **OpenCV and Matplotlib**: For providing robust libraries to handle image processing and visualization.
- **Dataset Providers**: Thanks to the data providers for the labeled images that make this project possible.

This project serves as a practical example of using computer vision techniques to detect and visualize objects in real-world images. Future improvements could include extending the functionality to real-time object detection, exploring advanced models for detection, and refining visualization techniques.
