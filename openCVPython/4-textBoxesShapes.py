import cv2
import numpy as np
print("Import: Successful")

#IMG-20200817_055840.jpg
#VID-20200412-WA0000.mp4

#Image
img = cv2.imread("IMG-20200817_055840.jpg")
#print(img.shape)

scale_percentage = 20
height = int(img.shape[0] * scale_percentage/100)
width = int(img.shape[1] * scale_percentage/100)
dim = (width, height)
imgResize = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

#while True:
#	cv2.imshow("Image", imgResize)
#	if cv2.waitKey(1) & 0xFF ==ord('z'):
#		break

overlay = np.zeros((imgResize.shape[0], imgResize.shape[1], 3), np.uint8)

#overlay[:]=255,0,0	#Blue

cv2.line(overlay, (0,0), (imgResize.shape[1], imgResize.shape[0]), (0, 255, 0), 3)
cv2.rectangle(overlay, (0,0), (100, 100), (255, 0, 0), 3)
cv2.circle(overlay, (100,100), 10, (0, 0, 255), 3)
cv2.putText(overlay, "test", (200, 200), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 0), 1)

while True:
	cv2.imshow("Image", overlay)
	if cv2.waitKey(1) & 0xFF ==ord('z'):
		break

