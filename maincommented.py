import cv2
import serial
#import libraries of face recognition and usb communication

def main():
    port = serial.Serial('COM7',9600)
    #port to talk to arduino
    faceCaascade = cv2.CascadeClassifier('haarcascade_frontalfce_default.xml')
    #the face recognition file
    video_capture = cv2.VideoCapture(0)
    #tells to the code what is the camera
    x = 0
    y = 0
    xArg = 90
    yArg = 90

    
    while True:
    #start of the loop
    
        ret, frame = video_capture.read()
        # Capture a frame

        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #convert image to black and white


        faces = faceCascade.detectMultiScale(
            gray_img,
            scaleFactor=1.1,
            minNeighbors=6,
            minSize=(31, 31),
            flags=cv2.CASCADE_SCALE_IMAGE
        )#find all the faces in the current frame
        
        
        
        if len(faces) >= 1:
            face = faces[0]
            for (x, y, w, h) in faces:
                if w * h > face[2] * face[3]:
                    face = (x, y, w, h)
        # choosing the biggest face available

            

            x = (face[0] + face[2]/2)
            y = (face[1] + face[3]/2)
            #find the ,iddle of the face
            
            
            cv2.circle(frame, (int(x), int(y)), 9, (0, 0, 255), -1)
            # Draw a dot in the middle of the face
            
            
        xArg = int(x / 4.923)
        yArg = int(y / 3.69)
        #screen size is 640X480 so scaling constant for x axis is 640/130 ->4.923, scaling constant for y axis is 480/130 -> 3.69
        #scaling constant may change because the camera does not capture 180 degrees

        yArg = 180 - yArg
        #values are coming inverted(when i move up the pointer moves down) so i need to invert the values(180 -> 0, 45 -> 135 etc..)

        if yArg < 70:
            yArg = 70
        #70 is the minimun value for the y angle because it may break    
            
        fnlstr = "X"+str(xArg+20)+"Y"+str(yArg)
        #build the information to send
        
        port.write(fnlstr.encode())
        #write the information for the arduino
        

        cv2.imshow('Video', frame)
        # Display the resulting picture
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        #if you press Q the program stops

    video_capture.release()
    #stop using the camera
    cv2.destroyAllWindows()
    #close the window of the picture
    
main()