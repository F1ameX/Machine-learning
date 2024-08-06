import cv2


webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
