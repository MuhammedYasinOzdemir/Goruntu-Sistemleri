import cv2
import numpy as np
kamera = cv2.VideoCapture(0)
durum, goruntu = kamera.read()
# 480,640
while True:
    durum, goruntu = kamera.read()
    cv2.line(goruntu, (0, 0), (640, 480), (120, 140, 20), 4)
    cv2.line(goruntu, (0, 480), (640, 0), (120, 140, 20), 4)

    if cv2.waitKey(30) & 0xFF == 32:
        break
    cv2.imshow("goruntu", goruntu)
kamera.release()
cv2.destroyAllWindows()
