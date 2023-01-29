import cv2
import numpy as np
cam = cv2.VideoCapture(0)
lower = np.array([160, 155, 85])
upper = np.array([180, 255, 255])
while cam.isOpened():
    _, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    c, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i, cnt in enumerate(c):
        area = cv2.contourArea(cnt)
        if area > 50000 or area < 200:
            continue
        perimeter = cv2.arcLength(cnt, True)
        epsilon = 0.01*perimeter
        apporox = cv2.approxPolyDP(cnt, epsilon, True)
        cv2.drawContours(frame, [apporox], -1, (0, 0, 0), 10)
        cv2.drawContours(frame, c, i, (100, 200, 150), 3)
        (x, y), radius = cv2.minEnclosingCircle(cnt)
        center = (int(x), int(y))
        if len(apporox) > 12:
            cv2.putText(frame, "daire", center,
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 4, (120, 140, 200), 4)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == 32:
        break
cam.release()
cv2.destroyAllWindows()
