import cv2
video = cv2.VideoCapture("slow.mp4")
while video.isOpened():  # kamereyı kontrol eder
    ret, frame = video.read()
    if not ret:
        print("video bitti.")
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow("goruntu", cv2.WINDOW_GUI_NORMAL)
    cv2.imshow("goruntu", frame)
    if cv2.waitKey(1) & 0xFF == 32:
        break
video.release()
cv2.destroyAllWindows()
