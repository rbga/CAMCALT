import picamera
import time
from time import sleep
from fractions import Fraction 
import Tkinter as tk
import tkMessageBox as tmb

with picamera.PiCamera() as camera:
    camera.resolution = (1920, 1080)
    camera.framerate = 24
    camera.contrast = 0
    camera.brightness = 50
    b=input(" No. of Burst Images? ")
    type(b)
    
    a=0
    while a<b:
    	camera.capture('/home/pi/Desktop/Camcalt/photo/image_taken' + time.strftime("%Y-%m-%d_%H-%M-%S") + '.jpg')
    	time.sleep(.5)
	a+=1

tmb.showinfo("Take Image", "Images Captured Successfully")