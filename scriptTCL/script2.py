import pexpect
import time
import random
import subprocess
import sys

init_task = "10070c"
fin_task = "10085c"

#num_of_fault = 4 #number of different fault -> fault is a bit flipping and a bps
num_of_sample = 1 #number of sample given a fault
num_of_run = 28 #number of run for trace all the PC per a faul -> +9 if wanna trace event 4000 and 8000

def bitFlipping(hex_value, rand_pos):
	'''Convert hex in bin, perform a bit flipping in a random position and return the hex value'''
	scale = 16 ## equals to hexadecimal

	num_of_bits = 32

	bin_value = bin(int(hex_value, scale))[2:].zfill(num_of_bits)
	#print(bin_value)
	
	list_bin = list(bin_value)
	if list_bin[rand_pos] == "1":
		list_bin[rand_pos] = "0"
	else:
		list_bin[rand_pos] = "1"
	bin_str = "".join(list_bin)		
	#print("pos " + str(rand_pos) + "  " + bin_str)
	hex_res = hex(int(bin_str, 2))
	#print(hex_res)
	return hex_res

def fault_injection(xsct, reg_num, pos_flipping, crash):
	reg = "r" + str(reg_num)
	read_cmd = "rrd " + reg
	print("CMD: " + read_cmd)
	xsct.sendline(read_cmd)
	xsct.expect(".*" + reg + ": *")
	value = xsct.readline().decode()
	print(reg + ": " + str(value))
	try:
	
		flipped_value = bitFlipping(value, pos_flipping)
		print("bit Flip: " + flipped_value)
		xsct.sendline("rwr " + reg + " " + flipped_value)
	except:
		crash=True	
	
def main():
	#subprocess.run(["python3", "/home/enrico/Desktop/marvin/scriptTCL/sniffer.py"])
	num_of_fault = sys.argv[1]
	print("start simulation, num of fault: " + str(num_of_fault))
	f = open("dataset", "w")	#Output file
	
	xsct = pexpect.spawn("xsct")
	xsct.expect("xsct%")
	print(xsct.before.decode())   #init

	xsct.sendline("source /home/enrico/Desktop/marvin/scriptTCL/init.tcl")
	xsct.expect(".*Successfully downloaded.*")
	
	xsct.sendline("bpadd -file freertos_hello_world.c -line 192") #TO CHANGE the final bp
	xsct.expect(".*Breakpoint 0.*")
	
	for i in range(int(num_of_fault)):
		rand_bp_pos = random.randint(int(init_task, base=16), int(fin_task, base=16)) #bp on elf file address pay attention that here number are decimal, normal address rappresentation is hex   #TO CHANGE
		reg_flipping = random.randint(0, 12)
		pos_flipping = random.randint(0, 31)

		print(f"Generated a fault in reg: {reg_flipping} pos: {pos_flipping} at LOC: {rand_bp_pos}")		
		f.write(f"{i}: reg: {reg_flipping} pos: {pos_flipping} at LOC: {rand_bp_pos}\n")
		xsct.sendline("mwr 0x10200 " + str(i) )
		crash = False
		for y in range(num_of_run): #This cycle depends on the number of events that we wanna trace
			xsct.sendline("mwr 0x10000 0x0")
			xsct.sendline("mwr 0x10000 " + str(y) ) #for this program write the number of execution at address 10000 is fine
			rand_bp_cmd = "bpadd " + str(rand_bp_pos)
			xsct.sendline(rand_bp_cmd)

			xsct.sendline("con -addr 0x00100000")
			
			xsct.expect(".*Breakpoint.*")
			print("raggiunto bp e fare injection: " + rand_bp_cmd )
			fault_injection(xsct, reg_flipping, pos_flipping, crash)

			xsct.sendline("bpremove " + str(num_of_run*i+y+1))
			print("bpremove " + str(num_of_run*i+y+1))
			xsct.sendline("con")
			
			try:
				xsct.expect(".*Breakpoint.*")
			except:
				#need to save that a crash or loop stack occurs
				print("An timeout exception occurs")
				crash = True
			
		if crash == False:
			xsct.sendline("mrd 0x10100")
			xsct.expect(".*10100: *")
			value = xsct.readline().decode()
			print(value)
			print(len(value))
			print(value[len(value)-5])
			if value[len(value)-5] == '1':
				f.write("benign\n")
			else:
				f.write("SDC\n")
		else:
			f.write("crash/hangs\n")		
	f.close()

if __name__ == "__main__":
	main()	
