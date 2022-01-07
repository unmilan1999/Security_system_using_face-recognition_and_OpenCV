import cv2
import face_recognition as fr
import os
import numpy as np

info = 'admin'

k = []
n = []
c = 0

def updateDir(Listr, kl):
    global k
    global n
    for cl in Listr:
        curImg = cv2.imread(f'{kl}/{cl}')
        k.append(curImg)
        n.append(os.path.splitext(cl)[0])

myL = os.listdir(info)
updateDir(myL, info)

def Enc(images):
    encode = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        en = fr.face_encodings(img)[0]
        encode.append(en)
    return encode

lKnown = Enc(k)

def Intruder(facer):
    print('Intruder is detected!!!\n')
    y1, x2, y2, x1 = facer
    cv2.rectangle(img, (x1,y1), (x2,y2), (0,0,255), 2)
    cv2.rectangle(img, (x1,y2-35), (x2,y2), (0,0,255), cv2.FILLED)
    cv2.putText(img, 'Intruder', (x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
    cv2.imshow('Intruder is not allowed!!', img)

video_capture = cv2.VideoCapture(0)

def Found():
    print('Admin found')
    video_capture.release()
    cv2.destroyAllWindows()
    os.system('python welcome.py')

while c==0:
    _, img = video_capture.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    iloc = fr.face_locations(img)
    ien = fr.face_encodings(img, iloc)
    for eF, fL in zip(ien, iloc):
        mat = fr.compare_faces(lKnown, eF)
        Dis = fr.face_distance(lKnown, eF)
        index = np.argmin(Dis)
        if mat[index]:
            c = 1
            Found()
        else:
            c = 0
            Intruder(fL)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    

video_capture.release()
cv2.destroyAllWindows()
