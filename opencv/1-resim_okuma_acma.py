import cv2
import numpy as np
# resimin alınması okunmasısağlanır
resim = cv2.imread("C:\\Users\\User\\Desktop\\pyhton\\opencv\\kartal.jpg")
cv2.imshow("Resim 1", resim)  # birinci paremetre baslık ikinci resim
cv2.waitKey(0)  # kapanmasını engeller
cv2.destroyAllWindows()  # butun her seyi kaptır sonda
