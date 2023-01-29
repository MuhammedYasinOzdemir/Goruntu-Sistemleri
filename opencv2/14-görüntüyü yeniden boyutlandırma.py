import cv2
resim = cv2.imread("ab.jpg")
r1 = cv2.resize(resim, (300, 300))  # 300 300 halegetirir
r2 = cv2.resize(resim, None, fx=1.5, fy=0.5)  # 1.5 kat x 0.5 kat y uzatır.
# daha  duzgun cıkar
r3 = cv2.resize(resim, None, fx=1.2, fy=1.5, interpolation=cv2.INTER_CUBIC)
cv2.imshow("resim", resim)
cv2.imshow("r1", r1)
cv2.imshow("r2", r2)
cv2.imshow("r3", r3)
cv2.waitKey(0)
cv2.destroyAllWindows()
