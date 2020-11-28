# facerec.py
import time
import RPi.GPIO as GPIO
import cv2, sys, numpy, os,pyttsx,time
from subprocess import call
size = 4
fn_haar = 'haarcascade_frontalface_default.xml'
fn_dir = '/home/pi/Desktop/Camcalt/Program_Files/Poacher Detection/db'

import RPi.GPIO as GPIO
import time
import os
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

TRIG = 19 
ECHO = 26
l1 =  23
l2 =  24
r1 = 6
r2 = 13
flame = 18
PIR = 4


GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(PIR,GPIO.IN)
GPIO.setup(flame, GPIO.IN)

GPIO.setup(l1,GPIO.OUT)
GPIO.setup(l2,GPIO.OUT)
GPIO.setup(r1,GPIO.OUT)
GPIO.setup(r2,GPIO.OUT)




	
	
GPIO.output(r1,GPIO.LOW)
GPIO.output(r2,GPIO.LOW)
GPIO.output(l1,GPIO.LOW)
GPIO.output(l2,GPIO.LOW)
	




























call(["sudo","pkill","-9","-f","ultra.py"])
GPIO.cleanup()
time.sleep(1)

# Part 1: Create fisherRecognizer
print('Training...')
# Create a list of images and a list of corresponding names
(images, lables, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(fn_dir):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(fn_dir, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            lable = id
	    images.append(cv2.imread(path, 0))
            lables.append(int(lable))
        id += 1
(im_width, im_height) = (112, 92)

# Create a Numpy array from the two lists above
(images, lables) = [numpy.array(lis) for lis in [images, lables]]

# OpenCV trains a model from the images

model = cv2.createFisherFaceRecognizer()
model.train(images, lables)


haar_cascade = cv2.CascadeClassifier(fn_haar)
webcam = cv2.VideoCapture(0)
count = 0
while True:
 try:
    #call(["sudo","python","motorstop.py"])
    (rval, frame) = webcam.read()
    if rval:
        frame=cv2.flip(frame,1,0)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        mini = cv2.resize(gray, (gray.shape[1] / size, gray.shape[0] / size))
        faces = haar_cascade.detectMultiScale(mini)
        for i in range(len(faces)):
            face_i = faces[i]
            (x, y, w, h) = [v * size for v in face_i]
            face = gray[y:y + h, x:x + w]
            face_resize = cv2.resize(face, (im_width, im_height))
            prediction = model.predict(face_resize)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            if prediction[0]==2 or prediction[0]==1 or prediction[0]==0:
		cv2.putText(frame, '%s - %.0f' % (names[prediction[0]],prediction[1]), (x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
		if prediction[0]==2:
			print"human 1"
                	cv2.putText(frame, '%s - %.0f' % (names[prediction[0]],prediction[1]), (x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
			count+=1
			if count == 10:
				print"count reached going to send mail"
				call(["sudo","python","connector.py"])
				
		if prediction[0]==3:
			print"human 2"
                	cv2.putText(frame, '%s - %.0f' % (names[prediction[0]],prediction[1]), (x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
			count+=1
			if count == 15:
				#print"count reached going to send mail"
				#call(["sudo","python","armail.py"])
				print"enter"		
		if '1' in prediction:
			print"door open"
                	cv2.putText(frame, '%s - %.0f' % (names[prediction[0]],prediction[1]), (x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
            else:
                cv2.putText(frame, 'Unknown',(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
	cv2.imshow('Face Recong', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
	print "Poacher Detection Complete"
        break
    
 except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit(0)                
webcam.release()
cv2.destroyAllWindows()
