import cv2
#print(cv2.__version__)
import time
import numpy as np


cam = cv2.VideoCapture(0)
# Verify the FPS setting
actual_fps = cam.get(cv2.CAP_PROP_FPS)
print(f"FPS set to: {actual_fps}")

Frame_Count = 0
Total_Frames = 0#second_1 = 1
current_time = time.localtime()
#second_ref = current_time.tm_sec
#fps = 0
MIN = current_time.tm_min
HOUR = current_time.tm_hour
moment = time.time()
fpsFilt = 30

while True:
    time.sleep(np.random.uniform(0, 0.02))
    #print(np.random.uniform(0, 0.1))

    dT = time.time() - moment
    moment = time.time()
    #print("dT: ", dT)
    fps_calc = int(1/dT)
    #print("fps_calc: ", fps_calc)
    fpsFilt = int(.95*fpsFilt + .05*fps_calc)
    
    
    SEC = current_time.tm_sec
    MIN = current_time.tm_min
    HOUR = current_time.tm_hour
    

    _, frame = cam.read()
    
    rcf = cv2.resize(frame, (320, 240))
    cv2.putText(rcf, "Total Frames : " + str(Total_Frames), (5, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.putText(rcf, "Time: " + str(HOUR) + ":" + str(MIN) + ":" + str(SEC), (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(rcf, "fps : " + str(fps_calc), (5, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(rcf, "fpsFilt : " + str(fpsFilt), (5, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255),1)
    cv2.imshow('MAC WebCam',   rcf )
    cv2.moveWindow('MAC WebCam', 0, 0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    #Frame_Count += 1
    Total_Frames += 1
    #current_time = time.localtime()

    #if current_time.tm_sec != second_ref:
        #fps = Frame_Count
        #Frame_Count = 0
        #second_ref = current_time.tm_sec


cam.release()