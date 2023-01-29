import cv2
import numpy as np
img = cv2.imread("s.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
min_dist = img.shape[0]/8
param1 = 100
param2 = 50
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT,
                           1, min_dist, param1=param1, param2=param2)
circles = np.uint16(np.around(circles))
if circles is not None:
    for x, y, r in circles[0, :]:
        cv2.circle(img, (x, y), r, (120, 100, 20), 4)
        cv2.circle(img, (x, y), 2, (0, 20, 50), 3)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
