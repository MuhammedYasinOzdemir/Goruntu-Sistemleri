import cv2
import numpy as np
resim1 = np.zeros((400, 800), np.uint8)
resim1[0:400, 0:400] = 255
resim2 = np.zeros((400, 800), np.uint8)
for i in range(100):
    cv2.circle(resim2, (400, 200), 100-i, 255, 4)
bitvise_and = cv2.bitwise_and(resim1, resim2)
bitvise_or = cv2.bitwise_or(resim1, resim2)
# birbirinden farklıysa beyaz döndürür aynıysa siyah
bitvise_xor = cv2.bitwise_xor(resim1, resim2)
bitvise_not = cv2.bitwise_not(resim1, resim2)
cv2.imshow("resim 1", resim1)
cv2.imshow("resim 2", resim2)
cv2.imshow("bitwise and", bitvise_and)
cv2.imshow("bitwise or", bitvise_or)
cv2.imshow("bitwise_xor", bitvise_xor)
cv2.imshow("bitwise not", bitvise_not)
cv2.waitKey(0)
cv2.destroyAllWindows()
