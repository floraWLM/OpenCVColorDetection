import cv2

# zero is for the first webcam， 1 is the second
# for macbook use 1 as the front webcam
cap = cv2.VideoCapture(1)
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
    # hue value
    hue_value = pixel_center[0]
    # saturation value
    sat_value = pixel_center[1]
    # value value
    val_value = pixel_center[2]
    
    color = "Undefined"
    if sat_value < 51 and val_value < 51:
        color = "BLACK"
    elif sat_value < 20 and val_value > 230:
        color = "WHITE"
    elif hue_value < 5:
        color = "RED"
    elif hue_value < 22:
        color = "ORANGE"
    elif hue_value < 33:
        color = "YELLOW"
    elif hue_value < 78:
        color = "GREEN"
    elif hue_value < 131:
        color = "BLUE"
    elif hue_value < 170:
        color = "PURPLE"
    else:
        color = "RED"


    pixel_center_bgr = frame[cy,cx]
    b,g,r = int(pixel_center_bgr[0]),int(pixel_center_bgr[1]),int(pixel_center_bgr[2])
    print(pixel_center)
    cv2.putText(frame, color, (10,50), 0, 1, (b,g,r), 2)
    cv2.circle(frame, (cx,cy),5,(25,25,25),3)


    cv2.imshow("Frame",frame)
    # hold the frame until esc
    key = cv2.waitKey(1)
    # check if the user press esc
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()