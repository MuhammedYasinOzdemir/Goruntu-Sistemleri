import cv2
resim = cv2.imread("elma.jpg", 0)
# simple thresholding
ret1, thres1 = cv2.threshold(resim, 127, 255, cv2.THRESH_BINARY)
# otsu thres holding otomatik yapar
ret2, thres2 = cv2.threshold(resim, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("resim", resim)
cv2.imshow("simple", thres1)
cv2.imshow("otsu", thres2)
cv2.waitKey(0)
cv2.destroyAllWindows()
