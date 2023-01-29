import cv2
import numpy as np
resim = np.zeros((300, 300, 3), dtype="uint8")
c = 1
while True:
    if c % 3 == 0:
        resim[:, :] = (100, 20, 220)
        for i in range(81):
            resim[50+i:i+55, i+50:i+60] = (100, 140, 40)
        for i in range(81):
            resim[130-i:135-i, 140+i:150+i] = (100, 140, 40)
        resim[130:250, 135:145] = (100, 140, 40)
    elif c % 5 == 0:
        resim[:, :] = (0, 100, 50)
        for i in range(81):
            resim[50+i:i+55, i+50:i+60] = (120, 40, 40)
        for i in range(81):
            resim[130-i:135-i, 140+i:150+i] = (120, 40, 40)
            resim[130:250, 135:145] = (120, 40, 40)
    elif c % 10 == 0:
        resim[:, :] = (100, 100, 50)
        for i in range(81):
            resim[50+i:i+55, i+50:i+60] = (20, 140, 140)
        for i in range(81):
            resim[130-i:135-i, 140+i:150+i] = (20, 140, 140)
            resim[130:250, 135:145] = (20, 140, 140)
    else:
        resim[:, :] = (10, 20, 50)
        for i in range(81):
            resim[50+i:i+55, i+50:i+60] = (200, 160, 60)
        for i in range(81):
            resim[130-i:135-i, 140+i:150+i] = (200, 160, 60)
            resim[130:250, 135:145] = (200, 160, 60)
    cv2.imshow("resim", resim)
    if cv2.waitKey(100) & 0xFF == 32:
        break
    c += 5
cv2.waitKey(0)
cv2.destroyAllWindows()
