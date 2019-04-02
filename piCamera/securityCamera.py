import cv2
import time
import sys, os

lastCap = int(round(time.time() * 1000)) - 10000

cap = cv2.VideoCapture(0)
cap.set(3, 640) #WIDTH
cap.set(4, 480) #HEIGHT

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(len(faces))
    if(len(faces) > 0):
        if(int(round(time.time() * 1000)) > lastCap + 10000):
            lastCap = int(round(time.time() * 1000))
            fileName = str(lastCap) + '.png'
            #print("File saved as " + fileName)
            cv2.imwrite(fileName, frame)
            #print("Issuing command: " + "./curl.sh " + fileName)
            os.system("./curl.sh " + fileName)
    # Display the resulting frame
    for (x, y, w, h) in faces:
         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
         roi_gray = gray[y : y + h, x : x + w]
         roi_color = frame[y : y + h, x : x + w]
        
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()