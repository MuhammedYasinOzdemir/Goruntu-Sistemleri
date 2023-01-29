import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("kızkulesi.jpg")
kesit = img[300:500, 300:500]
reflekt = cv2.copyMakeBorder(img, 200, 200, 200, 200, cv2.BORDER_REFLECT)
wrap = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_WRAP)
consant = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_CONSTANT)
replicate = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_REPLICATE)
# satır ,satır toplam miktar,sutun sayısı, plt.imshow(img), plt.title("orjinal")
plt.subplot(231), plt.imshow(img), plt.title("orjinal")
plt.subplot(232), plt.imshow(kesit), plt.title("kesit")
plt.subplot(233), plt.imshow(reflekt), plt.title("reflekt")
plt.subplot(234), plt.imshow(wrap), plt.title("wrap")
plt.subplot(235), plt.imshow(consant), plt.title("consant")
plt.subplot(236), plt.imshow(replicate), plt.title("replicate")
plt.show()
cv2.destroyAllWindows()
