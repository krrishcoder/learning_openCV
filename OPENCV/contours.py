import cv2 as cv 
import numpy as np 



# contours and edges are different thing

img = cv.imread('images/cat.jpg')

cv.imshow('Cat' , img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('gray cat ', gray)



blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow("blur", blur)


canny = cv.Canny(blur,125,175)
cv.imshow('edges' , canny)


# instead of canny edge detectors , we can use threshold


# ret , thresh = cv.threshold(gray,160, 255 , cv.THRESH_BINARY)

# cv.imshow("thresh" , thresh)

# finding contours

contours , hierarchies= cv.findContours( canny, cv.RETR_TREE , cv.CHAIN_APPROX_NONE)  # mode in which to find contous , contours approximation method

#  RETR_TREE --> to get all hierarchircal contours , RETR_EXTERNAL --> getting all external contours
#  RETR_LIST --> getting all the contours in an image


print(f'{len(contours)} contours where found')



# visualizing contours found

blank = np.zeros(img.shape, dtype='uint8')

cv.drawContours(blank,contours ,-1, (0,0,255),thickness=1)
cv.imshow("contours drawn", blank)


cv.waitKey(0)



# note!!  simple thresholding has disadvantage , that'why we use canny method