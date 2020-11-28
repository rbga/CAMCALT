import picamera
import time
from time import sleep
from fractions import Fraction

with picamera.PiCamera() as camera:
    camera.resolution = (1920, 1080)
    camera.framerate = 24
    camera.contrast = 0
    camera.brightness = 50
    camera.capture('/home/pi/Desktop/Camcalt/detect/detected' + time.strftime("%Y-%m-%d_%H-%M-%S") + '.jpg')