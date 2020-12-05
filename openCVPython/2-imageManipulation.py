import cv2
import numpy as np
print("Import: Successful")

#20200817_055840.jpg
#VID-20200412-WA0000.mp4

kernel = np.ones((5,5), np.uint8)

#Image
img = cv2.imread("IMG-20200817_055840.jpg")

scale_percentage = 20
height	= int(img.shape[0] * scale_percentage/100)
width	= int(img.shape[1] * scale_percentage/100)
dim = (width, height)
imgResize = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

imgGray = cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)

imgBlur = cv2.GaussianBlur(imgGray, (3,3), 0)

imgCanny = cv2.Canny(imgBlur, 50, 100)

imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

while True:
	cv2.imshow("Image", imgCanny)
	if cv2.waitKey(1) & 0xFF ==ord('q'):
		break


