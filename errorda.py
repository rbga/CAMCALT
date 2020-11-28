import Tkinter as tk
import cv2
from subprocess import call

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

def take():
	call(["python","cap.py"])
	print"completed"

def video():
	call(["python","picam.txt"])
	print"video completed"

def record():
	call(["python", "record.py"])
	print"Recorded and file stored"

def poacher():
	call(["python", "face_rec.py"])
	print"Poacher Detection Begin..."

def train():
	call(["python", "train.py"])
	print"Training of faces begin"

def gps():
	call(["sudo", "python", "gps.py"])
	print"The Coordinates -"

button = tk.Button(frame, 
                   text="Quit", 
                   fg="red",
                   command=quit)
button.pack(side=tk.BOTTOM)

button = tk.Button(frame, 
                   text="Take Picture", 
                   fg="red",command=take
                   )
button.pack(side=tk.BOTTOM)

button = tk.Button(frame, 
                   text="Live Feed", 
                   fg="red",command=video)
button.pack(side=tk.BOTTOM)

button = tk.Button(frame, 
                   text="Record Video", 
                   fg="red",command=record)
button.pack(side=tk.BOTTOM)

button = tk.Button(frame, 
                   text="Poacher Detection", 
                   fg="red",command=poacher)
button.pack(side=tk.BOTTOM)

button = tk.Button(frame, 
                   text="Train Poacher to Camcalt", 
                   fg="red",command=train)
button.pack(side=tk.BOTTOM)

button = tk.Button(frame, 
                   text="GPS Location", 
                   fg="red",command=gps)
button.pack(side=tk.LEFT)

root.mainloop()
