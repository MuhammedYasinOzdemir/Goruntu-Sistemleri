from calendar import c
import cv2
from cv2 import BORDER_WRAP
import numpy as np
resim = np.zeros((500, 500, 3), dtype="uint8")
resim[:, :] = (100, 150, 160)
cv2.putText(resim, "Yasin", (150, 250),
            cv2.FONT_HERSHEY_TRIPLEX, 2, (80, 20, 50), 3)
cv2.circle(resim, (240, 240), 120, (100, 250, 40), 2)
cv2.line(resim, (80, 80), (400, 80), (0, 75, 150), 5)
cv2.line(resim, (80, 80), (80, 400), (0, 75, 150), 5)
cv2.line(resim, (80, 400), (400, 400), (0, 75, 150), 5)
cv2.line(resim, (400, 80), (400, 400), (0, 75, 150), 5)
cv2.imshow("resim", resim)
kesit = resim[78:402, 78:402]
print(kesit.shape)
tekrarli = cv2.copyMakeBorder(kesit, 324, 0, 324, 324, cv2.BORDER_WRAP)
aynalanmıs = cv2.copyMakeBorder(kesit, 324, 0, 324, 0, cv2.BORDER_REFLECT)
cv2.imshow("kesit", kesit)
cv2.imshow("tekralı", tekrarli)
cv2.imshow("aynalanmıs", aynalanmıs)
cv2.waitKey(0)
cv2.destroyAllWindows()
