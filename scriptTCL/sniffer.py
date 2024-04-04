import serial

buond_rate = 115200
com_port = '/dev/ttyUSB1'

listener = serial.Serial(com_port, buond_rate)
f = open("out_bello", "w")
while 1:
	serial_out = listener.readline() 
	f.write(str(serial_out)[2:-3]+"\n")
	print(str(serial_out)[2:-3])
f.close()	
