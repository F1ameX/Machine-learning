import cv2
from util import color_limits


webcam = cv2.VideoCapture(0)
while True:
    ret, frame = webcam.read()

    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_limit, upper_limit = color_limits(255)

    mask = cv2.inRange(hsv_image, lower_limit, upper_limit)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


webcam.release()
cv2.destroyAllWindows()
