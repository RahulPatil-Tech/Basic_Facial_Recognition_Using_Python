import cv2 
import numpy as np
face_cascade = cv2.CascadeClassifier('E:\Python Project\Facial recignition\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
def detect_faces():
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        cv2.imshow('Face Detection', frame)
        
        if cv2.waitKey(1) == 27:  # Press Esc to exit
            break
    
    cap.release()
    cv2.destroyAllWindows()
detect_faces()
