import cv2
import numpy as np
beyaz = np.ones((400, 400))  # 1 lerden olusan matris
siyah = np.zeros((400, 400))  # 0 lardan olusan matris
cv2.imshow("beyaz", beyaz)
cv2.imshow("siyah", siyah)
cv2.waitKey(0)
cv2.destroyAllWindows()
