import cv2
import numpy as np
import os
import time

#IN PLACE OF 0 YOU CAN GIVE YOUR "VIDEO FILE" AS INPUT 
cap=cv2.VideoCapture('frame.jpg')

font = cv2.FONT_HERSHEY_SIMPLEX
face_detector = cv2.CascadeClassifier('haar_IS_haar.xml')
while True:
    # GET CAMERA IMAGE AND CONVERT TO GRAYSCALE
    success, img = cap.read()   
  
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face = face_detector.detectMultiScale(gray, 1.3, 5)
    if len(face) > 2 :
        cv2.imwrite('frame.jpg', img)
        print('Found Triple Rding ')
        #print(ocr('frame.jpg'))

    for (x, y, w, h) in face:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            cv2.putText(img,'Face',(x, y), font, 2,(255,0,0),5)



    cv2.putText(img,'Number of Faces : ' + str(len(face)),(40, 40), font, 1,(255,0,0),2)      
    # Display the resulting frame
    cv2.imshow('Video', img)


    if cv2.waitKey(1) & 0xFF == ord('q'):
         break
