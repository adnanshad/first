import serial
arduino = serial.Serial('COM6', 9600, timeout=.1)
while True:
	data = arduino.readline()
	if data:
	   print data
