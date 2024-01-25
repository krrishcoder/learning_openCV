import cv2 as cv

#reading images
# img = cv.imread("images/cat2.webp")

  #name , img path or matrix
# cv.imshow('cat',img)



# cv.waitKey(0)


#reading videos


# either 0 ,1 2 3 as argument , if you are using webcam or camera connected to  computer
# or path file as string
capture = cv.VideoCapture("videos/cat.mp4")

#we read video frame by frame

while True :
    isTrue , frame = capture.read()  #returns --> read successfully or not , a frame
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


