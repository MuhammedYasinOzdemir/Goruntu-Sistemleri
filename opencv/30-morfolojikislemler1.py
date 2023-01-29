import cv2
import numpy as np
resim = cv2.imread("j.png")
resim = cv2.pyrUp(resim)
# matris ne kadr kucukse o kadar ayrıntılı
kernel = np.ones((3, 3), np.uint8)
# resimdeki beyazlıkları genişletir
dilation = cv2.dilate(resim, kernel, iterations=1)
dilation2 = cv2.dilate(resim, kernel, iterations=2)  # daha kalın olur
# resimde beyazlıkları azaltır
erosion = cv2.erode(resim, kernel, iterations=1)
dilation3 = cv2.dilate(erosion, kernel, iterations=1)
cv2.imshow("erosion1", erosion)
cv2.imshow("resmi aşındırıp genişletmek", dilation3)
cv2.imshow("dilation2", dilation2)
cv2.imshow("dilation 1", dilation)
cv2.imshow("resim", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
