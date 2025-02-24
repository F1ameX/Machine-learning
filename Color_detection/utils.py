import cv2
import numpy as np


COLORS = {
    "green": np.array([0, 255, 0]),
    "blue": np.array([0, 0, 255]),
    "yellow": np.array([255, 255, 0]),
    "purple": np.array([255, 0, 255]),
}


def color_limits(color):
    color = np.uint8([[color]])
    hsv_color = cv2.cvtColor(color, cv2.COLOR_RGB2HSV)
    hue = hsv_color[0][0][0]

    if hue >= 165:
        lower_limit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upper_limit = np.array([180, 255, 255], dtype=np.uint8)
    elif hue <= 15:
        lower_limit = np.array([0, 100, 100], dtype=np.uint8)
        upper_limit = np.array([hue + 10, 255, 255], dtype=np.uint8)
    else:
        lower_limit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upper_limit = np.array([hue + 10, 255, 255], dtype=np.uint8)

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
    response = input("Are you familiar with the program features and agree to continue? [y/n] ")
    return response_handler(response)


def display_agreement():
    agree_message = """
    The next step is your consent to use the webcam.
    The application will use the image from your webcam, display it on the screen 
    and detect any color you choose in the next step
    """
    print(agree_message)
    response = input("Do you agree with the rules and are ready to continue? [y/n] ")
    return response_handler(response)


def display_selection():
    selection_message = """
    There are only 4 colors available:
    1. Green
    2. Blue
    3. Yellow
    4. Purple
    
    You can choose any color of this list you want. Just type name of color. Example: yellow. 
    """
    print(selection_message)
    color = input("What color would you like to detect?\n")
    return color_handler(color)


def response_handler(response):
    while True:
        if response.lower() == 'y':
            return True
        elif response.lower() == 'n':
            return False
        else:
            response = input("Your answer was not recognized. Please answer only y (Yes) or n (No): ")


def color_handler(color):
    wrong_message = """
    You color was not recognized. Please make sure you have selected a valid color from the list: 
    1. Green
    2. Blue
    3. Yellow
    4. Purple
    Try again. Just type name of color. Example: yellow. 
    """

    while True:
        if color.lower() in COLORS:
            return COLORS[color]
        else:
            print(wrong_message)
            color = input("What color would you like to detect?")
