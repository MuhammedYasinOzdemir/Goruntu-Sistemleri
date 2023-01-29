import cv2
import numpy as np

kartal = cv2.imread("maxresdefault.jpg")
cv2.imshow("kartal resmi", kartal)
print(kartal.shape)
print("""
    Resim Ozellikleri
1-resimin boyutu:{0}
2-Resmin veri tipi:{1}    
3-Resmin genişligi:{2}
4-Resmin yuksekliği:{3}
5-Resmin kanal sayisi:{4}  """.format(kartal.size, kartal.dtype, kartal.shape[0], kartal.shape[1], kartal.shape[2]))
print(kartal[100, 200]
      )  # birinci renk blue ikinci  green ucuncu red bgr 100 aasağı 200 sağ sol kose refarnas
cv2.waitKey(0)
cv2.destroyAllWindows()
