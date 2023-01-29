import cv2
import numpy as np
resim = np.zeros((400, 400, 3), dtype="uint8")
# resim,baslangıc,son,renk,kalınlık     çizgi
cv2.line(resim, (100, 300), (300, 300), (0, 250, 255), 2)
# resim,merkez,yarıcap,renk,kalınlk    daire
cv2.circle(resim, (40, 80), 30, (255, 200, 100), 4)
# resim,sol alt kose,sağ üst kose,renk,kalınlık   kare
cv2.rectangle(resim, (100, 200), (200, 100), [24, 100, 255], 9)
resim[100:200, 100:200] = [0, 255, 255]
cv2.putText(resim, "Merhaba", (80, 60),
            cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (200, 100, 240), 2)  # resim,yazı,yazı tipi,,baslangıc,boyutu(buyukluğu),renk,çizgi kalınlığı    metin
cv2.imshow("resim", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
