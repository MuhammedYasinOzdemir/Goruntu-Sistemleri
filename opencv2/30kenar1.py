
import cv2
import numpy as np  # kenar algilama
resim = cv2.imread("ss.jpg", 0)
resim = cv2.pyrDown(resim)
# resim,otomatk icin -1,x tarafi,y tarafi,matris
soblex1 = cv2.Sobel(resim, -1, 1, 0, ksize=5)
# resim,float donusturuyor,c,y,otamik seciyor
soblex2 = cv2.Sobel(resim, cv2.CV_64F, 1, 1, ksize=5)
soblex2 = np.absolute(soblex2)  # mutlak deger alinir
soblex2 = np.uint8(soblex2)  # int sayilara donusturur
Laplacian1 = cv2.Laplacian(resim, -1, ksize=1)
Laplacian2 = cv2.Laplacian(resim, -1, ksize=5)
Laplacian3 = cv2.Laplacian(resim, cv2.CV_64F, ksize=3)
Laplacian1 = np.absolute(Laplacian3)
Laplacian1 = np.uint8(Laplacian3)
Canny1 = cv2.Canny(resim, 50, 200)
Canny2 = cv2.Canny(resim, 0, 120)
Canny3 = cv2.Canny(resim, 200, 250)
cv2.imshow("Canny 1", Canny1)
cv2.imshow("Canny 2", Canny2)
cv2.imshow("Canny 3", Canny3)
cv2.imshow("Lablician 2", Laplacian2)
cv2.imshow("Lablician 3", Laplacian3)
cv2.imshow("Lablican 1", Laplacian1)
cv2.imshow("soblex1", soblex1)
cv2.imshow("soblex2", soblex2)
cv2.waitKey(0)
cv2.destroyAllWindows()
