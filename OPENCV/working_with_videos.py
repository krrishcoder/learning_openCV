import cv2 as cv


capture = cv.VideoCapture(0)

haar_cascade = cv.CascadeClassifier("haar_smile.xml")


while True :
    isTrue , frame = capture.read()  #returns --> read successfully or not , a frame
 
    # if cv.waitKey(20) & 0xFF == ord('d'):
    #     break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=7)

    for (x,y,w,h) in faces_rect :
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)

    cv.imshow('Video', frame)

    key = cv.waitKey(1)
    if key == 27:
        break

capture.release()
cv.destroyAllWindows()

