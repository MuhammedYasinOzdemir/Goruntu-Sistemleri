from wsgiref import headers
import cv2
import numpy as np
cam = cv2.VideoCapture(0)
lower = np.array([160, 155, 85])
upper = np.array([180, 255, 255])
kernel = np.ones((5, 5), np.uint8)
while cam.isOpened():
    ret, frame = cam.read()
    img = frame.copy()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    contour, headers = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    color = (80, 200, 150)
    for i, cnt in enumerate(contour):
        area = cv2.contourArea(cnt)
        if area > 50000 or area < 200:
            continue
        # try:
          #  elipse = cv2.fitEllipse(cnt)
          #  cv2.ellipse(img, elipse, color, 3)
        # except cv2.error as er:
         #   print("error:", er)
        cv2.drawContours(img, contour, i, color, 2)
    cv2.imshow("mask", mask)
    cv2.imshow("img", img)
    if cv2.waitKey(1) & 0xFF == 32:
        break
cam.release()
cv2.destroyAllWindows()
