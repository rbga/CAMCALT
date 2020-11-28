
#! /usr/bin/env python2.7
from subprocess import call
from cv2.cv import *
import RPi.GPIO as GPIO
import time
import urllib2
import json

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.IN)

while True:
    if GPIO.input(4)==1:	
        call(["python", "notify.py"])
        print "Motion Detected"
        
	i=0
        while i<5:
        	call(["python", "cap1.py"])
		time.sleep(.5)	
            	i+=1
        
	call(["python", "errorda.py"])
        time.sleep(2)
            
    else:
     	print "motion not detected"	    
        time.sleep(2)
	    
