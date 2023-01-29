import cv2
import numpy as np
resim = cv2.imread("aaa.jpg")
cv2.imshow("Resim 3", resim)

print(resim.size)  # resmin boyutunu verir
print(resim.dtype)  # hangi tipte yazıldığını verir
# birinci değer yükseklik ikinci genişlik ücuncu kanal sayısını verir
print(resim.shape)
print(resim)  # piksel piksel matris gosterilir
cv2.waitKey(0)
cv2.destroyAllWindows()
