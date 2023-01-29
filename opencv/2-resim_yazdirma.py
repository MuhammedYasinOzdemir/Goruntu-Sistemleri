import re
import cv2
import numpy as np
resim = cv2.imread("unnamed.jpg", 0)  # 0 siyah beyaz yapar
cv2.imshow("Resim 2", resim)
cv2.waitKey(0)
cv2.imwrite("yeniresim.png", resim)  # resmi yazdırmaya yarar
cv2.destroyAllWindows()
