from ast import While
from tkinter import W
import cv2
import numpy as np
cizim = 0
xi, yi = -1, -1


def draw(event, x, y, flags, param):
    global cizim, xi, yi
    if event == cv2.EVENT_LBUTTONDOWN:  # butona basılması
        xi, yi = x, y
        cizim = 1
    elif event == cv2.EVENT_RBUTTONDOWN:
        xi, yi = x, y
        cizim = 2
    elif event == cv2.EVENT_MOUSEMOVE:  # mouse hareketi
        if cizim == 1:
            cv2.line(paint, (xi, yi), (x, y), (120, 120, 40), 1)
        elif cizim == 2:
            cv2.rectangle(paint, (xi, yi), (x, y), (120, 40, 200), 1)
    elif event == cv2.EVENT_RBUTTONUP:
        cizim = 0
    elif event == cv2.EVENT_LBUTTONUP:  # butondan elin kalkması
        cizim = 0


paint = np.ones((800, 600, 3), np.uint8)
cv2.namedWindow("paint")
cv2.setMouseCallback("paint", draw)  # isim pencere,fonksiyon
while True:
    cv2.imshow("paint", paint)
    if cv2.waitKey(1) & 0xFF == 32:
        break
cv2.waitKey(0)
cv2.destroyAllWindows()
