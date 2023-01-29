import cv2
import numpy as np
kamera = cv2.VideoCapture(0)  # 0 bilgisayar 1 usb 2 video veya adreste olur

while True:
    ret, goruntu = kamera.read()
    cv2.imshow("video", goruntu)
    if cv2.waitKey(30) & 0xFF == 32:  # 32 ASCII KOD KARSILIĞİ
        break
kamera.release()
cv2.destroyAllWindows()
