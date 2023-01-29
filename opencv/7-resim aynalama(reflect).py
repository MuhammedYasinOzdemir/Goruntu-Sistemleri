import cv2
import numpy as np
resim = cv2.imread("aaa.jpg")
aynaresim = cv2.copyMakeBorder(
    resim, 360, 20, 350, 750, cv2.BORDER_REFLECT)  # reflect komutu kullanılır
cv2.imshow("aynalanan resim", aynaresim)
cv2.imwrite("aynalanan kus remi.jpg", aynaresim)
cv2.waitKey(0)
cv2.destroyAllWindows()
