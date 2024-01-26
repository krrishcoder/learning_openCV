import cv2 as cv

img = cv.imread("images/cat.jpg")
cv.imshow('Cat',img)




def rescaleFrame(frame , scale =0.75):

    #  Images , Videos , Live  Video

    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width,height)   #tuple

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)



img_resized = rescaleFrame(img,scale=0.30)

cv.imshow('Resized Cat', img_resized)


def changeRes(height,width):
    #Live Video
    capture.set(3,width)   #here 3 means , the parameter lies on 3rd somewhere
    capture.set(4,height)



capture = cv.VideoCapture("videos/cat.mp4")

#we read video frame by frame

while True :
    isTrue , frame = capture.read()  #returns --> read successfully or not , a frame

    frame_resized = rescaleFrame(frame,scale=0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video resized' , frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
