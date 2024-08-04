import cv2
import numpy as np


COLORS = {
    "red": np.array([255, 0, 0]),
    "green": np.array([0, 255, 0]),
    "blue": np.array([0, 0, 255]),
    "yellow": np.array([255, 255, 0]),
    "purple": np.array([255, 0, 255]),
    "cyan": np.array([0, 255, 255])
}


def color_limits(color):
    color = np.uint8(color)
    hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

    lower_limit = hsv_color[0][0][0] - 10, 100, 100
    upper_limit = hsv_color[0][0][0] + 10, 255, 255

    lower_limit = np.array(lower_limit, dtype=np.uint8)
    upper_limit = np.array(upper_limit, dtype=np.uint8)

    return lower_limit, upper_limit


def display_intro():
    intro_message = """
    Welcome to Color Detection Console Application!
    
    This Python script uses your webcam to detect and highlight specific colors and texts in real-time.
    
    Features:
        - Color Recognition: Detects a user-specified color via the webcam stream.
        
        - Simple Settings: Detects and highlights a user-specified color from the library in the video stream.
    """
    print(intro_message)
    response = input("You are familiar with the program features and agree to continue? [y/n]")
    return response_encounter(response)


def response_encounter(response):
    while True:
        if response.lower() == 'y':
            return True
        elif response.lower() == 'n':
            return False
        else:
            response = input("Your answer was not recognized. Please answer only y (Yes) or n (No): ")


