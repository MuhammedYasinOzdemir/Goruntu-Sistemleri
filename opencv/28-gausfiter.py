import cv2
resim = cv2.imread("meanfilter.png")
gaus1 = cv2.GaussianBlur(resim, (3, 3), 0)
gaus2 = cv2.GaussianBlur(resim, (5, 5), 0)
gaus3 = cv2.GaussianBlur(resim, (7, 7), 0)
cv2.imshow("gaus 1", gaus1)
cv2.imshow("gaus 2", gaus2)
cv2.imshow("gaus 3", gaus3)
cv2.imshow("resim", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
# gaus>median>mean
