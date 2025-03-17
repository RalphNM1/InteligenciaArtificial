import cv2
import os

dataPath = os.path.join(os.getcwd(), 'imagenes')
imagePaths = os.listdir(dataPath)
print('imagePaths',imagePaths)

face_recognizer = cv2.face.EigenFaceRecognizer_create()

face_recognizer.read('modeloEigenFace.xml')

video_file = 'video_yuliia.mp4'
cap = cv2.VideoCapture(video_file)

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret,frame = cap.read()
    if video_file == "video_santi.mp4": # he tenido que girar el video de santi ya que aparece en horizontal y no detecta bien la cara
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    
    if ret == False: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()

    faces = faceClassif.detectMultiScale(gray, 1.3, 5)
    

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        rostro = auxFrame[y:y + h, x:x + w]
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
        result = face_recognizer.predict(rostro)
    
        cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)

        print(result)  # al final he decido usar tannto result[0] como result[1]
        if result[0] == 1:
            cv2.putText(frame,'{}'.format(imagePaths[1]),(x,y-25),1,1.1,(0,255,0),1,cv2.LINE_AA) # colocar el nombre de la persona reconocida
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) # colocar el rectangulo alrededor de la cara
        elif result[0] == 0 and result[1] < 5000:
            cv2.putText(frame,'{}'.format(imagePaths[0]),(x,y-25),1,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        elif result[0] == 3 and result[1] < 3000:
            cv2.putText(frame,'{}'.format(imagePaths[3]),(x,y-25),1,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        elif result[0] == 2:
            cv2.putText(frame,'{}'.format(imagePaths[2]),(x,y-25),1,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        elif result[1] > 6500:
            cv2.putText(frame,'{}'.format('Desconocido'),(x,y-20),1,1.3,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)        
        else:
            cv2.putText(frame,'{}'.format('Desconocido'),(x,y-20),1,1.3,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('frame',frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
