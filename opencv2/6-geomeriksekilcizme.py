import cv2
import numpy as np
img = np.zeros((600, 600, 3), np.uint8)
cv2.line(img, (50, 50), (550, 50), (120, 5, 255), 4)
cv2.rectangle(img, (100, 100), (200, 300),
              (100, 200, 150), -1)  # -1 içini doldurur
cv2.circle(img, (400, 200), 100, (120, 10, 20), 4)
cv2.putText(img, "merhaba", (80, 400),
            cv2.FONT_HERSHEY_COMPLEX_SMALL, 4, (120, 140, 200), 4, cv2.LINE_AA)
cv2.ellipse(img, (255, 255), (200, 300), 0, 0, 180,
            (152, 140, 200), 4)  # resim,uzunluk(mesafe,yukseklik),yayacı,baslngıcacı,son acı,renk,kalınlık
cv2.imshow("resim", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
