import cv2 as cv 

img = cv.imread('images/cat.jpg')

cv.imshow('Cat BGR', img)

# converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray CAT' , gray)


#blur
blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blur CAT' , blur)

# finding edge in images  or Edge cascade
canny = cv.Canny(blur,125,175)
cv.imshow('Canny edges', canny)

# dialating an image
dialted = cv.dilate(canny,(3,3),iterations=3)
cv.imshow('dialted image', dialted)



# eroding an image
eroded = cv.erode(dialted,(3,3),iterations=3)
cv.imshow('eroded image', eroded)

# resize
resized = cv.resize(img,(300,200),interpolation=cv.INTER_CUBIC)
cv.imshow('resized image', resized)  # will not consider the aspect ratio

# cropping
cropped = img[100:300,300:600]
cv.imshow("cropped image",cropped)

cv.waitKey(0)
