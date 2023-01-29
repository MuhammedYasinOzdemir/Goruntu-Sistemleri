import re
import cv2
import numpy as np
resim = cv2.imread("insan4.jpg")
kesit = resim[100:300, 90:260]
resim[105:305, 450:620] = kesit
print(resim[(300, 440)])
resim[:, :, 0] = 255  # bu resme ekleme yazpar orjinal renk değişmez(efekt)
resim[100:200, 20:100, 2] = 200
# bu orjinal renk değişir(renk değişimi)
resim[0:100, 20:80] = (100, 20, 200)#kare parentez y x yuvarlak parantez x y
cv2.imshow("insan", resim)
cv2.imshow("kesit", kesit)
cv2.waitKey(0)
cv2.destroyAllWindows()
