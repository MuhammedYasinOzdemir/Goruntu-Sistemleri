import cv2
import numpy as numpy
resim = cv2.imread("insan4.jpg")
# x,y alt kose spl x,y ust kose
a = cv2.rectangle(resim, (440, 300), (650, 50), [20, 42, 150], 4)
cv2.imshow("resim", a)
cv2.waitKey(0)
cv2.destroyAllWindows()
