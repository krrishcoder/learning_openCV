import cv2 as cv 
import matplotlib.pyplot as plt 

# color space --> space of color

img = cv.imread('images/cat.jpg')
cv.imshow('cat' , img)

# BGR to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray scaled image" , gray)


# BGR to HSV

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv" , hsv)

# BGR to L * a * b

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab' , lab)


# BGR TO RGB

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

# plt.imshow(rgb)
# plt.show()


# HSV TO BGR


hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("hsv --> bgr" , hsv_bgr)


# LAB TO BGR

lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("lab --> bgr" , lab_bgr)


cv.waitKey(0)