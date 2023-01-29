import cv2
import numpy as np
import matplotlib.pyplot as plt
resim = np.ones((256, 256), np.uint8)
for i in range(256):
    resim[:, i] = i
_, bınary = cv2.threshold(resim, 120, 255, cv2.THRESH_BINARY)
_, bınary_inv = cv2.threshold(resim, 120, 255, cv2.THRESH_BINARY_INV)
_, trunc = cv2.threshold(resim, 120, 255, cv2.THRESH_TRUNC)
_, tozero = cv2.threshold(resim, 120, 255, cv2.THRESH_TOZERO)
_, tozero_inv = cv2.threshold(resim, 120, 255, cv2.THRESH_TOZERO_INV)
resimler = [resim, bınary, bınary_inv, trunc, tozero, tozero_inv]
baslık = ["resim", "bınary", "bınary_inv", "trunc", "tozero", "tozero_inv"]
for i in range(6):
    plt.subplot(
        3, 3, i+1), plt.imshow(resimler[i], "gray"), plt.title(baslık[i])
plt.show()
cv2.imshow("resim", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
