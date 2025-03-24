import serial

buond_rate = 115200
com_port = '/dev/ttyUSB1'

listener = serial.Serial(com_port, buond_rate)
f = open("faults", "a")
while 1:
	serial_out = listener.readline() 
	f.write(str(serial_out)[2:-3]+"\n")
	f.flush()
	print(str(serial_out)[2:-3])
	
f.close()	
