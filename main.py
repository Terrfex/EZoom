import cv2

faceCascade = cv2.CascadeClassifier(haarcascade_frontalface_default.xml)

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1, #some faces may be closer to the camera, they would appear bigger than the faces in the back. The scale factor compensates for this
        minNeighbors=5, ##defines how many objects are detected near the current one before it declares the face found.
        minSize=(30, 30), # gives the size of each window of the above param
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    # commonly used values for these fields. should different values for the window size, scale factor and find the best settings

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
