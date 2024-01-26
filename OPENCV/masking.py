


#masking allows to focus on certain part of image
# example --> working on faces of human , and removing rest


import cv2 as cv 
import numpy as np 

img = cv.imread("images/cat.jpg")
cv.imshow("Cat" , img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

circle  =  cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 400 , 255, -1) # circular mask

# cv.imshow('Mask', mask)

rectangle = cv.rectangle(blank.copy(),(30,30), (370,370), 255 ,-1)  # rectangular mask

weired_mask =cv.bitwise_and(circle,rectangle)

cv.imshow('wired shape' , weired_mask)

masked = cv.bitwise_and(img,img,mask=weired_mask)
cv.imshow('weired shape masked image',masked)


# masked = cv.bitwise_and(img,img,mask=mask)
# cv.imshow('masked image',masked)

cv.waitKey(0)