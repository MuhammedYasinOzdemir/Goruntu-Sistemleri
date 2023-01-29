import cv2
import numpy as np
# resimlerin üst üste eklenmesi
resim = cv2.imread("insan4.jpg")
kesit1 = resim[20:320, 50:300]
kesit2 = resim[20:320, 420:670]
toplam = cv2.add(kesit1, kesit2)
# herzaman son paremetre 0 yuzde toplamı 1 lmalı
agırlıklıtoplam = cv2.addWeighted(kesit1, 0.6, kesit2, 0.4, 0)
cv2.imshow("kesit 1", kesit1)
cv2.imshow("kesit 2", kesit2)
cv2.imshow("toplam", toplam)
cv2.imshow("ağırlıklı toplam", agırlıklıtoplam)
cv2.waitKey(0)
cv2.destroyAllWindows()
