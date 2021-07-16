import cv2
import face_recognition as fr
import os
import numpy as np

known = 'admins'
k = []
n = []
name = "No access"
flag = 0

def updateDir(Dir, Listr, kode, node):
    for cl in Listr:
        curImg = cv2.imread(f'{Dir}/{cl}')
        kode.append(curImg)
        node.append(os.path.splitext(cl)[0])
        
myL = os.listdir(known)
updateDir(known, myL, k, n)

def Enc(images):
    encode = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        en = fr.face_encodings(img)[0]
        encode.append(en)
    return encode

lKnown = Enc(k)

def FailedAuth(image, locn, nm):
    global flag
    y1, x2, y2, x1 = locn
    flag = 1
    cv2.rectangle(image, (x1,y1), (x2,y2), (0,0,255), 2)
    cv2.rectangle(image, (x1,y2-35), (x2,y2), (0,0,255), cv2.FILLED)
    cv2.putText(image, nm, (x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)

def AdminAdd(img, tacer):

    global name
    if name == 'Intruder':
        FailedAuth(img, tacer, name)
    else:
        name = "No access"
    y1, x2, y2, x1 = tacer
    normal_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    if name == "No access":
            global myL
            global n
            global k
            global lKnown
            name = input('Enter name: ')
            name = name.lower()
            if name in n:
                name = 'Intruder'
                return
            
            else:
                cv2.imwrite(known+"/"+name+".jpg", normal_img)
                listo = os.listdir(known)
                if name not in n:
                    myL.clear()
                    k.clear()
                    n.clear()
                    myL = listo
                    updateDir(known, myL, k, n)
                    lKnown.clear()
                    lKnown = Enc(k)
        
def Found(nList, i, facer):
    name = nList[i].upper()
    y1, x2, y2, x1 = facer
    cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
    cv2.rectangle(img, (x1,y2-35), (x2,y2), (0,255,0), cv2.FILLED)
    cv2.putText(img, name, (x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)

def OurMember(nym, img2, track):
    global flag
    y1, x2, y2, x1 = track
    flag = 1
    cv2.rectangle(img2, (x1,y1), (x2,y2), (255,0,0), 2)
    cv2.rectangle(img2, (x1,y2-35), (x2,y2), (255,0,0), cv2.FILLED)
    cv2.putText(img2, nym, (x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
    
def CheckForMember(image, e, l):
    global name
    klass = 'members'
    k1 = []
    n1 = []
    memList = os.listdir(klass)
    updateDir(klass, memList, k1, n1)
    lK = Enc(k1)
    for eF1, fL1 in zip(e, l):
        m1 = fr.compare_faces(lK, eF1)
        d1 = fr.face_distance(lK, eF1)
        id1 = np.argmin(d1)
        if m1[id1]:
            name = 'Member'
            OurMember(name, image, fL1)
        else:
            AdminAdd(image, fL1)

video_capture = cv2.VideoCapture(0)

while True:
    _, img = video_capture.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    iloc = fr.face_locations(img)
    ien = fr.face_encodings(img, iloc)
    for eF, fL in zip(ien, iloc):
        mat = fr.compare_faces(lKnown, eF)
        Dis = fr.face_distance(lKnown, eF)
        index = np.argmin(Dis)
        if mat[index]:
            Found(n, index, fL)
 
        else:
            CheckForMember(img, ien, iloc)

    cv2.imshow('Face Detection', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

if name != 'Intruder' and flag == 0:
    k.clear()
    n.clear()
    lKnown.clear()
    myL.clear()
    i = 1
    kap = 'members'
    myL = os.listdir(kap)
    updateDir(known, myL, k, n)
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

elif name == 'Member':
    print('')
    print('You are a member')
    print('')

else:
    print('')
    print('You are intruder...you dont have admin access')
    print('')
    
video_capture.release()
cv2.destroyAllWindows()
