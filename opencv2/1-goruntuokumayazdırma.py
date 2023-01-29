import cv2
from matplotlib import pyplot as plt
resim = cv2.imread("kızkulesi.jpg", 0)
# penceryi istediğimiz gibi hareket ettirmemize yarar.
cv2.namedWindow("resim", cv2.WINDOW_GUI_NORMAL)
cv2.imshow("resim", resim)
# cmap bir şey yazılırsa ona gore kaydeder yazılmasasa normal gosterir ama rgb ye gore
plt.imshow(resim, cmap="gray")
plt.show()
k = cv2.waitKey(0)
if k == 27:
    cv2.imwrite("kızkulesigri.jpg", resim)
    print("resim kaydedildi")
elif k == 32:
    print("space tusuna basıldı.")
cv2.destroyAllWindows()
