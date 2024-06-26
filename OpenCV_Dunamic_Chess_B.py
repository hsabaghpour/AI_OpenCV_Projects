import cv2

import numpy as np

boardSize = input("Enter the size of the board: ")
boardSize = int(boardSize)

NUM_SQUARES = int(input("Enter the number of squares: "))
squareSize = int(boardSize / NUM_SQUARES)

darkColor = [0, 0, 0]
lightColor = [175, 175, 175]
nowColor = darkColor

while True:
    
    x = np.zeros((boardSize, boardSize,3), dtype=np.uint8)
    for row in range(0,NUM_SQUARES):
        for column in range(0,NUM_SQUARES):
            
            x[row*squareSize:row*squareSize+squareSize, column*squareSize:column*squareSize+squareSize] = nowColor
            if nowColor == darkColor:
                nowColor = lightColor
            else:
                nowColor = darkColor
        if nowColor == darkColor:
            nowColor = lightColor
        else:
            nowColor = darkColor    
    cv2.imshow('Chess_board', x)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    