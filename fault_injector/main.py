import pexpect
import time
import random
import subprocess
import sys
import os


from utils import parse_args, random_in_intervals


#SHA: 		100944 -> 103290
#DIJKSTRA   109688 -> 109b38
#QSORT 		108ddc -> 108f64
#SEARCH		1004f8 -> 1006b8
#RIJNDEAL	1035d0 -> 108720 
#BASICMATH	109fe0 -> 10a134 d0,d16,d17,d18
#ALL 		SHA, DIJKSTRA, QSORT

#SHA: 1004f8-10050c -> 102e34-102e44    r0 a r3 + r11
#Dijkstra: 103098/103290 -> 103518
#qsort: 10b24c -> 10b84a /// 102f68 -> 102fc8
init_task = "" #ToCHANGE 
fin_task = ""
final_bp = "381"
reg_used = []

fault_location = "" #possible value memory, registers, pc
num_of_fault = 100 #number of different fault -> fault is a bit flipping and a bps
num_of_sample = 1 #number of sample given a fault
num_of_run = 7 #number of run for trace all the PC per a faul (28) -> +9 if wanna trace event 4000 and 8000 
num_of_mf = 1 

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
	
vet_read = [0]*3
def fault_injection(xsct, reg_num, pos_flipping, rand_memory_pos, crash, fault_location, y, j):
	read_cmd = ""
	pos = ""
	aus = ""
	if fault_location == "memory":
		pos = str(rand_memory_pos)
		read_cmd = "mrd " + str(rand_memory_pos)
	if fault_location == "pc":
		pos = "pc"
		read_cmd = "rrd " + pos
	if fault_location == "registers":
		#pos = "r" + str(reg_num)
		if reg_num[0] == 'd':
			
			if pos_flipping > 31:
				pos = "vfp q" +str(int(int(reg_num[1:])/2)) + " " + reg_num + " s" + str((int(reg_num[1:])*2)+1)
				aus = "s" + str((int(reg_num[1:])*2)+1)
			else:
				pos = "vfp q" +str(int(int(reg_num[1:])/2)) + " " + reg_num + " s" + str(int(reg_num[1:])*2)	
				aus = "s" + str(int(reg_num[1:])*2)
			pos_flipping = pos_flipping%32	
		else:
			pos = reg_num	

		read_cmd = "rrd " + pos
	if y == 0:	
		print("CMD: " + read_cmd)
		xsct.sendline(read_cmd)
		if fault_location == "memory":	
			aus = pos[2:].upper()
		else:
			if reg_num[0] == 'r':
				aus = pos	
		#print(aus)
		xsct.expect(".*" + aus + ": *")
		value = xsct.readline().decode()
		print(pos + ": " + str(value))
		vet_read[j] = value
	try:
		flipped_value = bitFlipping(vet_read[j], pos_flipping)
		print("bit Flip: " + flipped_value)
		if fault_location == "memory":
			xsct.sendline("mwr " + rand_memory_pos + " " + flipped_value)
		else:
			xsct.sendline("rwr " + pos + " " + flipped_value)
	except:
		print("An timeout exception occurs")
		crash=True
	

#SHA: 		100944 -> 103290
#DIJKSTRA   109688 -> 109b38
#QSORT 		108ddc -> 108f64
#SEARCH		1004f8 -> 1006b8
#RIJNDEAL	1035d0 -> 108720 
#BASICMATH	109fe0 -> 10a134 d0,d16,d17,d18
#ALL 		SHA, DIJKSTRA, QSORT 

#MAIN		10a148 -> 10a9a4
#XIL_PRINTF
#TaskGetHandler	10b4a0
#xTaskGetCurrentTaskHandle 10b65c
#and others task funct
#vTaskStartScheduler 10bf1c
#vTaskEnd Scheduler 10c068 -> 10c0e0
#other task funct
#vTaskPlaceOnEventList 10c678 -> 10c77c
#other timer/task/scheduler funct
#free heap 10e618 -> 10e8d4
#interrupr handler function and queue
#switch handler 110a20

def set_param(benchmark):
    if benchmark == "sha":
        return [("100974", "103288")], [0, 1, 2, 3], 1
		#return [("100944", "103290")], [0, 1, 2, 3], 1
    if benchmark == "dijkstra":
        return [("109734", "1097ec"), ("109820", "1098bc"), ("109918", "109bb0")], [0, 1, 2, 3], 2
    if benchmark == "quicksort":
        return [("108e64", "108e88")], [0, 1, 2, 3], 3
		# return [("108e3c", "108e60"), ("108e88", "108f9c")], [0, 1, 2, 3], 3 
        # return [("108e28", "108fa8")], [0, 1, 2, 3], 3
    if benchmark == "stringsearch":
        return [("1004f8", "1006b8")], [0, 1, 2, 3], 4  # fino a qui i bench sono apposto, da sistemare da rijndeal in poi
    if benchmark == "rijndeal":
        return [("1035d0", "108720")], [0, 1, 2, 3], 5
    if benchmark == "basicmath":
        return [("109fe0", "10a134")], [0, 1, 2, 3, 36, 37, 38], 6
    if benchmark == "all":
        return [("10b4a0", "1125c0")], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 7



def main(args):
	#this if must be commented if the fi is launched by the automizer
	if os.path.exists("faults"):
		os.remove("faults")
		print("Faults file has been deleted.")
	
	num_of_fault = args.number_faults #number of faults
	rand_input = not args.import_input
	benchmark = args.benchmark
	fault_location = args.injection_location
	num_of_mf = args.multibit 
	feature = args.feature

	print("Start Injection Campaign")
	print("-")
	print("-Number of fault: " + str(num_of_fault))
	print("-Random: " + str(rand_input))
	print("-Benchmark: " + benchmark)
	print("-Injection Location: " + fault_location)
	print("-Bit-flipping per Fault: " + str(num_of_mf))
	print("")

	task_intervals, reg_used, num_bench = set_param(benchmark)
	print(init_task)
	print(fin_task)
	print(reg_used)
	f = open("faults", "a")	#Output file
	
	xsct = pexpect.spawn("xsct")
	xsct.expect("xsct%")
	print(xsct.before.decode())   #init

	xsct.sendline("source ./init.tcl")
	xsct.expect(".*Successfully downloaded.*")
	
	xsct.sendline("bpadd -file main.c -line " + final_bp) #TO CHANGE the final bp
	xsct.expect(".*Breakpoint 0.*")
	
	input_file = None 
	if not rand_input:
		input_file = open("./input.csv")
		input_file.readline() #Readline to skip the header of the csv file

	num_bp_remove = 1

	for i in range(int(num_of_fault)):
		rand_bp_pos = None
		rand_memory_pos = 0
		reg_flipping = 0
		vet_of_faults = []
		pos_flipping = 0
		data = None

		if rand_input:
			rand_bp_pos = random_in_intervals(task_intervals) #bp on elf file address pay attention that here number are decimal, normal address rappresentation is hex   #TO CHANGE
			#rand_bp_pos = rand_bp_pos - rand_bp_pos%4 #Da verificare allineamento dell'istruzione
		else:
			data = input_file.readline().strip().split(",")
			rand_bp_pos = data[3]
			
		
		
		for j in range(num_of_mf):
			if rand_input:
				pos_flipping = random.randint(0, 31)
			else:
				pos_flipping = data[2+(3*j)]
					
			if fault_location == "memory":
				if rand_input:
					if benchmark == "all":
						rand_memory_pos = hex(random_in_intervals([("11b028","1224f4"),("128018","1387c8")])) #for injection in OS data, segment .rodata .data .bss
					else:	
						rand_memory_pos = hex(random_in_intervals([("100000","13dfd0")]))
					rand_memory_pos = hex(int(rand_memory_pos, 16) - (int(rand_memory_pos, 16)%4))
				else:
					rand_memory_pos = data[1+(3*j)]
				print(f"Generated a fault in mem: {rand_memory_pos} pos: {pos_flipping} at LOC: {rand_bp_pos}")		
				f.write(f"{i}: mem: {rand_memory_pos} pos: {pos_flipping} at LOC: {rand_bp_pos}\n")
				vet_of_faults.append((rand_memory_pos, pos_flipping))
			elif fault_location == "pc":
				reg_flipping = "pc" #Change to 12 to get also the crash
				print(f"Generated a fault in reg: {reg_flipping} pos: {pos_flipping} at LOC: {rand_bp_pos}")		
				f.write(f"{i}: reg: {reg_flipping} pos: {pos_flipping} at LOC: {rand_bp_pos}\n")
				vet_of_faults.append((reg_flipping, pos_flipping))
			else:
				if rand_input:
					reg_flipping = reg_used[random.randint(0,len(reg_used)-1)] #Change to 12 to get also the crash
					if reg_flipping >= 20:
						reg_flipping = "d" + str(reg_flipping-20)
						pos_flipping = random.randint(0,63)
					else:
						reg_flipping = "r" + str(reg_flipping)
				else:
					reg_flipping = data[1+(3*j)]			
				print(f"Generated a fault in reg: {reg_flipping} pos: {pos_flipping} at LOC: {rand_bp_pos}")		
				f.write(f"{i}: reg: {reg_flipping} pos: {pos_flipping} at LOC: {rand_bp_pos}\n")
				vet_of_faults.append((reg_flipping, pos_flipping))
			
		
		#random_seed = random.randint(0,100)
		#Starting the fault injection number i
		xsct.sendline("mwr 0x40000004 " + str(i) )
		xsct.sendline("mwr 0x40000000 0x0")  #the value 0 stand for the golden run
		if rand_input:
			xsct.sendline("mwr 0x40000014 0x0") #if the value of random seed is zero generate input on the board
		else:	
			random_seed = data[1+(num_of_mf*3)]
			print(random_seed)
			xsct.sendline("mwr 0x40000014 " + str(random_seed))	
		xsct.sendline("mwr 0x4000000c " + str(num_bench))
		xsct.sendline("con -addr 0x00100000")

		try:
			xsct.expect(".*Breakpoint.*")
			
		except:
			#crash during the golden run
			print("An timeout exception occurs during the golden run")
			continue
		crash = False
		num_of_run = 7
		feature_num = 0
		if(feature == "memory"):
			num_of_run = 1
		elif(feature == "all"):
			num_of_run = 8	
		for y in range(num_of_run): #This inner cycle depends on the number of events that we wanna trace
			if y == 7 or (y < 7 and feature == "memory"):
				feature_num = 1
			if y < 7 and (feature == "all" or feature == "events"):
				feature_num = 0
			xsct.sendline("mwr 0x40000010 " + str(feature_num))
			xsct.sendline("mwr 0x40000000 0x0")
			xsct.sendline("mwr 0x40000000 " + str(int(y+1)) ) #for this program write the number of execution at address 10000 is fine
			rand_bp_cmd = "bpadd " + str(rand_bp_pos)
			xsct.sendline(rand_bp_cmd)
			
			#xsct.sendline("rst")
			xsct.sendline("con -addr 0x00100000")
			#xsct.expect(".*unnin.*")
			
			xsct.expect(".*Breakpoint.*")
			print("raggiunto bp e fare injection: " + rand_bp_cmd )
			for j in range(num_of_mf):
				if fault_location == "memory":
					fault_injection(xsct, 0, vet_of_faults[j][1], vet_of_faults[j][0], crash, fault_location, y, j)
				else:	
					fault_injection(xsct, vet_of_faults[j][0], vet_of_faults[j][1], 0, crash, fault_location, y, j)

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
				for j in range(num_of_mf):
					fault_injection(xsct, 0, vet_of_faults[j][1], vet_of_faults[j][0], crash, fault_location, num_of_run, num_of_mf)		
			
		if crash == False:
			xsct.sendline("mrd 0x40000008")
			xsct.expect(".*40000008: *")
			value = xsct.readline().decode()
			
			if value[len(value)-5] == '1':
				print("---Benign---")
				f.write("benign\n")
			else:
				print("---SDC---")
				f.write("SDC\n")
		else:
			if fault_location == "memory":
				fault_injection(xsct, reg_flipping, pos_flipping, rand_memory_pos, crash, fault_location, num_of_run, num_of_mf)
			print("---Crash/Hangs---")
			f.write("crash/hangs\n")
		f.flush()			
	f.close()

if __name__ == "__main__":
	main(args=parse_args())	
