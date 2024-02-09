
import numpy as np
import matplotlib.pyplot as plt
import cv2 

from machinevisiontoolbox import Image

  
# path 
path = '/Users/nick/ImageEdit/sample_stop_sign.png'

image = cv2.imread(path)
kernel = np.ones((9,9),np.float32)/81
image = cv2.filter2D(image,-1,kernel)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define a range for the red color in HSV
lower_red = np.array([0, 120, 80])
upper_red = np.array([10, 255, 255])
# Create a mask using the inRange function
mask = cv2.inRange(hsv, lower_red, upper_red)
# Bitwise AND the original image with the mask
result = cv2.bitwise_and(image, image, mask=mask)

gray_img=cv2.cvtColor(result,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray_img, 1, 255, cv2.THRESH_BINARY)

blobs = thresh.blobs()
if len(blobs) > 0:
    for blob in range(len(blobs)):
        if blobs[blob].area > 100:
            print("Stop Sign!")
            bot.setVelocity(0, 0)
            time.sleep(0.5)
            break

