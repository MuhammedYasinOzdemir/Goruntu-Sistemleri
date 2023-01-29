import cv2
img1 = cv2.imread("ab.jpg")
img2 = cv2.imread("logo.jpg")
img2 = cv2.pyrDown(img2)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
img2_not = cv2.bitwise_not(img2_gray)
ret, mask = cv2.threshold(img2_not, 0, 255, cv2.THRESH_BINARY)
x, y, z = img2.shape
roi = img1[0:x, 0:y]
mask_inv = cv2.bitwise_not(mask)
img2_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img1_fg = cv2.bitwise_and(img2, img2, mask=mask)
toplam = cv2.add(img1_fg, img2_bg)
img1[0:x, 0:y] = toplam

cv2.imshow("img_fg", img1_fg)
cv2.imshow("toplam", toplam)
cv2.imshow("img_bt", img2_bg)
cv2.imshow("img 1", img1)
cv2.imshow("mask", mask)
cv2.imshow("roi", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
