import os
import cv2 as cv 
import numpy as np 
import face_recognition

# label -->  0   ,   1
people = ['krishna','chetan']


DIR = r'/Users/rajkumar/Downloads'

features = []
labels = []

haar_cascade = cv.CascadeClassifier('haar_face.xml')   # object detection algorithm 


i = 0
def create_train() :
    global i
    for person in people:
        path = os.path.join(DIR,person)   # since  folder name is same as person name
        label = people.index(person)

        for img in os.listdir(path):             
            img_path = os.path.join(path,img)

            img_arr = cv.imread(img_path)
            # gray = cv.cvtColor(img_arr , cv.COLOR_BGR2GRAY)
            # cv.imshow(str(i),gray)

            i +=1

            face_encoding = face_recognition.face_encodings(img_arr)
            # faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

            if len(face_encoding) > 0:
                features.append(face_encoding)
                labels.append(label)

            # for (x,y,w,h) in faces_rect :
            #     faces_region = gray[y:y+h,x:x+w]
            #     features.append(faces_region)
            #     labels.append(label)



create_train()
print("training done ---------------")


try:
    features = np.array(features , dtype='object')
    labels = np.array(labels, dtype='uint8')

# train the recognizer  on the features list and the labels list
    
    print(labels)
    print(len(labels))
    print(len(features))

    # Train the face recognition model
  
    model = {"features": features, "label" : labels}
    np.save('features.npy', features)
    np.save('labels.npy', labels)

except Exception as e:
    print("caught exception")
    print(e)



# cv.waitKey(0)



            