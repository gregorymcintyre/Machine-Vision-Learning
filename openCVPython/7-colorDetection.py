import cv2
import numpy as np
print("Import: Successful")

#IMG-20200817_055840.jpg
#IMG-20200915_165720.jpg
#VID-20200412-WA0000.mp4

def empty():
    pass

#slider Window
#TODO: Fix Blackbox
cv2.namedWindow("Sliders")
#cv2.resizeWindow("Sliders", 640, 240)
cv2.createTrackbar("Hue Min", "Sliders", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Sliders", 90, 179, empty)
cv2.createTrackbar("Saturation Min", "Sliders", 0, 255, empty)
cv2.createTrackbar("Saturation Max", "Sliders", 255, 255, empty)
cv2.createTrackbar("Volume Min", "Sliders", 0, 255, empty)
cv2.createTrackbar("Volume Max", "Sliders", 185, 255, empty)

#Image
img = cv2.imread("IMG-20200915_165720.jpg")
#print(img.shape)

scale_percentage = 20
height = int(img.shape[0] * scale_percentage/100)
width = int(img.shape[1] * scale_percentage/100)
dim = (width, height)
imgResize = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

imgHSV = cv2.cvtColor(imgResize, cv2.COLOR_BGR2HSV)

while True:
    h_min = cv2.getTrackbarPos("Hue Min", "Sliders")
    h_max = cv2.getTrackbarPos("Hue Max", "Sliders")
    s_min = cv2.getTrackbarPos("Saturation Min", "Sliders")
    s_max = cv2.getTrackbarPos("Saturation Max", "Sliders")
    v_min = cv2.getTrackbarPos("Volume Min", "Sliders")
    v_max = cv2.getTrackbarPos("Volume Max", "Sliders")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_max, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    imgMask = cv2.inRange(imgHSV, lower, upper)
    imgMasked = cv2.bitwise_and(imgResize, imgResize, mask=imgMask)

    cv2.imshow("Image", imgResize)
    #cv2.imshow("Modified", imgHSV)
    #cv2.imshow("Mask", imgMask)
    cv2.imshow("And", imgMasked)

    if cv2.waitKey(1) & 0xFF ==ord('z'):
        break