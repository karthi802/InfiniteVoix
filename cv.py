import time
import pyautogui
import datetime
from ecapture import ecapture as ec
import cv2
import subprocess

x = datetime.datetime.now()
sub = x.strftime("%f")
name = "screenshot_"+ sub+".png"

def takeSS():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'D:/Pictures/'+name)

def takePicture(wait):
    pic_name = "img_"+sub+".jpg"
    # ec.capture(0,"robo camera",pic_name)

    if wait == 0:


    #Define a video capture object
        vid = cv2.VideoCapture(0)
        capture = False

        while True:
            # Capture the video frame by frame
            ret, frame = vid.read()

            # Display the resulting frame
            cv2.imshow('frame', frame)

            # Wait for a key event indefinitely
            key = cv2.waitKey(1)

            # Check if the key is the spacebar (32 is the ASCII code for space)
            if key == 32:  # 32 is the ASCII code for space
                capture = True
            elif key & 0xFF == ord('q'):
                break

            # If capture is True, save the frame as an image
            if capture:
                cv2.imwrite(f'D:/Pictures/{pic_name}', frame)
                print("Image captured!")
                capture = False

        # After the loop release the capture object
        vid.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
    else:       

        # Open the default camera (usually camera index 0)
        cap = cv2.VideoCapture(0)

        # Display the video for 5 seconds
        start_time = time.time()
        while (time.time() - start_time) < wait:
            ret, frame = cap.read()
            cv2.imshow('Video Feed', frame)
            cv2.waitKey(1)

        # Capture a frame at the 5th second
        ret, frame_at_5th_second = cap.read()
        if ret:
            cv2.imwrite(f'D:/Pictures/{pic_name}', frame_at_5th_second)
            
        else:
            print("Failed to capture a frame.")

        # Release the camera
        cap.release()
        cv2.destroyAllWindows()



