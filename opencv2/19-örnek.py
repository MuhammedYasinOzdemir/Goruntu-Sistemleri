import cv2
import numpy as np
resim = cv2.imread("ab.jpg")
xi, yi = -1, 1
img_output = np.zeros(resim.shape, np.uint8)


def draw(event, x, y, flags, param):
    global xi, yi
    if event == cv2.EVENT_LBUTTONDOWN:
        xi, yi = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        a, b = resim.shape[:2]
        src_points = np.float32([
            [xi, yi],
            [x, yi],
            [xi, y],
            [x, y]
        ])
        dst_points = np.float32([
            [0, 0],
            [b-1, 0],
            [0, a-1],
            [b-1, a-1]
        ])
        projected_points = cv2.getPerspectiveTransform(src_points, dst_points)
        img_output = cv2.warpPerspective(resim, projected_points, (b, a))
        cv2.imshow("output", img_output)


cv2.namedWindow("resim")
cv2.setMouseCallback("resim", draw)
while True:
    cv2.imshow("resim", resim)
    if cv2.waitKey(1) & 0xFF == 32:
        break
cv2.destroyAllWindows()
