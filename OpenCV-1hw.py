import cv2

cam = cv2.VideoCapture(0)


while True:
    _, frame = cam.read()
    rcf = cv2.resize(frame, (320, 240))

    rgf = cv2.cvtColor(rcf, cv2.COLOR_BGR2GRAY)
    rlf = cv2.cvtColor(rcf, cv2.COLOR_BGR2Lab)
    hls = cv2.cvtColor(rcf, cv2.COLOR_BGR2Luv)
    
    cv2.moveWindow('Gray', 0, 0)

    cv2.imshow('Gray', rgf )
    

    cv2.imshow('BGR', rcf )
    cv2.moveWindow('BGR', 320, 0)
    
    cv2.imshow('Lab', rlf )
    cv2.moveWindow('Lab', 0, 240)
    
    cv2.imshow('Luv', hls )
    cv2.moveWindow('Luv', 320, 240)
    
    delay = 1
    
    
    if cv2.waitKey(delay) & 0xff == ord('q'):
        break
cam.release()