import cv2
     

def dist_and_direction(d_x, d_y, p_x, p_y):
	horizontal = -1
	vertical = -1
	return (sqrt( (d_x - p_x)**2 + (d_y - p_y)**2 ), , )
	#returning the distance, left(0)\right(1), up(0)/down(1)

     
     
faceCascade = cv2.CascadeClassifier('C:\\Users\\User\\Desktop\\facedetect\\haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)
p_x = 0
p_y = 0
d_x = 0
d_y = 0


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
	#choosing the biggest face available
	face = faces[0]
	for (x, y, w, h) in faces:
		if(w*h > face[2] * face[3]):
		   face = (x, y, w, h)
	
		
			
	
    # Draw a dot in the middle of the face
	p_x = d_x
	p_y = d_y
	d_x = (face[0]+face[2])/2 	
	d_y = (face[1]+face[3])/2
	cv2.circle(frame, (d_x , d_y ), 4, (0, 255, 0), -1)

    # Display the resulting frame
	cv2.imshow('Video', frame)
	print("distance is: " + dist(d_x, d_y, p_x, p_y) )

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
