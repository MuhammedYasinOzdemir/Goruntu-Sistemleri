import cv2
video = cv2.VideoCapture(0)
# formatı belirliyoruz mp4 için MP4V avi için XVID
fourcc = cv2.VideoWriter_fourcc(*"XVID")
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
widtht = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))  # kameraya gore yapıyoruz
out = cv2.VideoWriter("kayit1.avi", fourcc, 30.0,
                      (widtht, height))  # isim,format,fps,boyut avi veya mp4 kaydedilebilir
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        print("video kayıt edilemedi")
    cv2.namedWindow("kayıt videosu", cv2.WINDOW_GUI_NORMAL)
    cv2.imshow("kayıt videosu", frame)
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == 32:
        break
video.release()
out.release()
cv2.destroyAllWindows()
