import numpy as np 
import cv2 as cv 
import face_recognition

people = ["krishna","chetan"]

features = np.load("features.npy", allow_pickle=True)

features = features.astype(float)

labels = np.load("labels.npy",allow_pickle=True)


known_faces = [face_encoding.flatten() for face_encoding in features]



# Compute face encodings for the unknown image

capture = cv.VideoCapture(0)

haar_cascade = cv.CascadeClassifier("haar_face.xml")


while True :
    isTrue , frame = capture.read() 

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=7)

    framex = frame


    a =0
    b=0
    c=0
    d=0
    for (x,y,w,h) in faces_rect :
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
        framex = frame[y:y+w,x:x+h]
        a=x
        b=y
        c=w
        d=h



   

    key = cv.waitKey(1)
    if key == 27:
        break

    unknown_face_encodings = face_recognition.face_encodings(frame)

    # Check if any faces are found in the unknown image
    if len(unknown_face_encodings) > 0:
    #     # Assume the first detected face is the target
        unknown_face_encoding = unknown_face_encodings[0]

        # if unknown_face_encoding.shape[0] == 128:
        #     print("Unknown Face Encoding has 128 dimensions.")

        # for i, face_encoding in enumerate(known_faces):
        #     if face_encoding.shape[0] == 128:
        #         print(f"Face {i + 1} has 128 dimensions.")
        #     else:
        #         print(f"Face {i + 1} has unexpected dimensions: {face_encoding.shape}")


        if features.size > 0 and unknown_face_encoding.size > 0:
            matches = face_recognition.compare_faces(known_faces, unknown_face_encoding)
            
         
            for i, face_encoding in enumerate(matches):
                if face_encoding==True:
                    # print(people[labels[i]])
                    cv.putText(frame,people[labels[i]],(a,b-10),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),1)  
                    break


        cv.imshow('Video', frame)

        # Find the index of the first match (if any)
       
        

        


capture.release()
cv.destroyAllWindows()


# note !!

# there are very few things that can actually beat the deep learning model

# we will be building deep Computer vision model to classify between the sensing characters

# we will use tensor flow implementation

# taking help from kaggle

# we require a GPU --> speeds up the training process

# kaggle offers free GPU'S for us to use

