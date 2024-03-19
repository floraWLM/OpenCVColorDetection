import cv2
import math 

# zero is for the first webcam， 1 is the second
# for macbook use 1 as the front webcam
cap = cv2.VideoCapture(1)
# set the pixel size of the cam
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# variables storing the bgr value for colors
red = (0, 0, 255)
orange = (0,128,255)
yellow = (0,255,255)
green = (0,255,0)
blue = (255,0,0)
purple = (255,0,127)
pink = (204,153,255)
white = (255,255,255)
black = (0,0,0)
gray = (128,128,128)
brown = (0,76,153)
colorAll = (red,orange,yellow,green,blue,purple,pink,white,black,gray,brown)
colorName = ("RED","ORANGE","YELLOW","GREEN","BLUE","PURPLE","PINK","WHITE","BLACK","GRAY","BROWN")

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
    pixel_center_bgr = frame[cy,cx]
    b,g,r = int(pixel_center_bgr[0]),int(pixel_center_bgr[1]),int(pixel_center_bgr[2])

    dMin = 500
    storedValue = (255,255,255)
    color = "Undefined"
    i = 0
    # search for the closest color stored
    for c in colorAll:
        d = math.sqrt(pow(c[0]-b,2)+pow(c[1]-g,2)+pow(c[2]-r,2))
        if d < dMin:
            dMin = d
            color = colorName[i]
            storedValue = c
        elif d == dMin:
            sizedMin = math.sqrt(pow(storedValue[0],2)+pow(storedValue[1],2)+pow(storedValue[2],2))
            sized = math.sqrt(pow(b,2)+pow(g,2)+pow(r,2))
            if sized < sizedMin:
                color = colorName[i]
                storedValue = c
        i = i + 1
    print(color)
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
