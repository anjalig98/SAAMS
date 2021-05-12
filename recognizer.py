import cv2, numpy as np;
import xlwrite
import time
import sys

start=time.time()
period=8
#face_cas = cv2.CascadeClassifier('haarcascade_profileface.xml')
face_cas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0);
recognizer = cv2.face.LBPHFaceRecognizer_create();
recognizer.read('trainer/trainer.yml');
flag = 0;
id=0;
filename='filename';
dict1 = {
            'item1': 1
}

refECE1 = {'V.M Aravind':'no' ,'Anjali G':'no'}
#font = cv2.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 5, 1, 0, 1, 1)
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, img = cap.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    faces = face_cas.detectMultiScale(gray, 1.3, 7);
   
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2);
        id,conf=recognizer.predict(roi_gray)
        if(conf < 50):
         if(id==1):
            id='V.M Aravind'
            if((str(id)) not in dict1):
                #filename=xlwrite.output('attendanceECE1','class1',1,id,'yes');
                dict1[str(id)]=str(id);
                print('V.M Aravind is present')
                refECE1['V.M Aravind']='yes'


         elif(id==2):
            id = 'Anjali G'
            if ((str(id)) not in dict1):
                #filename =xlwrite.output('attendanceECE1', 'class1', 2, id, 'yes');
                dict1[str(id)] = str(id);
                print('Anjali G is present')
                refECE1['Anjali G']='yes'

         elif(id==3):
            id = 'name3'
            if ((str(id)) not in dict1):
                filename =xlwrite.output('attendanceECE1', 'class1', 3, id, 'yes');
                dict1[str(id)] = str(id);

         elif(id==4):
            id = 'name4'
            if ((str(id)) not in dict1):
                filename =xlwrite.output('attendanceECE1', 'class1', 4, id, 'yes');
                dict1[str(id)] = str(id);

         else:
             id = 'Unknown, can not recognize'
             flag=flag+1
             break
        
        cv2.putText(img,str(id)+" "+str(conf),(x,y-10),font,0.55,(120,255,120),1)
        #cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,0,255));
    cv2.imshow('frame',img);
    #cv2.imshow('gray',gray);
    if flag == 10:
        
        print("Transaction Blocked")
        break;
    if time.time()>start+period:
        break;
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break;

cap.release();
cv2.destroyAllWindows();
j=1
for i in refECE1:
            filename =xlwrite.output('attendanceECE1', 'class1', j, i, refECE1[i]);
            j=j+1

