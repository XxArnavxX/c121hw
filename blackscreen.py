import cv2
import time
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'XVID')
outputfile = cv2.VideoWriter('output.avi', fourcc, 30.0, (640, 480))

cam = cv2.VideoCapture(0)

time.sleep(5)

for i in range(60):
    ret, bg = cam.read()

bg = np.flip(bg, axis = 1)

while(cam.isOpened()):
    ret, ing = cam.read()
    if not ret:
        break

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_black = np.array([0, 120, 50])
upper_black = np.array([10, 255, 255])
mask_1 = cv2.inRange(hsv, lower_black, upper_black)

lower_black = np.array([170, 120, 70])
upper_black = np.array([180, 255, 255])
mask_2 = cv2.inRange(hsv, lower_black, upper_black)

mask_1 = mask_1 + mask_2

mask_1 = cv2.morphologyEx(mask_1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
mask_1 = cv2.morphologyEx(mask_1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

mask_2 =  cv2.bitwise_not(mask_1)

res_1 = cv2.bitwise_and(img, img, mask=mask_2)

res_2 = cv2.bitwise_and(bg, bg, mask=mask_1)


