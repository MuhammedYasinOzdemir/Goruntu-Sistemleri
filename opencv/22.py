import cv2
import numpy as np
kamera = cv2.VideoCapture(0)
durum, goruntu = kamera.read()
# 480,640
while True:
    durum, goruntu = kamera.read()
    cv2.line(goruntu, (0, 0), (640, 480), (120, 140, 20), 4)
    cv2.line(goruntu, (0, 480), (640, 0), (120, 140, 20), 4)
    kucult = cv2.pyrDown(goruntu)
    a = cv2.pyrDown(kucult)
    uzatılmıs = cv2.copyMakeBorder(
        a, 480, 140, 640, 640, cv2.BORDER_REFLECT)
    if cv2.waitKey(10) & 0xFF == 32:
        break
    cv2.imshow("goruntu", uzatılmıs)
kamera.release()
cv2.destroyAllWindows()
