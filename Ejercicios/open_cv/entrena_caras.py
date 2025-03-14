import cv2
import os
import numpy as np

dataPath = os.path.join(os.getcwd(), 'imagenes')
peopleList = os.listdir(dataPath)
print('Lista de personas: ', peopleList)
labels = []
facesData = []
label = 0
for nameDir in peopleList:
    personPath = dataPath + '/' + nameDir
    print('Leyendo las imágenes')
    for fileName in os.listdir(personPath):
        print('Rostros: ', nameDir + '/' + fileName)
        labels.append(label)
        facesData.append(cv2.imread(personPath+'/'+fileName,0))
        image = cv2.imread(personPath+'/'+fileName,0)
        #cv2.imshow('image',image) #mostrar imagenes
        #cv2.waitKey(10)
    label = label + 1
 # cv2.destroyAllWindows

# mostrar labels
# print('labels= ',labels)
# print('Número de etiquetas 0: ',np.count_nonzero(np.array(labels)==0))
# print('Número de etiquetas 1: ',np.count_nonzero(np.array(labels)==1))

print("Entrenamiento: ")

face_recognizer = cv2.face.EigenFaceRecognizer_create()
face_recognizer_fisher = cv2.face.FisherFaceRecognizer_create()
#face_recognizer_fisher = cv2.face.FaceRecognizer_create()


face_recognizer.train(facesData, np.array(labels))
face_recognizer_fisher.train(facesData, np.array(labels))
# Guardar el modelo

face_recognizer.write('modeloEigenFace.xml')
#face_recognizer_fisher.write('modeloFisherFace.xml')

print("Modelos guardados")

### FALTAN 3 PERSONAS MÁS 