import cv2
import numpy as np
filter1 = np.array([[-1, -1, -1],  # keskinlesme filtresi
                   [-1, 9, -1],
                   [-1, -1, -1]])
filter2 = np.array([[0, 0, -1, 0, 0],  # kendi fitrem
                   [0, 0, 1, 0, 0],
                   [-1, 1, 1, 1, -1],
                   [0, 0, 1, 0, 0],
                   [0, 0, -1, 0, 0]])
resim = cv2.imread("ab.jpg")
dst1 = cv2.filter2D(resim, -1, filter1)  # resim,aynı hal olmasi için -1,matris
dst2 = cv2.filter2D(resim, -1, filter2)+15
cv2.imshow("dst2", dst2)
cv2.imshow("resim", resim)
cv2.imshow("dst1", dst1)
cv2.waitKey(0)
cv2.destroyAllWindows()
