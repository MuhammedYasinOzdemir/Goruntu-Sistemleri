import cv2
import numpy as np
resim = np.ones((255, 255), np.uint8)
for i in range(255):
    resim[:, i] = i
ret, thres = cv2.threshold(resim, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("thres", thres)
cv2.imshow("resim", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
