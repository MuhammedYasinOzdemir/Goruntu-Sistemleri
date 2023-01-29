import re
import cv2
import numpy as np
resim = cv2.imread("kartal.jpg")
resim[:, :, 0] = 100  # 0 mavi 1 yesil 2 kırmızı bu hepsine efekt uygulma
# belli bir yere uygulama birincisi y paremtersi ikincix paremetre sol kose refrenas alınarak
resim[100:200, 15:20, 2] = 200
cv2.imshow("resim", resim)

cv2.waitKey(0)
cv2.destroyAllWindows(0)
