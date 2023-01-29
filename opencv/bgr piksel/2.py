import cv2
import numpy as np

resim = cv2.imread("kartal.jpg")
for i in range(60):
    for j in range(200):
        resim[i, j] = [0, 0, 0]
for k in range(0, 10):
    for i in range(60):
        for j in range(10):
            resim[i, 20*k + j] = [200, 200, 200]
cv2.imshow("kartal resmi", resim)
cv2.imwrite("beşiktaş.jpg", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
