import cv2
url = "192.168.1.119:8080"
video = cv2.VideoCapture(url)
while video.isOpened():
    ret, frame = video.read()
    cv2.imshow("video", frame)
    if waitKey(1) & 0xFF == 32:
        break
video.release()
cv2.destroyAllWindows()
