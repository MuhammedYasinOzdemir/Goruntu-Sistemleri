import cv2
import numpy as np
resim1 = cv2.imread("sumeyye.jpg")
resim2 = cv2.imread("insan4.jpg")

print(resim1[100, 300])
print(resim2[100, 300])
print(resim1[100, 300]+resim2[100, 300])
cv2.imshow("resim 1", resim1)
cv2.imshow("resim2", resim2)
cv2.waitKey(0)
cv2.destroyAllWindows()
