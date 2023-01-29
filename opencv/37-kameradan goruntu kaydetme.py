import cv2
kamera = cv2.VideoCapture(0)
widtht = int(kamera.get(cv2.CAP_PROP_FRAME_WIDTH))  # yuksekliği alır
height = int(kamera.get(cv2.CAP_PROP_FRAME_HEIGHT))  # genişiği alır kameranın
print(widtht, height)
fourcc = cv2.VideoWriter_fourcc(*'MP4V')  # formatını belirliyoruz
# isim,format,kac ms ye(hızı belirtir),(genişlik ,yukseklik)
writer = cv2.VideoWriter(
    "C:\\Users\\User\\Desktop\\pyhton\\opencv\\kayit.mp4", fourcc, 50, (widtht, height))
while True:
    ret, goruntu = kamera.read()
    writer.write(goruntu)
    cv2.imshow("goruntu", goruntu)
    if cv2.waitKey(50) & 0xFF == 32:
        break
kamera.release()
writer.release()
cv2.destroyAllWindows()
