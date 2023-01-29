import cv2
import numpy as np
import time

cam = cv2.VideoCapture(0)


lower = np.array([160, 100, 100])
upper = np.array([180, 255, 255])
kernel = np.ones((3, 3), np.uint8)
min_dist = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))/12
print(min_dist)
param1 = 90  # thresh hol degeri
param2 = 50  # nekadar kucukse o kadar daire
c = 1
while cam.isOpened():
    _, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=3)
    mask = cv2.blur(mask, (19, 19))
    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, min_dist,
                               param1=param1, param2=param2, minRadius=0, maxRadius=0)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for x, y, r in circles[0, :]:
            cv2.circle(frame, (x, y), r, (0, 0, 200), 3)
            cv2.circle(frame, (x, y), 5, (0, 0, 240), 3)
            cv2.line(frame, (x, y+r+int(r/2.5)),
                     (x, y-r-int(r/2.5)), (0, 0, 200), 3)
            cv2.line(frame, (x+r+int(r/2.5), y),
                     (x-r-int(r/2.5), y), (0, 0, 200), 3)
            cv2.putText(frame, "x : {}   y: {}   r: {}".format(x, y, r), (15, 30),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (200, 50, 150), 1, cv2.LINE_AA)
            cv2.putText(frame, "Kirmizi Alan Goruldu.", (320, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                        1, (200, 100, 20), 1, cv2.LINE_AA)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    if cv2.waitKey(16) & 0xFF == 32:
        break

cam.release()
cv2.destroyAllWindows()
