import cv2
import math   

def is_right(d_x, p_x):
	if(p_x <  d_x):
		return 1
	return 0

def is_up(d_y, p_y):
	if(p_y < d_y):
		return 1
	return 0



def dist_and_direction(d_x, d_y, p_x, p_y):
	horizontal = -1
	vertical = -1
	return (math.sqrt( (d_x - p_x)**2 + (d_y - p_y)**2 ), is_right(d_x, p_x) ,is_up(d_y, p_y))
	#returning the distance, isright(0\1), isup(0\1)

     
def main:
	faceCascade = cv2.CascadeClassifier('C:\\haarcascade_frontalface_default.xml')

	video_capture = cv2.VideoCapture("C:\\test.mp4")
	p_x = 0
	p_y = 0
	d_x = 7
	d_y = 7


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
		if (len(faces) >= 1):
			face = faces[0]
			for (x, y, w, h) in faces:
				if(w*h > face[2] * face[3]):
				   face = (x, y, w, h)
			
		    # Draw a dot in the middle of the face
			p_x = d_x
			p_y = d_y
			d_x = (face[0]+face[2])/2 	
			d_y = (face[1]+face[3])/2
			cv2.circle(frame, (int(d_x) + 300 , int(d_y) ), 10, (0, 255, 0), -1)#unknown why there is a 300px offset
			print("distance is: " + str(dist_and_direction(d_x, d_y, p_x, p_y)) )
		    # Display the resulting frame
		cv2.imshow('Video', frame)
		

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# When everything is done, release the capture
	video_capture.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()
