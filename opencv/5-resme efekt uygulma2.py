import numpy as np
import cv2
resim = cv2.imread("sumeyye.jpg")
resim[542:560, 430:460, 0] = 100
resim[670:700, 500:600, 1] = 100

cv2.imshow("sumeyye", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
