import cv2
import matplotlib.pyplot as plt
resim = cv2.imread(
    "C:\\Users\\User\\Desktop\\pyhton\opencv\\meanfilter.png", 0)
resim = cv2.resize(resim, None, fx=2, fy=2)
blur = cv2.GaussianBlur(resim, (9, 9), 0)
ret, thres = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

plt.subplot(1, 3, 1), plt.imshow(resim, "gray"), plt.title("orjinal resim")
plt.subplot(1, 3, 2), plt.hist(resim.ravel(), 256), plt.title("histogram")
plt.subplot(1, 3, 3), plt.imshow(
    thres, "gray"), plt.title("thres"), plt.title("thres")
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
