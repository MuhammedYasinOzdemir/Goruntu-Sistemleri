import cv2
kamera = cv2.VideoCapture(0)
print(kamera.get(cv2.CAP_PROP_FRAME_WIDTH))  # genislik
print(kamera.get(cv2.CAP_PROP_FRAME_HEIGHT))  # yükseklik
print(kamera.get(cv2.CAP_PROP_FPS))  # fps gösterir
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 100)  # genisliği değistirir
while True:
    ret, frame = kamera.read()
    if not ret:  # kamera konrol edilir
        print("kamera acılamadı")
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # resme efekt uygular
    cv2.imshow("goruntu", frame)  # goruntu okunur
    if cv2.waitKey(1) & 0xFF == 27:  # 27 esc tusuna basılırsa cıkılır
        break
kamera.release()
cv2.destroyAllWindows()
