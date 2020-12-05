import cv2
import numpy as np
print("Import: Successful")

#IMG-20200817_055840.jpg
#IMG-Cards.jpeg
#VID-20200412-WA0000.mp4

#TODO: Get a higher def image.

#75,79
#121,41
#183,110
#137,150

#Image
img = cv2.imread("IMG-Cards.jpeg")
print(img.shape)

width, height = 250, 350
points1 = np.float32([[75,79],[137,150],[121,41],[183,110]])
points2 = np.float32([[0,0],[0, height],[width,0],[width, height]])
matrix = cv2.getPerspectiveTransform(points1, points2)
imgTransform = cv2.warpPerspective(img, matrix, (width, height))

while True:
	cv2.imshow("Image", img)
	if cv2.waitKey(1) & 0xFF ==ord('z'):
		break

while True:
	cv2.imshow("Image", img)
	cv2.imshow("Image", imgTransform)
	if cv2.waitKey(1) & 0xFF ==ord('z'):
		break

