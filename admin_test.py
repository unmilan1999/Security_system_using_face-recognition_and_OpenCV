import cv2
import face_recognition as fr
import os
import numpy as np

known = 'admins'
k = []
n = []
name = "Admin"
flag = 0

def flagShift():
    global flag
    flag = 1

def updateDir(Listr):
    global k
    global n
    for cl in Listr:
        curImg = cv2.imread(f'{known}/{cl}')
        k.append(curImg)
        n.append(os.path.splitext(cl)[0])
        
myL = os.listdir(known)
updateDir(myL)

def Enc(images):
    encode = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        en = fr.face_encodings(img)[0]
        encode.append(en)
    return encode

lKnown = Enc(k)

def FailedAuth(image, locn):
    global flag
    global name
    y1, x2, y2, x1 = locn
    flagShift()
    nm = 'Intruder'
    cv2.rectangle(image, (x1,y1), (x2,y2), (0,0,255), 2)
    cv2.rectangle(image, (x1,y2-35), (x2,y2), (0,0,255), cv2.FILLED)
    cv2.putText(image, nm, (x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
    name = nm
       
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
            flagShift()
            break
        mat = fr.compare_faces(lKnown, eF)
        Dis = fr.face_distance(lKnown, eF)
        index = np.argmin(Dis)
        if mat[index]:
            Found(n, index, fL)
 
        else:
            FailedAuth(img, fL)

    cv2.imshow('Face Detection', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

if name != 'Intruder' and flag==0:
    k.clear()
    n.clear()
    lKnown.clear()
    myL.clear()
    i = 1
    kap = 'members'
    myL = os.listdir(kap)
    updateDir(myL)
    print('')
    print('Members')
    print('-------')
    for c in n:
        print(i, c)
        i=i+1
    print('')
    ch = input('Select the member you wanna make admin: ')
    ch = int(ch)
    x = n[ch-1]
    print('')
    os.rename('members/'+myL[ch-1], 'admins/'+myL[ch-1])
    print(n[ch-1], 'is now admin!!')
    print('')

if flag == 1:
    print('')
    print('We found an intruder while doing face detection...')
    print('')
    
video_capture.release()
cv2.destroyAllWindows()
