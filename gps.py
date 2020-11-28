import serial
from pynmea import nmea
import time
import cv2
import tkMessageBox as tmb
ser=serial.Serial('/dev/ttyS0')
ser.baudrate=9600
print('Waiting for data')
gpgga = nmea.GPGGA()

try:
	while True:
		message = ser.readline()
		if message[0:6] == '$GPGGA':   
			print(message)
			gpgga.parse(message)   
			lat = gpgga.latitude
			lon = gpgga.longitude
			print "Lattitude:" +str(lat)
			print "Longitude:" +str(lon)

	tmb.showinfo("GPS Coordinates", "Coordinates obtained Successfully")
	
except KeyboardInterrupt:
	pass