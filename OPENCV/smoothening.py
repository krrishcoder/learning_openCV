import cv2 as cv 

img = cv.imread("images/nature.jpg")
cv.imshow("nature ", img)


# Averaging
avg = cv.blur(img, (3,3))
cv.imshow('Average blur', avg)

# gaussian blur
gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow("gaussian blur", gauss)

# Median Blur

median = cv.medianBlur(img, 3)
cv.imshow("median blur" , median)


# bilateral blurring  --> most effective  , retains edges in images

bilateral = cv.bilateralFilter(img,10,10,15)

cv.imshow("bi lateral", bilateral)

# sigma color --> more color will be considered
# space sigma  --> larger value, pixel furthur out will influence blurring factor

cv.waitKey(0)