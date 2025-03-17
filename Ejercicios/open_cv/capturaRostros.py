import cv2
import os
import imutils

# cambiar el nombre para cada persona
personName = 'santi' 
dataPath = os.path.join(os.getcwd(), 'imagenes')
personPath = os.path.join(dataPath, personName)

 # crear las carpetas necesarias 
if not os.path.exists(dataPath):
    print('Carpeta creada: imagenes')
    os.makedirs(dataPath)

if not os.path.exists(personPath):
    print('Carpeta creada:', personPath)
    os.makedirs(personPath)

video_file = 'video_santi.mp4'
cap = cv2.VideoCapture(video_file)

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
count = 0

#pasar el video a escala de grises, reconocer las caras, y guardar los frames reconocidos como imagen 
while True:
    ret, frame = cap.read()
    if not ret:
        break

    if video_file == "video_santi.mp4":
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

    frame = imutils.resize(frame, width=640)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()

    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        rostro = auxFrame[y:y + h, x:x + w]
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(os.path.join(personPath, f'rostro{count}.jpg'), rostro)
        count += 1

    cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    if k == 27 or count >= 300:
        break  # Salir del bucle cuando se alcanza el límite de imágenes

cap.release()
cv2.destroyAllWindows()
