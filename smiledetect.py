
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# from time import sleep
# sd=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')
# fd=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
# vid=cv2.VideoCapture(0)
# # vid=cv2.VideoCapture(0)
# while True:
#     flag,img=vid.read()
#     if flag:
#         img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#         faces=fd.detectMultiScale(
#             img_gray,
#             scaleFactor=1.1, 
#             minNeighbors=5,
#             minSize=(50,50)
#             )
#         np.random.seed(50)
#         colors=[np.random.randint(0,255,3).tolist()
#                 for i in faces]
#         i=0
#         # th,img_bw=cv2.threshold(img_gray,170,255,cv2.THRESH_BINARY)
#         for x,y,w,h in faces:
#         #  x,y,w,h=(350,300,300,200)
#             face=img[y:y+h,x:x+w,:].copy()
#             smiles=sd.detectMultiScale(
#                 img_gray,
#                 scaleFactor=1.1, 
#                 minNeighbors=5,
#                 minSize=(50,50)
#             )
#             if(len(smiles)==1):
#                 cv2.imwrite('myself.png',img)
#             cv2.rectangle(
#                 img,pt1=(x,y), pt2=(x+w,y+h), color=colors[i],
#                 thickness=8
#             )
#             i=i+1
        
#         cv2.imshow('preview',img)
#         key = cv2.waitKey(1)
#         if key==ord('q'):
#             break
        
#     else:
#      print('no frame')
#      break
# sleep(0.1)
# vid.release()
# cv2.destroyAllWindows()

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# from time import sleep
# sd=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')
# fd=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
# vid=cv2.VideoCapture(0)
# # vid=cv2.VideoCapture(0)
# while True:
#     flag,img=vid.read()
#     if flag:
#         img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#         faces=fd.detectMultiScale(
#             img_gray,
#             scaleFactor=1.1, 
#             minNeighbors=5,
#             minSize=(50,50)
#             )
#         np.random.seed(50)
#         colors=[np.random.randint(0,255,3).tolist()
#                 for i in faces]
#         i=0
#         # th,img_bw=cv2.threshold(img_gray,170,255,cv2.THRESH_BINARY)
#         for x,y,w,h in faces:
#         #  x,y,w,h=(350,300,300,200)
#             face=img[y:y+h,x:x+w,:].copy()
#             smiles=sd.detectMultiScale(
#                 img_gray,
#                 scaleFactor=1.1, 
#                 minNeighbors=5,
#                 minSize=(50,50)
#             )
#             if(len(smiles)==1):
#                 cv2.imwrite('myself.png',img)
#             cv2.rectangle(
#                 img,pt1=(x,y), pt2=(x+w,y+h), color=colors[i],
#                 thickness=8
#             )
#             i=i+1
        
#         cv2.imshow('preview',img)
#         key = cv2.waitKey(1)
#         if key==ord('q'):
#             break
        
#     else:
#      print('no frame')
#      break
# sleep(0.1)
# vid.release()
# cv2.destroyAllWindows()

#current working
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# from time import sleep
# sd=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')
# fd=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
# vid=cv2.VideoCapture(0)
# seq=0
# # vid=cv2.VideoCapture(0)
# while True:
#     flag,img=vid.read()
#     if flag:
#         img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#         faces=fd.detectMultiScale(
#             img_gray,
#             scaleFactor=1.1, 
#             minNeighbors=5,
#             minSize=(50,50)
#             )
#         np.random.seed(50)
#         colors=[np.random.randint(0,255,3).tolist()
#                 for i in faces]
#         i=0
#         # th,img_bw=cv2.threshold(img_gray,170,255,cv2.THRESH_BINARY)
#         for x,y,w,h in faces:
#         #  x,y,w,h=(350,300,300,200)
#             face=img[y:y+h,x:x+w,:].copy()
#             smiles=sd.detectMultiScale(
#                 img_gray,
#                 scaleFactor=1.1, 
#                 minNeighbors=5,
#                 minSize=(50,50)
#             )
            
#             if(len(smiles)==1):
#                 seq+=1
#                 if seq==10:
#                     cv2.imwrite('myself.png',img)
#                     notCaptured=False
#                     break
#             else 
#                 seq=0
#             cv2.rectangle(
#                 img,pt1=(x,y), pt2=(x+w,y+h), color=colors[i],
#                 thickness=8
#             )
#             i=i+1
            
#         cv2.imshow('preview',img)
#         key = cv2.waitKey(1)
#         if key==ord('q'):
#             break
        
#     else:
#      print('no frame')
#      break
# sleep(0.1)
# vid.release()
# cv2.destroyAllWindows()

#mayank code
# import numpy as np
# import cv2
# import matplotlib.pyplot as plt
# from time import sleep

# fd=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
# sd=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')
# vid=cv2.VideoCapture(0)
# while True:
#     flag, img = vid.read()
#     if flag:
#         img_gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         faces = fd.detectMultiScale(
#             img_gray,
#             scaleFactor = 1.1,
#             minNeighbors= 5,
#             minSize= (50,50)
#             )
#         np.random.seed(50)
#         colors = [np.random.randint(0,255,3).tolist() 
#                   for i in faces]
#         i=0
#        # th, img_bw =cv2.threshold(img_gray,170,255,cv2.THRESH_BINARY)
       
#         #x,y,w,h=(400,300,300,200)
#         #img_cropped=img[y:y+h, x:x+w, :]
#         for x,y,w,h in faces:
#             cv2.rectangle(
#             img,pt1=(x,y),pt2=(x+w,y+h), color=colors[i],
#             thickness=8
#             )
#             i=i+1

#         cv2.imwrite('myselfie.png',img)    

        

#         cv2.imshow('Preview', img)
#         key=cv2.waitKey(1)
#         if key==ord('q'):
#             break
#     else:
#         print('No Frames')
#         break
#     sleep(0.1)
# vid.release()
# cv2.waitKey(1)
# cv2.destroyAllWindows()


#final correct
import cv2
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
fd=cv2.CascadeClassifier(
    cv2.data.haarcascades+'haarcascade_frontalface_default.xml'
)
sd=cv2.CascadeClassifier(
    cv2.data.haarcascades+'haarcascade_smile.xml'
)
vid = cv2.VideoCapture(0)
notCaptured = True
seq = 0
while notCaptured:
    flag, img = vid.read()
    if flag:
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = fd.detectMultiScale(
            img_gray,
            scaleFactor = 1.1,
            minNeighbors = 5,
            minSize = (50,50)
        )
        np.random.seed(50)
        colors = np.random.randint(0,255, (len(faces), 3)).tolist() 
        i = 0
        for x,y,w,h in faces:
            face = img_gray[y:y+h, x:x+w].copy()
            smiles = sd.detectMultiScale(
                face,
                scaleFactor = 1.1,
                minNeighbors = 5,
                minSize = (50,50)
            )

            if len(smiles) == 1:
                seq += 1
                print(seq)
                if seq == 5:
                    cv2.imwrite('myself.png', img)
                    cv2.imshow('Preview', img)
                    notCaptured = False
                    break
            else:
                seq = 0

            cv2.rectangle(
                img, pt1=(x,y), pt2=(x+w, y+h), color=colors[i],
                thickness=8
            )
            i += 1
       
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    else:
        print('No Frames')
        break
    sleep(0.1)
cv2.destroyAllWindows()
cv2.waitKey(1)
vid.release()
del vid



 