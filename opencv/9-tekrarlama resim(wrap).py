import cv2
import numpy as np
resim = cv2.imread("aaa.jpg")
tekrar = cv2.copyMakeBorder(
    resim, 400, 400, 368, 368, cv2.BORDER_WRAP)
print(resim.shape)
cv2.imshow("tekrarlanmış resim", tekrar)

cv2.waitKey(0)
cv2.destroyAllWindows()
