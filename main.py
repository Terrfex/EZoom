import cv2
     

def dist(d_x, d_y)
{
	return 0
}
     
     
faceCascade = cv2.CascadeClassifier('C:\\Users\\User\\Desktop\\facedetect\\haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
	ret, frame = video_capture.read()

	gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(
		gray_img,
		scaleFactor=1.1,
		minNeighbors=6,
		minSize=(31, 31),
		flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a dot in the middle of the face
	lst = []
	for (x, y, w, h) in faces:
		#detect the right dot of the face while ignoring the others
		lst.append(w*h)
	max(lst)
	#### maybe try to do it with ictionry likr 30:x,y,w,h
		
			
		
	d_x = (x+w)/2
	d_y = (y+h)/2
	cv2.circle(frame, d_x , d_y ), 4, (0, 255, 0), -1)

    # Display the resulting frame
	cv2.imshow('Video', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
