import cv2
import numpy as np

resim = cv2.imread("insan4.jpg")
# burada ayırette n x y eksenine gore yapılır birinci sol alt ikinci üst sağ kose dorduncu renk besinc kalınlık(1-9) arası
cv2.rectangle(resim, (75, 310), (275, 20), [24, 100, 255], 4)
cv2.imshow("resim", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
