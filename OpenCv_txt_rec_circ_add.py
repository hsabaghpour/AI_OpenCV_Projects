import cv2
#print(cv2.__version__)
import time

# Get the current local time as a struct_time object

# Extract the seconds
#seconds = current_time.tm_sec
#minutes = current_time.tm_min

#print("Current seconds:", seconds)

cam = cv2.VideoCapture(0)
#cam.set(cv2.CAP_PROP_FPS, 15)

# Set the desired FPS
#fps_set = 10
#cam.set(cv2.CAP_PROP_FPS, fps_set)

# Verify the FPS setting
actual_fps = cam.get(cv2.CAP_PROP_FPS)
print(f"FPS set to: {actual_fps}")

Frame_Count = 0
Total_Frames = 0#second_1 = 1
current_time = time.localtime()
second_ref = current_time.tm_sec
fps = 0
MIN = current_time.tm_min
HOUR = current_time.tm_hour

while True:
    SEC = current_time.tm_sec
    MIN = current_time.tm_min
    HOUR = current_time.tm_hour
    

    _, frame = cam.read()
    
    rcf = cv2.resize(frame, (320, 240))
    #rcf[180:220,200:400] = [0,100,150]
    #cv2.rectangle(rcf, (int(5*Frame_Count), int(200/(Frame_Count+1))), (40+Frame_Count, 80-Frame_Count), (120+Frame_Count,100-Frame_Count,3*Frame_Count), -1) 
    #cv2.circle(rcf, (159-Frame_Count, 119+Frame_Count), SEC, (255,8*Frame_Count,6*Frame_Count), 3)

    #second_1 = current_time.tm_sec

    #cv2.putText(rcf, str(second), (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 4)
    cv2.putText(rcf, "Total Frames : " + str(Total_Frames), (5, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.putText(rcf, "Time: " + str(HOUR) + ":" + str(MIN) + ":" + str(SEC), (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(rcf, "fps : " + str(fps), (5, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    #grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('MAC WebCam',   rcf )
    cv2.moveWindow('MAC WebCam', 0, 0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    Frame_Count += 1
    Total_Frames += 1
    #second_2 = current_time.tm_sec
    current_time = time.localtime()

    if current_time.tm_sec != second_ref:
        #print("Frames per second: ", Frame_Count)
        #cv2.putText(rcf, str(Frame_Count), (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)
        fps = Frame_Count
        Frame_Count = 0
        second_ref = current_time.tm_sec
    #cv2.putText(rcf, str(fps), (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 4)


cam.release()