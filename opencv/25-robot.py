import re
import cv2
import numpy as np
from random import randint


def robot(sayi):
    resim = np.zeros((400, 400, 3), dtype="uint8")
    # (120, 160, 200) insan rengi
    resim[:, :] = (sayi*randint(0, 3), sayi*randint(0, 3), sayi*randint(0, 3))
    cv2.circle(resim, (200, 100), 80, (120, 160, 200), 4)
    resim[100:300, 80:320] = (150, 100, 20)
    cv2.rectangle(resim, (80, 100), (320, 300), (150, 100, 20), 4)  # kaburga
    cv2.line(resim, (120, 100), (280, 100), (20, 160, 200), 4)
    cv2.rectangle(resim, (150, 60), (170, 75), (120, 160, 200), 4)  # göz
    cv2.rectangle(resim, (230, 60), (250, 75), (120, 160, 200), 4)  # göz
    resim[66:71, 155:165] = (0, 0, 200)
    resim[66:71, 235:245] = (0, 0, 200)
    a = cv2.copyMakeBorder(resim, 100, 100, 300, 300, cv2.BORDER_REPLICATE)
    cv2.rectangle(a, (250, 220), (380, 260), (120, 160, 200), 4)  # kol
    a[220:260, 250:380] = (140, 100, 80)  # kol
    for i in range(5):  # tırnak
        cv2.line(a, (220, 230+i*5), (250, 230+i*5), (120, 160, 200), 2)
    cv2.rectangle(a, (620, 220), (750, 260), (120, 160, 200), 4)  # kol
    a[220:260, 620:750] = (140, 100, 80)  # kol
    for i in range(5):  # tırnak
        cv2.line(a, (750, 230+i*5), (780, 230+i*5), (120, 160, 200), 2)
    for i in range(23):  # kol desen
        cv2.rectangle(a, (250+i*5, 230), (270+i*5, 250), (80, 180, 180), 2)
    for i in range(17):  # kol desen
        cv2.rectangle(a, (620+i*5, 230), (670+i*5, 250), (80, 180, 180), 2)
    cv2.line(a, (420, 200), (500, 300), (80, 180, 180), 3)  # yaka
    cv2.line(a, (580, 200), (500, 300), (80, 180, 180), 3)  # yaka
    cv2.line(a, (500, 300), (500, 400), (80, 180, 180), 3)  # yaka
    cv2.rectangle(a, (400, 320), (450, 360), (10, 60, 140), 4)  # cep
    cv2.rectangle(a, (550, 320), (600, 360), (40, 60, 140), 4)  # cep
    a[400:550, 550:600] = (20, 100, 200)
    a[400:550, 400:450] = (20, 100, 200)
    cv2.rectangle(a, (550, 400), (600, 550), (120, 160, 200), 4)
    cv2.rectangle(a, (400, 400), (450, 550), (120, 160, 200), 4)
    for i in range(14):
        cv2.rectangle(a, (400, 400+i*10), (450, 420+i*10), (140, 180, 50), 2)
    for i in range(14):
        cv2.rectangle(a, (550, 400+i*10), (600, 420+i*10), (140, 180, 50), 2)
    cv2.imshow("robot", a)


while True:
    sayi = randint(0, 80)
    robot(sayi)
    if cv2.waitKey(20) & 0xFF == 32:
        break
cv2.destroyAllWindows()
