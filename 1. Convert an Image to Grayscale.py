import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
print(kernel)
path =r"C:\Users\palas\OneDrive\Pictures\Screenshots\Screenshot 2024-02-21 090822.png"
img =cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale",imgGray)
cv2.waitKey(0)
