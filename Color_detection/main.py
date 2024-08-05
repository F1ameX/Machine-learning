import cv2
import sys
from utils import *

if not display_intro():
    sys.exit()

if not display_agreement():
    sys.exit()

webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()

    if not ret or (cv2.waitKey(1) & 0xFF == ord('q')):
        break

    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_limit, upper_limit = color_limits(255)

    mask = cv2.inRange(hsv_image, lower_limit, upper_limit)

    cv2.imshow('frame', frame)


webcam.release()
cv2.destroyAllWindows()
