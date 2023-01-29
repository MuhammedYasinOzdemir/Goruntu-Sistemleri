import cv2
import numpy as np
resim = np.zeros((500, 500, 3), dtype="uint8")
resim[:, :] = (100, 200, 15)
resim[20:120, 20:30] = (185, 80, 200)
resim[120:130, 20:120] = (185, 80, 200)
resim[20:130, 120:130] = (185, 80, 200)
resim[130:240, 70:80] = (185, 80, 200)

cv2.imshow("resim", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
