import cv2
import numpy as np
resim = cv2.imread("logo.jpg")
a, b = resim.shape[:2]
src_points = np.float32([
    [0, 0],
    [b-1, 0],
    [0, a-1],
    [b-1, a-1]
])
dst_points = np.float32([
    [0, 0],
    [b-1, 0],
    [int((b-1)*0.33), a-1],
    [int((b-1)*0.66), a-1]
])
projected_points = cv2.getPerspectiveTransform(src_points, dst_points)
img_output = cv2.warpPerspective(resim, projected_points, (b, a))
cv2.imshow("aa", img_output)
cv2.waitKey(0)
cv2.destroyAllWindows()
