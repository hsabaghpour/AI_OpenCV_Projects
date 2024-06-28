import cv2

print(cv2.__version__)

width = 640
height = 480
evt = 0
click_coordinates = (0, 0)
#x1, y1, x2, y2 = 0, 0, width,height
pnt1 = (0, 0)
pnt2 = (640, 480)
Click = False
Release = False
Kill = False

def mouseClick(event, x, y, flags, param):
    
 
    global pnt1
    global pnt2
    #global Click
    #global Release
    #global Kill
    global evt

    if event == cv2.EVENT_LBUTTONDOWN:
        evt = event
        pnt1 = (x, y)
        #Click = True



    if event == cv2.EVENT_LBUTTONUP:
        evt = event
        pnt2 = (x, y)
        #Release = True
        #Release = True
    if event == cv2.EVENT_RBUTTONUP:
        evt = event



# Using the default camera index 0
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

if not cam.isOpened():
    print("Error: Could not open camera.")
    exit()
cv2.namedWindow('my WEBcam')
cv2.setMouseCallback('my WEBcam', mouseClick)
while True:

    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break
    
    x1, y1 = pnt1
    x2, y2 = pnt2
    try:
        if evt == 4 :
            print('x1 =', x1, 'y1 =', y1, 'x2 =', x2, 'y2 =', y2)
            cv2.rectangle(frame, pnt1, pnt2, (0, 255, 0), 2)
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            print('x1 =', x1, 'y1 =', y1, 'x2 =', x2, 'y2 =', y2)
                
            frameROI = frame[y1:y2, x1:x2]
            copy_frameROI = frameROI.copy()
            grayROI = cv2.cvtColor(frameROI, cv2.COLOR_BGR2GRAY)
            C_GrayROI = cv2.cvtColor(grayROI, cv2.COLOR_GRAY2BGR)
            frame[y1:y2, x1:x2] = C_GrayROI    
            cv2.imshow('ROI', copy_frameROI)
            cv2.moveWindow('ROI', 0, 500)
            print(evt)
            
        if evt == 5:
                #Click = False
                #Release = False
                #Kill = False
            print('Kill')
            print(evt)
            cv2.destroyWindow('ROI')
            evt = 0
    except cv2.error as e:
        print(f"Please avoid Double Clicking on the frame!!!")
        # You can choose to skip this frame and continue, or handle it in another way
        #continue
            


  

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)
    


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
