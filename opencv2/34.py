import cv2
import numpy as np
img = cv2.imread("ss.png")
img = cv2.pyrDown(img)
img_copy = img.copy()
gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 120)
# kenarli resim,piksel degeri,aci,threshold
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
# kenarli resim,piksel,aci,threshold,min birlesmeyleyle cizgi kabbul etme,max bosluk
lines2 = cv2.HoughLinesP(edges, 1, np.pi/180, 120, 100, 5, 5)
if not isinstance(lines, type(None)):
    for line in lines:
        for rho, theta in line:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = rho*a
            y0 = rho*b
            x1 = int(x0+1000*(-b))
            y1 = int(y0+1000*(a))
            x2 = int(x0-1000*(-b))
            y2 = int(y0-1000*(a))
            cv2.line(img_copy, (x1, y1), (x2, y2), (0, 200, 255), 2)
if not isinstance(lines2, type(None)):
    for line in lines2:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), (100, 0, 255), 2)
cv2.imshow("resim 1", img)
cv2.imshow("resim 2", img_copy)
cv2.imshow("Canny", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
