import cv2

# Initialize the webcam and set it to capture at 60 fps
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Check if the webcam is opened correctly
if not cam.isOpened():
    print("Error: Could not open webcam.")
    exit()

frame_count = 0

while True:
    # Read a frame from the webcam
    ret, frame = cam.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    # Process every other frame to display at 30 fps
    if frame_count % 1 == 0:
        # Resize the frame to (320, 240)
        rcf = cv2.resize(frame, (320, 240))

        # Convert the resized frame to different color spaces
        rgf = cv2.cvtColor(rcf, cv2.COLOR_BGR2GRAY)
        rlf = cv2.cvtColor(rcf, cv2.COLOR_BGR2Lab)
        hls = cv2.cvtColor(rcf, cv2.COLOR_BGR2Luv)

        # Display the frames in different windows
        cv2.imshow('Gray', rgf)
        cv2.moveWindow('Gray', 0, 0)
        
        cv2.imshow('BGR', rcf)
        cv2.moveWindow('BGR', 320, 0)
        
        cv2.imshow('Lab', rlf)
        cv2.moveWindow('Lab', 0, 240)
        
        cv2.imshow('Luv', hls)
        cv2.moveWindow('Luv', 320, 240)

        # Introduce a delay to maintain 30 fps playback
        if cv2.waitKey(33) & 0xFF == ord('q'):
            break
    
    frame_count += 1

# Release the webcam and close all windows
cam.release()
cv2.destroyAllWindows()
