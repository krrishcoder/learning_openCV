# will be using classifier to detect faces that are present in an image

import cv2 as cv 


img = cv.imread("images/group.jpg")
cv.imshow("lady face",img)

# mostly we does not require any tones of skin
# we see mainly edges

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray" , gray)

haar_cascade = cv.CascadeClassifier("haar_face.xml")

# now lets try to detect

faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=11)

# rectangular coordinates of that face as a list

print(f'number of faces found {len(faces_rect)}')


for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0),thickness=2)

cv.imshow("detected face", img)


cv.waitKey(0)