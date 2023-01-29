import cv2
import numpy as np
kamera = cv2.VideoCapture(0)
while True:
    durum, goruntu = kamera.read()
    cv2.putText(goruntu, "Muhammed Yasin", (60, 100),
                cv2.FONT_ITALIC, 1.4, (120, 240, 180), 4)
    cv2.rectangle(goruntu, (200, 200), (300, 300), (124, 45, 78), 4)
    cv2.circle(goruntu, (250, 250), 50, (140, 200, 140), 3)
    cv2.line(goruntu, (0, 40), (40, 0), (141, 52, 240), 4)
    if cv2.waitKey(30) & 0xFF == 32:
        break
    cv2.imshow("kamera", goruntu)
kamera.release()
cv2.destroyAllWindows()
