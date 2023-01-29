import cv2
import numpy as np
img = np.zeros((300, 800, 3), np.uint8)


def nothing(x):
    print(x)
    pass


cv2.namedWindow("resim")
cv2.createTrackbar("R", "resim", 0, 255, nothing)
cv2.createTrackbar("G", "resim", 0, 255, nothing)
cv2.createTrackbar("B", "resim", 0, 255, nothing)
cv2.createTrackbar("ON/OF", "resim", 0, 1, nothing)
while True:
    cv2.imshow("resim", img)
    r = cv2.getTrackbarPos("R", "resim")
    g = cv2.getTrackbarPos("G", "resim")
    # değeri alır fonksiyondada yapılabilir
    b = cv2.getTrackbarPos("B", "resim")
    a = cv2.getTrackbarPos("ON/OF", "resim")
    if a:
        img[:] = (b, g, r)
    else:
        img[:] = 0
    if cv2.waitKey(1) & 0xFF == 32:
        break
cv2.destroyAllWindows()
