import cv2
import time
import numpy as np

#print(cv2.__version__)
cam = cv2.VideoCapture(0)

Start = np.random.randint(1, 160)
Top = Start
Left = Start
Right = Left + 80
Butt = Top + 50
Step = 5
H_Step = 1
V_Step = 1
Frame_Count = 0
while True:
    
    _, frame = cam.read()
    rcf = cv2.resize(frame, (320, 240))
    


    if Butt > 240 or Top == 0 :
        V_Step = V_Step * -1
        Top = Top + V_Step
        Butt = Butt + V_Step

             
    else:
        Top = Top + V_Step
        Butt = Butt + V_Step

    
    if Right > 320 or Left == 0:
        H_Step = H_Step * -1
        Right = Right + H_Step
        Left = Left + H_Step 
    else:
        Right = Right + H_Step
        Left = Left + H_Step 

            


        cv2.rectangle(rcf, (Left,Top), (Right,Butt), (255,255,255), 2) 
    
        
            #rcf[i, j] = [0, 0, 255]
    frameROI = rcf[Top:Butt, Left:Right]    
    frameROI_BACKUP = frameROI.copy()

    grayROI = cv2.cvtColor(frameROI, cv2.COLOR_BGR2GRAY)
    BGRROI  = cv2.cvtColor(grayROI, cv2.COLOR_BGR2RGB)
    rcf[Top:Butt, Left:Right] = BGRROI
    
    grayHW = cv2.cvtColor(rcf, cv2.COLOR_BGR2GRAY)
    Gray2BGRHW = cv2.cvtColor(grayHW, cv2.COLOR_GRAY2BGR)
    Gray2BGRHW[Top:Butt, Left:Right] = frameROI_BACKUP
    cv2.imshow('GrayHW', Gray2BGRHW)
    cv2.moveWindow('GrayHW', 0, 300)

    
    #cv2.imshow('ROI',  frameROI)
    cv2.imshow('BGR', rcf)   
    #cv2.moveWindow('ROI', 0, 0)
    cv2.moveWindow('BGR', 220, 0)
    #cv2.imshow('Gray', grayROI)
    #cv2.moveWindow('Gray', 0, 250)
    #cv2.imshow('RGB', BGRROI)
    #cv2.moveWindow('RGB', 220, 250)

    #time.sleep(0.01)
    Frame_Count += 1
     
    if cv2.waitKey(1) & 0xff == ord('q'):
                break
cam.release()