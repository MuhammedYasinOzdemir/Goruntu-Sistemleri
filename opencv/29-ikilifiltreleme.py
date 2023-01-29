import cv2
resim = cv2.imread("meanfilter.png")
a1 = cv2.bilateralFilter(resim, 9, 75, 75)
cv2.imshow("ikili", a1)
cv2.imshow("resim", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
