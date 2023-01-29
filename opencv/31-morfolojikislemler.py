import cv2
import numpy as np
resim = cv2.imread("j.png")
kernel = np.ones((5, 5), np.uint8)
resim = cv2.pyrUp(resim)
# once erosion(aşındırma) sonra dilation (genişletme) uygulanır.bu gürültülü yerleri idermekte kullanılır
opening = cv2.morphologyEx(resim, cv2.MORPH_OPEN, kernel)
# once dilation(genişletme) sonra erosion (aşındırma) uygulanır.#aşınmış yerleri birleştirmede
closing = cv2.morphologyEx(resim, cv2.MORPH_CLOSE, kernel)
closing2 = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
# dilationdan erosion çıkarılır.
gradyan = cv2.morphologyEx(resim, cv2.MORPH_GRADIENT, kernel)
# orjinal halden opening çıkarır gürültülü yerler gözkür.
tophat = cv2.morphologyEx(resim, cv2.MORPH_TOPHAT, kernel)
# orjinal resim blachat farkı gürültü daha net gözüküt
blachat = cv2.morphologyEx(resim, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("blachat", blachat)
cv2.imshow("tophat", tophat)
cv2.imshow("closing", closing)
cv2.imshow("gradyan", gradyan)
cv2.imshow("closing2", closing2)
cv2.imshow("opening", opening)
cv2.imshow("resim", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
