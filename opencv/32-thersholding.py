import cv2
resim = cv2.imread("elma.jpg", 0)
# resim,eşikdeğer,max değer,tür
# resim  eşik feğerden kucukse 0 yani siyah buyukse max atadığımız değer çıkar.
ret1, thres1 = cv2.threshold(resim, 150, 255, cv2.THRESH_BINARY)
# bınary tamtersi çıkar atadğımız değer kucukse max değer değilse 0
ret2, thres2 = cv2.threshold(resim, 100, 255, cv2.THRESH_BINARY_INV)
# resim efekt li çıkar bınar ayni
ret3, thres3 = cv2.threshold(resim, 100, 255, cv2.THRESH_TRUNC)
# resim bınary trunc karışımı cıkar
ret4, thres4 = cv2.threshold(resim, 100, 255, cv2.THRESH_TOZERO)
ret5, thres5 = cv2.threshold(
    resim, 100, 255, cv2.THRESH_TOZERO_INV)  # tozero tam tersi
print(ret1, ret2, ret3, ret4, ret5)
cv2.imshow("resim", resim)
cv2.imshow("thres1", thres1)
cv2.imshow("thres2", thres2)
cv2.imshow("thres3", thres3)
cv2.imshow("thres4", thres4)
cv2.imshow("thres5", thres5)
cv2.waitKey(0)
cv2.destroyAllWindows()
