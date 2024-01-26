import cv2 as cv 

img = cv.imread("images/sun.jpg")
cv.imshow('Nature',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# simple thresholding

threshold ,thresh =  cv.threshold(gray,100,255, cv.THRESH_BINARY)
cv.imshow("thresholded image",thresh)

#inverse threshold

threshold ,thresh_inv =  cv.threshold(gray,100,255, cv.THRESH_BINARY_INV)
cv.imshow("thresholded image inverse",thresh_inv)


# adaptive thresholding   --> optimal T value  two methods mean , gaussian 
adaptive_thresh = cv.adaptiveThreshold(gray,255 , cv.ADAPTIVE_THRESH_GAUSSIAN_C , cv.THRESH_BINARY_INV, 11 , 3)

cv.imshow("adaptive thresholding", adaptive_thresh)

cv.waitKey(0)