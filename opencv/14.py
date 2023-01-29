import cv2
import numpy as np
resim = cv2.imread("indir.jpg")
cv2.imshow("resim", resim)  # filtreleme
resimgri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)  # buda grileştirme
# bu da farklı tonlama orneği
ikikatb = cv2.pyrUp(resim)
ikikatk = cv2.pyrDown(resim)
a = cv2.cvtColor(resim, cv2.COLOR_LAB2RGB)
cv2.imshow("resimm", a)  # filtrele
cv2.imshow("resimb", ikikatb)
cv2.imshow("resimk", ikikatk)
cv2.imshow("resimgri", resimgri)
cv2.waitKey(0)
cv2.destroyAllWindows()
