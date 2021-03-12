import cv2

# sınıflandırıcı
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# video
cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

while True:
    
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    
    if ret:
        
        face_rect = face_cascade.detectMultiScale(frame, minNeighbors = 15)
        
        for (x, y, w, h) in face_rect:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)
        cv2.imshow("face detect", frame)
        
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()