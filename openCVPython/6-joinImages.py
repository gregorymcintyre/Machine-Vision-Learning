import cv2
import numpy as np
print("Import: Successful")

#TODO: Stack different channel images

#IMG-20200817_055840.jpg
#VID-20200412-WA0000.mp4

#Image
img = cv2.imread("IMG-20200817_055840.jpg")
print(img.shape)

scale_percentage = 20
height = int(img.shape[0] * scale_percentage/100)
width = int(img.shape[1] * scale_percentage/100)
dim = (width, height)
imgResize = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

imgHor = np.hstack((imgResize, imgResize))

while True:
	cv2.imshow("Image", imgHor)
	if cv2.waitKey(1) & 0xFF ==ord('z'):
		break

imgVert = np.vstack((imgResize, imgResize))

while True:
	cv2.imshow("Image", imgVert)
	if cv2.waitKey(1) & 0xFF ==ord('z'):
		break