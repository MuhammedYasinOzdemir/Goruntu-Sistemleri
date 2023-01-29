import cv2
import numpy as np
camera = cv2.VideoCapture(0)


def nothing(x):
    pass


cv2.namedWindow("frame", cv2.WINDOW_GUI_NORMAL)
cv2.createTrackbar("H1", "frame", 0, 360, nothing)  # renk özu min
cv2.createTrackbar("H2", "frame", 0, 360, nothing)  # renk özü max
cv2.createTrackbar("S1", "frame", 0, 255, nothing)  # doygunluk min
cv2.createTrackbar("S2", "frame", 0, 255, nothing)  # doygunluk max
cv2.createTrackbar("V1", "frame", 0, 255, nothing)  # parlaklık min
cv2.createTrackbar("V2", "frame", 0, 255, nothing)  # parlaklık max
while camera.isOpened():
    _, frame = camera.read()
    img = frame.copy()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    H1 = int(cv2.getTrackbarPos("H1", "frame")/2)
    H2 = int(cv2.getTrackbarPos("H2", "frame")/2)
    S1 = cv2.getTrackbarPos("S1", "frame")
    S2 = cv2.getTrackbarPos("S2", "frame")
    V1 = cv2.getTrackbarPos("V1", "frame")
    V2 = cv2.getTrackbarPos("V2", "frame")
    lower = np.array([H1, S1, V1])
    upper = np.array([H2, S2, V2])
    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    contours, hiararchy = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i, cnt in enumerate(contours):
        area = cv2.contourArea(cnt)
        if area > 50000 or area < 200:
            continue
        x, y, w, h = cv2.boundingRect(cnt)
        print(x, y, w, h)
        color = (100, 150, 200)
        try:
            elipse = cv2.fitEllipse(cnt)
            cv2.ellipse(img, elipse, color, 3)
        except cv2.error as e:
            print("eror:", e)

    cv2.imshow("frame", frame)
    cv2.imshow("hsv", hsv)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    cv2.imshow("img", img)
    if cv2.waitKey(1) & 0xFF == 32:
        break
camera.release()
cv2.destroyAllWindows()
