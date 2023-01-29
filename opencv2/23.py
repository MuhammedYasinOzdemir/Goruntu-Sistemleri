import cv2
import numpy as np
resim = np.ones((256, 256), np.uint8)
for i in range(256):
    resim[:, i] = i


def nothing(x):
    pass


cv2.namedWindow("resim", cv2.WINDOW_NORMAL)
cv2.createTrackbar("eşik", "resim", 0, 255, nothing)
cv2.createTrackbar("max", "resim", 0, 255, nothing)
while True:
    esik = cv2.getTrackbarPos("eşik", "resim")
    max = cv2.getTrackbarPos("max", "resim")
    ret, thres = cv2.threshold(resim, esik, max, cv2.THRESH_BINARY)
    cv2.imshow("thres", thres)
    cv2.imshow("resim", resim)
    if cv2.waitKey(1) & 0xFF == 32:
        break
cv2.destroyAllWindows()
