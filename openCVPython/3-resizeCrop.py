import cv2
import numpy as np
print("Import: Successful")

#20200817_055840.jpg
#VID-20200412-WA0000.mp4

kernel = np.ones((5,5), np.uint8)

#Image
img = cv2.imread("IMG-20200817_055840.jpg")
print(img.shape)

scale_percentage = 20
height = int(img.shape[0] * scale_percentage/100)
width = int(img.shape[1] * scale_percentage/100)
dim = (width, height)
imgResize = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

#imgCropped = img[0:200, 200:500]		#height then width

while True:
	cv2.imshow("Image", imgResize)
	if cv2.waitKey(1) & 0xFF ==ord('q'):
		break

