import cv2
import numpy as np
lower = np.array([0, 0, 100])
upper = np.array([150, 240, 255])
camera = cv2.VideoCapture(0)
kernel = np.ones((5, 5), np.uint8)
_, backround = camera.read()
while camera.isOpened():
    ret, frame = camera.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    mask_not = cv2.bitwise_not(mask)
    fg = cv2.bitwise_and(frame, frame, mask=mask_not)
    bg = cv2.bitwise_and(backround, backround, mask=mask)
    dst = cv2.addWeighted(bg, 1, fg, 1, 0)
    dst = cv2.GaussianBlur(dst, (15, 15), 0)
    c = cv2.morphologyEx(dst, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("dst", dst)
    cv2.imshow("hsv", hsv)
    cv2.imshow("mask", mask)
    cv2.imshow("frame", frame)
    cv2.imshow("fg", fg)
    cv2.imshow("bg", bg)
    cv2.imshow("c", c)
    if cv2.waitKey(1) & 0xFF == 32:
        break
camera.release()
cv2.destroyAllWindows()
