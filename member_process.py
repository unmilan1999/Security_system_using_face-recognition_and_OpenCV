import cv2
import face_recognition as fr
import os
import numpy as np

known = 'members'
known2 = 'admins'
k = []
n = []
name = "No access"

def updateDir(Listr, kl):
    global k
    global n
    for cl in Listr:
        curImg = cv2.imread(f'{kl}/{cl}')
        k.append(curImg)
        n.append(os.path.splitext(cl)[0])
        
myL = os.listdir(known)
updateDir(myL, known)
myL2 = os.listdir(known2)
updateDir(myL2, known2)
print(n)

def Enc(images):
    encode = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        en = fr.face_encodings(img)[0]
        encode.append(en)
    return encode

lKnown = Enc(k)

def goto():
    nm = input('Enter name: ')
    nm = nm.lower()
    return nm

def NotFound(img, tacer):

    name = "No access"
    y1, x2, y2, x1 = tacer
    normal_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    if name == "No access":
            global myL
            global n
            global k
            global lKnown
            global known
            global known2
            global myL2
            name = goto()
            if name in n:
                print('Member name already exists')
                print('')
                goto()
            
            else:
                cv2.imwrite(known+"/"+name+".jpg", normal_img)
                listo = os.listdir(known)
                if name not in n:
                    myL.clear()
                    k.clear()
                    n.clear()
                    myL = listo
                    updateDir(myL, known)
                    updateDir(myL2, known2)
                    lKnown.clear()
                    lKnown = Enc(k)
        
def Found(nList, i, facer):
    name = nList[i].upper()
    y1, x2, y2, x1 = facer
    cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
    cv2.rectangle(img, (x1,y2-35), (x2,y2), (0,255,0), cv2.FILLED)
    cv2.putText(img, name, (x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)

video_capture = cv2.VideoCapture(0)

while True:
    _, img = video_capture.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    iloc = fr.face_locations(img)
    ien = fr.face_encodings(img, iloc)
    for eF, fL in zip(ien, iloc):
        if len(myL) == 0:
            NotFound(img, fL)
        mat = fr.compare_faces(lKnown, eF)
        Dis = fr.face_distance(lKnown, eF)
        index = np.argmin(Dis)
        if mat[index]:
            Found(n, index, fL)
 
        else:
            NotFound(img, fL)

    cv2.imshow('Face Detection', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
