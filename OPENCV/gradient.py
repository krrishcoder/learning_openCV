import cv2 as cv 
import numpy as np 

img = cv.imread("images/cat.jpg")
cv.imshow("nature" , img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# laplacian --> way tpo detect edges
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

cv.imshow("Laplacian", lap)

# Sobel --> calcualtes in 2 direction x and y

sobelx= cv.Sobel(gray, cv.CV_64F, 1, 0 )
sobely = cv. Sobel(gray, cv.CV_64F , 0 , 1)

combined = cv.bitwise_or(sobelx,sobely)

canny = cv.Canny(gray,125,175)


cv.imshow("sobel x" , sobelx)
cv.imshow("sobel y", sobely)
cv.imshow("combined sobel", combined)
cv.imshow("canny", canny)





cv.waitKey(0)