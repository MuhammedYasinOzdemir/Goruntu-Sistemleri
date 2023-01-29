import cv2
resim = cv2.imread("grott.jpg")
cv2.imshow("aa", resim)
cv2.imwrite("kızkulesi.jpg", resim)
cv2.waitKey(0)

cv2.destroyAllWindows()
