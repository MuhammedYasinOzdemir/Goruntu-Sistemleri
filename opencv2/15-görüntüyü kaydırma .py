import cv2
import numpy as np
img = cv2.imread("aa.jpg")
img = cv2.resize(img, (300, 300))
satır, sutun = img.shape[:2]
translation_matrix = np.float32([
    [1, 0, 50],  # 50 sağa kaydırmak
    [0, 1, 50]  # 50 aiağı kaydırma
])
img_translation = cv2.warpAffine(
    img, translation_matrix, (sutun+100, satır+100))
cv2.imshow("resim", img)
cv2.imshow("translation", img_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()
