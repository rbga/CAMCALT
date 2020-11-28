import picamera
import time
import tkMessageBox as tmb

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 90
camera.start_recording('/home/pi/Desktop/Camcalt/video/my_video' + time.strftime("%Y-%m-%d_%H-%M-%S") + '.h264')
camera.wait_recording(5)
camera.stop_recording()
tmb.showinfo("Record Video", "5 sec Video Recorded and Stored Successfully")