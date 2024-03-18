import cv2

# zero is for the first webcam， 1 is the second
# for macbook use 0 as the front webcam
cap = cv2.VideoCapture(0)
# set the pixel size of the cam
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# the while loop enable us to take multiple images
# which enable us to form a video
while cap.isOpened:
    # the underscore capture the boolean value of whether the frame is read
    # frame is numpy array normally in BGR format
    _,frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # getting the center of the frame
    height, weight, _ = frame.shape
    cx = int(weight / 2)
    cy = int(height / 2)

    # pick pixel value for the center
    pixel_center = hsv_frame[cy,cx]
    print(pixel_center)
    cv2.circle(frame, (cx,cy),5,(255,0,0),3)


    cv2.imshow("Frame",frame)
    # hold the frame until esc
    key = cv2.waitKey(1)
    # check if the user press esc
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()