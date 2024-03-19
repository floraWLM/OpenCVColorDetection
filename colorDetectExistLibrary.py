import cv2
import webcolors
from colorutils import Color
from colorutils import hex_to_web

# def rgb_to_color_name(rgb_tuple):
#     try:
#         # Get the closest color name based on RGB values
#         print(rgb_tuple)
#         print(1)
#         color_name = webcolors.rgb_to_name(rgb_tuple)
#         print(2)
#         print(color_name)
#         return color_name
#     except ValueError:
#         return "Unknown color"

def rgb_to_hex(r, g, b):
    # Ensure RGB values are within the valid range (0-255)
    r = max(0, min(r, 255))
    g = max(0, min(g, 255))
    b = max(0, min(b, 255))
    
    # Convert RGB to hexadecimal color code
    hex_code = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return hex_code

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
    pixel_center_bgr = frame[cy,cx]

    # h,s,v = int(pixel_center[0]),int(pixel_center[1]),int(pixel_center[2])
    b,g,r = int(pixel_center_bgr[0]),int(pixel_center_bgr[1]),int(pixel_center_bgr[2])
    # print("hhha",c.hex,c.shorthex,c.web)
    hex = rgb_to_hex(r, g, b)
    print(hex)
    co = hex_to_web(hex)
    print("hhhh",co)
    # color = "Unknown color"
    # try:
    #     color = webcolors.hex_to_name(hex)
    # except ValueError:
    #     pass

    # color = rgb_to_color_name(pixel_center)
    print(pixel_center)
    cv2.putText(frame, co, (10,50), 0, 1, (b,g,r), 2)
    cv2.circle(frame, (cx,cy),5,(25,25,25),3)

    cv2.imshow("Frame",frame)
    # hold the frame until esc
    key = cv2.waitKey(1)
    # check if the user press esc
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()