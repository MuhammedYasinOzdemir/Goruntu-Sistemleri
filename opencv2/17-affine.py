import cv2
import numpy as np
resim = cv2.imread("logo.jpg")
a, b = resim.shape[:2]
src_points = np.float32([
    [0, 0],
    [0, a-1],
    [b-1, 0]
])
dst_points = np.float32([
    [0, 0],  # x,y
    [0, int((a-1)*0.6)],
    [b-1, 50]
])
# secilen nokta matrisi,değiştirdiğimiz matris
affine_matrix = cv2.getAffineTransform(src_points, dst_points)
# resim,matris,resmin yeni boyutları
img_output = cv2.warpAffine(resim, affine_matrix, (b, a))
cv2.imshow("affine", img_output)
cv2.waitKey(0)
cv2.destroyAllWindows()
