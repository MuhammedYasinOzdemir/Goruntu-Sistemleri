import re
import cv2
import numpy as np
resim = np.zeros((330, 800, 3), dtype="uint8")  # y ,x,kanal sayisi,tipi
resim[:, :] = (100, 100, 100)
for i in range(81):
    resim[20+i:i+25, i+20:i+30] = (200, 140, 40)
for i in range(81):
    resim[100-i:105-i, 110+i:120+i] = (200, 140, 40)
resim[105:200, 105:115] = (200, 140, 40)
resim[80:90, 210:320] = (200, 140, 40)
resim[80:200, 320:330] = (200, 140, 40)
resim[200:210, 220:330] = (200, 140, 40)
resim[150:210, 210:220] = (200, 140, 40)
resim[150:160, 210:300] = (200, 140, 40)
resim[80:90, 380:480] = (200, 140, 40)
resim[80:150, 370:380] = (200, 140, 40)
resim[150:160, 370:480] = (200, 140, 40)
resim[160:210, 470:480] = (200, 140, 40)
resim[200:210, 370:480] = (200, 140, 40)
resim[80:210, 530:540] = (200, 140, 40)
resim[40:60, 530:540] = (200, 140, 40)
resim[80:210, 590:600] = (200, 140, 40)
resim[80:90, 585:720] = (200, 140, 40)
resim[80:210, 710:720] = (200, 140, 40)
for i in range(60):
    for j in range(800):
        resim[i+270, j] = [0, 0, 0]
for k in range(0, 40):
    for i in range(60):
        for j in range(10):
            resim[i+270, 20*k + j] = [255, 255, 255]
resim[0:300, 0:10] = [255, 255, 255]
resim[0:300, 790:800] = [0, 0, 0]
for i in range(10):
    for j in range(800):
        resim[i, j] = [0, 0, 0]
for k in range(0, 40):
    for i in range(10):
        for j in range(10):
            resim[i, 20*k + j] = [255, 255, 255]
resim = cv2.copyMakeBorder(resim, 60, 0, 10, 10, cv2.BORDER_REPLICATE)
cv2.imshow("resim", resim)
cv2.imwrite("resim.jpg", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
