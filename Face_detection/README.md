## Face Detection Webcam Project
This repository contains a simple computer vision project that detects faces using a webcam feed.

## Project Structure
- Face_detection/
    - main.py: Main script of the program
    - requirements.txt: Requirements used in the project
    - .gitignore: System git file
    - README.md: Project description

## Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/Face_detection.git
    cd Face_detection/
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  
    # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Ensure your webcam is connected.
2. Run the main script:

    ```bash
    python main.py
    ```

3. A window will open displaying the webcam feed with detected faces highlighted by rectangles. Press 'q' to exit the program.

## Acknowledgements
- The open-source community for their valuable libraries and tools, particularly OpenCV.

## License
This project is licensed under the MIT License.