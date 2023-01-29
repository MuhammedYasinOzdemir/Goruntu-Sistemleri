import cv2
import numpy as np
img = cv2.imread("aa.jpg")
img = cv2.resize(img, (300, 300))
satır, sutun = img.shape[:2]
# merkez ,döndürme derecesi,resim boyutu kücültülmesse kayıp olur
rotation_matris = cv2.getRotationMatrix2D((sutun/2, satır/2), 30, 1)
img_rotation = cv2.warpAffine(
    img, rotation_matris, (sutun+100, satır+100))  # resim,matris,resmin yeni boyutları

cv2.imshow("resim", img)
cv2.imshow("rotation", img_rotation)
cv2.waitKey(0)
cv2.destroyAllWindows()
