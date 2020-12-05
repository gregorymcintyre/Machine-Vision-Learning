import cv2
print("Import: Successful")
print("enable webcam with Devices>webcams>USB2.0*")

#20200817_055840.jpg
#VID-20200412-WA0000.mp4

#Image
img = cv2.imread("IMG-20200817_055840.jpg")

while True:
	cv2.imshow("Image", img)
	if cv2.waitKey(1) & 0xFF ==ord('q'):
		break

#Video
video = cv2.VideoCapture("VID-20200412-WA0000.mp4")

while True:
	success, img = video.read()
	cv2.imshow("Video", img)
	if cv2.waitKey(1) & 0xFF ==ord('q'):
		break
		
#webcam
webcam = cv2.VideoCapture(0)
webcam.set(3, 640)	#width
webcam.set(4, 480)	#height
#webcam.set(10, 100)	#brightness

while True:
	success, img = webcam.read()
	cv2.imshow("Video", img)
	if cv2.waitKey(1) & 0xFF ==ord('q'):
		break
