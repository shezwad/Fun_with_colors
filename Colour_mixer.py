'''This is a basic code for observing how R G B values impact colors.'''  

import cv2
import numpy as np

def ss(x):
    pass

img = np.zeros((400,400,3),np.uint8)
cv2.namedWindow('Color_Mixer')
cv2.createTrackbar('R','Color_Mixer',0,255,ss)
cv2.createTrackbar('G','Color_Mixer',0,255,ss)
cv2.createTrackbar('B','Color_Mixer',0,255,ss)

while(True):
    cv2.imshow('Color_Mixer',img)

    k = cv2.waitKey(1) &  0xFF
    if k == 27:
        break

    r = cv2.getTrackbarPos('R','Color_Mixer')
    g = cv2.getTrackbarPos('G','Color_Mixer')
    b = cv2.getTrackbarPos('B','Color_Mixer')

    img[:] = [b,g,r]

cv2.destroyAllWindows()