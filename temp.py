import cv2

# Create a VideoCapture object
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Set the desired FPS
#fps = 120
#cam.set(cv2.CAP_PROP_FPS, fps)

# Verify the FPS setting
actual_fps = cam.get(cv2.CAP_PROP_FPS)
print(f"FPS set to: {actual_fps}")

while True:
    _, frame = cam.read()
    

    # Display the frame
    cv2.imshow('Webcam', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cam.release()
cv2.destroyAllWindows()