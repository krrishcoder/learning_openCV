import cv2 as cv
import numpy as np 

img = cv.imread( "images/cat.jpg")


#creating a blank image
blank = np.zeros((500,500,3),dtype='uint8')

# 1. draw a certain portion of image
# blank[200:300,300:400] = 0,0,255
# cv.imshow('blank', blank)

# 2. draw a rectangle
cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=-1)  # thickness = cv.FILLED , thickness = 2 for border of thickness 2 
cv.imshow('rectangle', blank)

# 3. draw a circle
cv.circle(blank,(250,250),100,(0,0,255),thickness=-1)
cv.imshow('circle',blank)

# 4. draw a line
cv.line(blank,(0,0),(250,250),(255,255,255),thickness=3)
cv.imshow('line',blank)

# 5. write a text on image
cv.putText(blank,"HEllo , my name is krrish ",(0,250),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),1)
cv.imshow('Text',blank)


# cv.imshow("Cat",img)

cv.waitKey(0) # 0 means,  a blocking call that waits for a key event.