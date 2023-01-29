import cv2
import numpy as np
camera = cv2.VideoCapture(0)
while camera.isOpened():
    ret, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 0, 0])
    upper = np.array([150, 150, 150])
    hsv = cv2.inRange(frame, lower, upper)
    res = cv2.bitwise_and(frame, frame, mask=hsv)
    cv2.imshow("hsv", hsv)
    cv2.imshow("res", res)
    if cv2.waitKey(1) & 0xFF == 32:
        break
camera.release()
cv2.destroyAllWindows()
