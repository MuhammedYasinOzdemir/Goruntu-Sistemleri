import cv2
import numpy as np
cam = cv2.VideoCapture("car5.mp4")
sapma = 80
kernel = np.ones((5, 5), np.uint8)


def crop_matris(img):
    x, y = img.shape[:2]
    value = np.array([
        [(sapma, x-sapma),  # sol alt kose
         (int((y*3.1)/8), int(x*0.6)),  # sol ust kose
         (int((y*5.1)/8), int(x*0.6)),  # sag ust kose
         (y, x-sapma)]], np.int32)  # sag alt kose
    return value


def crop_image(img, matris):
    x, y = img.shape[:2]
    mask = np.zeros(shape=(x, y), dtype=np.uint8)
    mask = cv2.fillPoly(mask, matris, 255)
    mask = cv2.bitwise_and(img, img, mask=mask)
    return mask


def filt(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mask = cv2.inRange(img, 150, 255)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
    mask = cv2.GaussianBlur(mask, (9, 9), 0)
    mask = cv2.Canny(mask, 40, 180)
    return mask


def lines_mean(img):
    right = []
    left = []
    for line in lines:
        for x1, y1, x2, y2 in line:
            m = (y2-y1)/(x2-x1)
            if m < -0.4:
                right.append((x1, y1, x2, y2))
            elif m > 0.4:
                left.append((x1, y1, x2, y2))
    right_mean = np.mean(right, axis=0)
    left_mean = np.mean(left, axis=0)
    if not isinstance(right_mean, type(np.nan)):
        if not isinstance(left_mean, type(np.nan)):
            return right_mean, left_mean
        else:
            return right_mean, None
    else:
        if not isinstance(left_mean, type(np.nan)):
            return None, left_mean
        else:
            return None, None


def draw_line(img, line):
    line = np.int32(np.around(line))
    x1, y1, x2, y2 = line
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 200), 8)
    return img


while cam.isOpened():
    _, frame = cam.read()

    matris = crop_matris(frame)
    img = crop_image(frame, matris)
    img = filt(img)
    lines = cv2.HoughLinesP(img, 1, np.pi/180, 70,
                            minLineLength=10, maxLineGap=50)
    if lines is not None:
        right_line, left_line = lines_mean(lines)
        if right_line is not None:
            frame = draw_line(frame, right_line)
        if left_line is not None:
            frame = draw_line(frame, left_line)
    cv2.imshow("video", frame)
    cv2.imshow("img", img)
    if cv2.waitKey(16) == 32:
        break
cam.release()
cv2.destroyAllWindows()
