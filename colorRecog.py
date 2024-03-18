import cv2

img = cv2.imread("orange_fruit.jpg")

print(img)

cv2.imshow("Img", img)
# cv2.waitKey(0)