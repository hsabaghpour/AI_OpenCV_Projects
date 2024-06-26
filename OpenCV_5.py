import cv2
import numpy as np
while True:
    
    frame = np.zeros((800, 800,3), dtype=np.uint8)
    #frame[0:100, 0:100] = 255
    #frame[100:200, 100:200] = 255
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                frame[i*100:i*100+100, j*100:j*100+100] = [0,255/(i+1),255/(j+1)]
            else:
                frame[i*100:i*100+100, j*100:j*100+100] = [255/(j+i+1),255/(i+j+1),0q]
  
    
    cv2.imshow('Chess_board', frame)
    
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    