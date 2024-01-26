
import cv2 as cv 
import numpy as np 


img = cv.imread('images/cat.jpg')
cv.imshow('Cat', img)



# Translation

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],  img.shape[0])          # width ,height

    return cv.warpAffine(img,transMat,dimensions)

# -x -->LEFT
# -y  --> up
# x   --> right
# y  --> down


translated = translate(img, -300,300)

cv.imshow('Translated',translated)


# rotation

def rotate(img,angle,rotPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint ==None :
        rotPoint = (width//2 , height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0) 
    dimensions = (width,height)

    return cv.warpAffine(img,rotMat,dimensions)


rotated = rotate(img, -45)

cv.imshow("roatated image" , rotated)


# Resizing

resized = cv.resize(img, (500,1000) , interpolation=cv.INTER_CUBIC)

cv.imshow('Resized' , resized)


# Flipping an image
flip = cv.flip(img,-1)
cv.imshow('flipped' , flip)

# 0  ->  vertically
# 1  -> horizontally
# -1 ->



# cropping

cropped = img[200:400,300:400]
cv.imshow("cropped", cropped)


cv.waitKey(0)

