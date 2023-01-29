import cv2
resim = cv2.imread("meanfilter.png")
median1 = cv2.medianBlur(resim, 3)
median2 = cv2.medianBlur(resim, 5)  # (5,5) matris alır
median3 = cv2.medianBlur(resim, 15)
cv2.imshow("resim", resim)
cv2.imshow("median1", median1)
cv2.imshow("median2", median2)
cv2.imshow("median3", median3)
cv2.waitKey(0)
cv2.destroyAllWindows()
