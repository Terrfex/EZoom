import cv2
import serial

def main():
    port = serial.Serial('COM7',9600)
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    video_capture = cv2.VideoCapture(0)
    x = 0
    y = 0
    xArg = 90
    yArg = 90

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
        # choosing the biggest face available
        if len(faces) >= 1:
            face = faces[0]
            for (x, y, w, h) in faces:
                if w * h > face[2] * face[3]:
                    face = (x, y, w, h)

            # Draw a dot in the middle of the face

            x = (face[0] + face[2]/2)
            y = (face[1] + face[3]/2)
            
            cv2.circle(frame, (int(x), int(y)), 9, (0, 0, 255), -1)
            #screen size is 640X480 so scaling constant for x axis is 640/180 ->3.55555, scaling constant for y axis is 480/180 -> 2.66667
            #scaling constant may change because the camera does not capture 180 degrees
            

            
        xArg = int(x / 4.923)
        yArg = int(y / 3.2)
        #values are coming inverted(when i move left the pointer moves right) so i need to invert the values(180 -> 0, 45 -> 135 etc..)
        yArg = 180 - yArg
        if yArg < 75:
            yArg = 75
        fnlstr = "X"+str(xArg+20)+"Y"+str(yArg)
        
        print("\nSent: " + fnlstr)
        port.write(fnlstr.encode())
        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
