import cv2
import numpy as np
resim = cv2.imread("aaa.jpg")
cerceve = cv2.copyMakeBorder(
    resim, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=(100, 200, 42))
cv2.imshow("Cerceveli resim", cerceve)
cv2.waitKey(0)
cv2.destroyAllWindows()
