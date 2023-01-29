
import cv2
import numpy as np
x = np.uint8([250])
y = np.uint8([10])
print(x, y)
print(x+y)  # toplar 256 ya gore modu alır
print(cv2.add(x, y))  # max değeri alır
# 0 yerine baska bir şey varsa parlaklık artar
print(cv2.addWeighted(x, 0.5, y, 0.5, 0))
img1 = cv2.imread("5.png")
img2 = cv2.imread("aa.jpg")
img1 = img1[0:700, 0:900]
img2 = img2[0:700, 0:900]
t1 = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
t2 = cv2.addWeighted(img1, 0.4, img2, 0.6, 50)
t3 = cv2.add(img1, img2)
cv2.imshow("agırlıklı 1", t1)
cv2.imshow("agırlıklı 2", t2)
cv2.imshow("normal topma", t3)
cv2.waitKey(0)
cv2.destroyAllWindows()
