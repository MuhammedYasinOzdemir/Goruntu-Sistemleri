import cv2
from cv2 import destroyAllWindows
import numpy as np
kamera = cv2.VideoCapture(
    "Python ile Görüntü İşleme - Resimde Belli Bölgeyi Dikdörtgen İçine Alma.mp4")
while True:
    ret, goruntu = kamera.read()
    if cv2.waitKey(30) & 0xFF == 32:
        break
    cv2.imshow("goruntu", goruntu)
kamera.release()
destroyAllWindows()
