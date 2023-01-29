import cv2
import numpy as np
resim = cv2.imread("aaa.jpg")
uzatılmısresim = cv2.copyMakeBorder(
    resim, 100, 100, 300, 300, cv2.BORDER_REPLICATE)
cv2.imshow("uzatılmıs resim", uzatılmısresim)
cv2.waitKey(0)
cv2.destroyAllWindows()
