import pexpect
import time
import random
import subprocess
import sys


#SHA: 10050c -> 102e34
#Dijkstra: 103098/103290 -> 103518
#qsort: 10b24c -> 10b84a /// 102f68 -> 102fc8
init_task = "102f68" #ToCHANGE 
fin_task = "1030f4"
final_bp = "195"
fault_location = "pc" #possible value memory or registers

#num_of_fault = 4 #number of different fault -> fault is a bit flipping and a bps
num_of_sample = 1 #number of sample given a fault
num_of_run = 7 #number of run for trace all the PC per a faul (28) -> +9 if wanna trace event 4000 and 8000 

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
	

def fault_injection(xsct, reg_num, pos_flipping, rand_memory_pos, crash):
	read_cmd = ""
	pos = ""
	if fault_location == "memory":
		pos = str(rand_memory_pos)
		read_cmd = "mrd " + str(rand_memory_pos)
	elif fault_location == "pc":
		pos = "pc"
		read_cmd = "rrd " + pos
	else:
		pos = "r" + str(reg_num)
		read_cmd = "rrd " + pos
		
	#print("CMD: " + read_cmd)
	xsct.sendline(read_cmd)
	aus = ""
	if fault_location == "memory":	
		aus = pos[2:].upper()
	else:
		aus = pos	
	#print(aus)
	xsct.expect(".*" + aus + ": *")
	value = xsct.readline().decode()
	print(pos + ": " + str(value))
	try:
		flipped_value = bitFlipping(value, pos_flipping)
		print("bit Flip: " + flipped_value)
		if fault_location == "memory":
			xsct.sendline("mwr " + rand_memory_pos + " " + flipped_value)
		else:
			xsct.sendline("rwr " + aus + " " + flipped_value)
	except:
		print("An timeout exception occurs")
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
	
	xsct.sendline("bpadd -file freertos_hello_world.c -line " + final_bp) #TO CHANGE the final bp
	xsct.expect(".*Breakpoint 0.*")
	
	num_bp_remove = 1
	for i in range(int(num_of_fault)):
		rand_bp_pos = random.randint(int(init_task, base=16), int(fin_task, base=16)) #bp on elf file address pay attention that here number are decimal, normal address rappresentation is hex   #TO CHANGE
		
		rand_memory_pos = 0
		reg_flipping = 0
		pos_flipping = random.randint(0, 31)
		if fault_location == "memory":
			rand_memory_pos = hex(random.randint(int("100000", base=16), int("15db8c", base=16)))
			
			rand_memory_pos = hex(int(rand_memory_pos, 16) - (int(rand_memory_pos, 16)%4))
			print(f"Generated a fault in mem: {rand_memory_pos} pos: {pos_flipping} at LOC: {rand_bp_pos}")		
			f.write(f"{i}: mem: {rand_memory_pos} pos: {pos_flipping} at LOC: {rand_bp_pos}\n")
		elif fault_location == "pc":
			reg_flipping = "pc" #Change to 12 to get also the crash
			print(f"Generated a fault in reg: {reg_flipping} pos: {pos_flipping} at LOC: {rand_bp_pos}")		
			f.write(f"{i}: reg: {reg_flipping} pos: {pos_flipping} at LOC: {rand_bp_pos}\n")
		else:
			reg_flipping = random.randint(0, 12) #Change to 12 to get also the crash
			print(f"Generated a fault in reg: {reg_flipping} pos: {pos_flipping} at LOC: {rand_bp_pos}")		
			f.write(f"{i}: reg: {reg_flipping} pos: {pos_flipping} at LOC: {rand_bp_pos}\n")
			
		xsct.sendline("mwr 0x10200 " + str(i) )
		crash = False
		for y in range(num_of_run): #This cycle depends on the number of events that we wanna trace
			xsct.sendline("mwr 0x10000 0x0")
			xsct.sendline("mwr 0x10000 " + str(y) ) #for this program write the number of execution at address 10000 is fine
			rand_bp_cmd = "bpadd " + str(rand_bp_pos)
			xsct.sendline(rand_bp_cmd)
			
			#xsct.sendline("rst")
			xsct.sendline("con -addr 0x00100000")
			#xsct.expect(".*unnin.*")
			
			xsct.expect(".*Breakpoint.*")
			print("raggiunto bp e fare injection: " + rand_bp_cmd )
			fault_injection(xsct, reg_flipping, pos_flipping, rand_memory_pos, crash)

			xsct.sendline("bpremove " + str(num_bp_remove))
			print("bpremove " + str(num_bp_remove))
			num_bp_remove = num_bp_remove + 1
			xsct.sendline("con")
			
			try:
				xsct.expect(".*Breakpoint.*")
				
			except:
				#need to save that a crash or loop stack occurs
				print("An timeout exception occurs")
				crash = True
				break
			if fault_location == "memory":
				fault_injection(xsct, reg_flipping, pos_flipping, rand_memory_pos, crash)		
			
		if crash == False:
			xsct.sendline("mrd 0x10100")
			xsct.expect(".*10100: *")
			value = xsct.readline().decode()
			
			if value[len(value)-5] == '1':
				print("---Benign---")
				f.write("benign\n")
			else:
				print("---SDC---")
				f.write("SDC\n")
		else:
			if fault_location == "memory":
				fault_injection(xsct, reg_flipping, pos_flipping, rand_memory_pos, crash)
			print("---Crash/Hangs---")
			f.write("crash/hangs\n")		
	f.close()

if __name__ == "__main__":
	main()	
