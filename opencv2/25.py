import cv2
resim = cv2.imread("aa.jpg", 0)
blur = cv2.GaussianBlur(resim, (3, 3), 0)
resim = cv2.resize(resim, None, fx=0.2, fy=0.2)
ret, thres1 = cv2.threshold(resim, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
_, thres2 = cv2.threshold(resim, 0, 255, cv2.THRESH_TOZERO+cv2.THRESH_OTSU)
# resim,max deger,adaptive turu ,thres turu,matris,cıkaralıcak deger
thres3 = cv2.adaptiveThreshold(
    resim, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 0)
thres4 = cv2.adaptiveThreshold(
    resim, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 0)
cv2.imshow("thres binary", thres1)
cv2.imshow("thres otsu", thres2)
cv2.imshow("thres mean", cv2.pyrUp(thres3))
cv2.imshow("thres gaussian", thres4)
cv2.imshow("resim", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
