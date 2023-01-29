import cv2
resim = cv2.imread("elma.jpg", 0)
# simple thresholding
ret, thres1 = cv2.threshold(resim, 120, 255, cv2.THRESH_BINARY)
# adaptive thres
thres2 = cv2.adaptiveThreshold(resim, 120, cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY, 3, 3)  # ortalamayı alarak yapar
thres3 = cv2.adaptiveThreshold(
    resim, 120, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, 3, 3)
cv2.imshow("resim", resim)
cv2.imshow("thres1", thres1)
cv2.imshow("thres2", thres2)
cv2.imshow("thres3", thres3)
cv2.waitKey(0)
cv2.destroyAllWindows()
