# görüntuyu yumaşatmaya yarar arkayı bulanışlastirir
import cv2
# mean filteda matristeki pikseller toplanır piksel sayısına bolup ortaya yazılır.
resim = cv2.imread("meanfilter.png")
# 3 6 9      3 6 9
# 0 27 0     0  6 0 bu hale gelir
# 0 0  9     0  0  9
# resim,matris matris nekadar buyuk olursa o kadar bulanık olur
mean1 = cv2.blur(resim, (10, 10))
mean2 = cv2.blur(resim, (20, 2))  # x,y
cv2.imshow("orjinal resim", cv2.pyrUp(resim))
cv2.imshow("meanfilterli resim", cv2.pyrUp(mean1))
cv2.imshow("mean2 resim", mean2)
cv2.waitKey(0)
cv2.destroyAllWindows()
