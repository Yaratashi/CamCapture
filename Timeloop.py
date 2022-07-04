import time
import numpy as np
import cv2
from datetime import datetime


#Import/Open IPcamera (here default webcam)
cap = cv2.VideoCapture(0) 
c_image=0
timer= 0 


while (True):    
    #extraction of frame from Camera
    done, frame = cap.read()

    #display the IPcamera (Webcam)
    cv2.imshow('live video', frame) 

    #display time on the frame
    font = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(frame, str(datetime.now()), (20, 40), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
    
    #Pressing 'q' to quit 
    if cv2.waitKey(1) ==ord ('q'):
        break
    

    #Setting timer knowing by delaying the process
    for sec in range(5,0,-1): 
        print (sec) 
        time.sleep(1)

    #start_time= time.time()
    #time.sleep(5)
    #run_time=time.time()-start_time

    #testrun to make sure the delay period is exact
    #print(int(run_time))


    # Save the images in given path
    cv2.imwrite('frame'+ str(c_image) + '.jpg', frame)
    c_image +=1
    timer = 0
    #run_time=time.time()-start_time

    
cap.release()
cv2.destroyAllWindows()