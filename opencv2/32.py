import cv2
import numpy as np
cam = cv2.VideoCapture(0)
lower = np.array([160, 155, 85])
upper = np.array([180, 255, 255])
paint = np.ones((480, 640, 3), np.uint8)
paint = cv2.flip(paint, 1)
while cam.isOpened():
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    conteour, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i, cnt in enumerate(conteour):
        area = cv2.contourArea(cnt)
        if area > 50000 or area < 200:
            continue
        color = (100, 50, 150)
        (x, y), radius = cv2.minEnclosingCircle(cnt)
        center = (int(x), int(y))
        cv2.circle(frame, center, int(radius), (0, 200, 0), -1)
        cv2.circle(paint, center, 10, (100, 150, 20), -1)
        cv2.drawContours(frame, conteour, i, (100, 40, 80), 2)
    cv2.imshow("mask", mask)
    cv2.imshow("paint", paint)
    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == 32:
        paint[:] = 255
cam.release()
cv2.destroyAllWindows()
