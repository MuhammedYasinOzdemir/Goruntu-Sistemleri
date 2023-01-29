import cv2
import numpy as np
resim = cv2.imread("grott.jpg")
resim = cv2.pyrUp(resim)
gray = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3, 3), 0)
canny = cv2.Canny(gray, 100, 150)  # resim,eşikdeğer min,eşik değer max değer
kernel = np.ones((3, 3), np.uint8)


def autocanny(blur, sigma=0.0000005):
    median = np.median(blur)
    lower = int(max(0, 1-sigma)*median)
    upper = int(min(255, 1+sigma)*median)
    canny = cv2.Canny(blur, lower, upper)
    return canny


canny2 = cv2.Canny(blur, 50, 250)
canny3 = autocanny(blur)
cv2.imshow("blur", blur)
cv2.imshow("canny1", canny)
cv2.imshow("canny2", canny2)
cv2.imshow("canny3", canny3)
cv2.imshow("canny4", cv2.morphologyEx(canny3, cv2.MORPH_CLOSE, kernel))
cv2.imshow("hepsi", np.hstack([canny, canny2, canny3]))
cv2.waitKey(0)
cv2.destroyAllWindows()
