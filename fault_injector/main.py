import pexpect
import time
import random
import subprocess
import sys
import os

from utils import parse_args, random_in_intervals

#GLOBAL VARIABLES
final_bp = "424"		#TO BE CHANGED: it's the LOC of the final breakpoint inside the main.c
reg_used = []			#Array to store the registers used by each benchmark, target of the injection

fault_location = "" 	#set the fault location (possible value memory, registers, pc)
num_of_fault = 100 		#number of different fault -> fault is a bit flipping and a bps
num_of_sample = 1 		#number of sample given a fault
num_of_run = 7 			#number of run for trace all the architectural events per fault 
num_of_mf = 1 			#number of bitflip for each fault

def bitFlipping(hex_value, rand_pos):
	'''
		Takes as input the  an hexadecimal value and the random position for the bitflip
		Convert the hex value in binary, perform a bitflip in the random position
		Return: the reconverted hexadecimal value after the bitflip.
	'''
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
	

vet_read = [0]*3 #vet to store the read in case of multibit flipping
def fault_injection(xsct, reg_num, pos_flipping, rand_memory_pos, crash, fault_location, y, j):
	'''
		Function to perform the fault injection, takes as input the xsct terminal and all the info about the fault.
	'''

	read_cmd = ""
	pos = ""
	aus = ""

	#preapare the read command based on the different injection location
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
		xsct.sendline(read_cmd)		#send the read command to retrive the golden value
		if fault_location == "memory":	
			aus = pos[2:].upper()
		else:
			if reg_num[0] == 'r':
				aus = pos	
		#print(aus)
		xsct.expect(".*" + aus + ": *")
		value = xsct.readline().decode()
		print(pos + ": " + str(value))
		vet_read[j] = value 										#add the read value to the array
	try:
		flipped_value = bitFlipping(vet_read[j], pos_flipping)		#perform the bitflipping
		print("bit Flip: " + flipped_value)

		#send the write command to write the faulty value
		if fault_location == "memory":
			xsct.sendline("mwr " + rand_memory_pos + " " + flipped_value)
		else:
			xsct.sendline("rwr " + pos + " " + flipped_value)
	except:
		#In case of fail, classify the fault as a crash
		print("An timeout exception occurs")
		crash=True
	

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
	'''
		Function to set the injction address ranges and the target registers based on the benchmark
		Takes as input the benchmark.
		Return: the array of tuples with the ranges, the array with target registers and a progressive number to identify the benchmark
	'''
    if benchmark == "sha":
        return [("103414", "103414")], [0, 1, 2, 3], 1
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
        return [("1087cc", "108bf8")], [0, 1, 2, 3], 5
    if benchmark == "basicmath":
        return [("109fe0", "10a134")], [0, 1, 2, 3, 36, 37, 38], 6
    if benchmark == "all":
        return [("10b4a0", "1125c0")], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 7



def main(args):
	
	#delete older faults file from previous injection
	if os.path.exists("faults"):
		os.remove("faults")
		print("Faults file has been deleted.")
	
	#set all the campaign parameters taken from the args parser
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

	#takes injection parmeters based on the benchmark
	task_intervals, reg_used, num_bench = set_param(benchmark)
	print(init_task)
	print(fin_task)
	print(reg_used)
	
	f = open("faults", "a")			#Open the faults output file
	
	xsct = pexpect.spawn("xsct")	#spawn the xsct terminal
	xsct.expect("xsct%")			#wait the xsct terminal to be ready
	print(xsct.before.decode())

	xsct.sendline("source ./init.tcl")				#run the init.tcl script to prepare the board and flash the elf file
	xsct.expect(".*Successfully downloaded.*")		#wait until the board is flashed
	
	xsct.sendline("bpadd -file main.c -line " + final_bp) 	#set the final breakpoint, to detect when a faulty or golden execution is completed
	xsct.expect(".*Breakpoint 0.*")
	
	#if the injection campaign is not set to generate random input, open the input file, to retrive the faults to inject
	input_file = None 
	if not rand_input:	
		input_file = open("./input.csv")
		input_file.readline() #Readline to skip the header of the csv file

	num_bp_remove = 1	#set the number of breakpoint to remove

	#loop over the faults
	for i in range(int(num_of_fault)):
		
		rand_bp_pos = None
		rand_memory_pos = 0
		reg_flipping = 0
		vet_of_faults = []
		pos_flipping = 0
		data = None

		#if random input is true generate random position for the faulty breakpoint. otherwise read it from the input file
		if rand_input:
			rand_bp_pos = random_in_intervals(task_intervals) #bp on elf file,  here number are decimal
			#rand_bp_pos = rand_bp_pos - rand_bp_pos%4 #Da verificare allineamento dell'istruzione
		else:
			data = input_file.readline().strip().split(",")
			rand_bp_pos = data[3]
			
		
		#loop over the Multibit parameter, it's one in case of SBU
		for j in range(num_of_mf):
			
			#if random input is true generate random position for the bitflip. otherwise read it from the input file
			if rand_input:
				pos_flipping = random.randint(0, 31)
			else:
				pos_flipping = data[2+(3*j)]

			#generate or read the faulty location, based on the type (memory, registers, PC)
			if fault_location == "memory": #Memory
				
				if rand_input: #generate
					if benchmark == "all":	#in case of benchmark all set the operating system
						rand_memory_pos = hex(random_in_intervals([("11b028","1224f4"),("128018","1387c8")])) #for injection in OS data, segment .rodata .data .bss
					else:	#in others cases set target all the memory
						rand_memory_pos = hex(random_in_intervals([("100000","13dfd0")]))
					rand_memory_pos = hex(int(rand_memory_pos, 16) - (int(rand_memory_pos, 16)%4))	
				else: #read
					rand_memory_pos = data[1+(3*j)]
				print(f"Generated a fault in mem: {rand_memory_pos} pos: {pos_flipping} at LOC: {rand_bp_pos}")		
				f.write(f"{i}: mem: {rand_memory_pos} pos: {pos_flipping} at LOC: {rand_bp_pos}\n")
				vet_of_faults.append((rand_memory_pos, pos_flipping))

			elif fault_location == "pc":  #PC, In this case the location is always fixed, its the Program Counter
				
				reg_flipping = "pc"
				print(f"Generated a fault in reg: {reg_flipping} pos: {pos_flipping} at LOC: {rand_bp_pos}")		
				f.write(f"{i}: reg: {reg_flipping} pos: {pos_flipping} at LOC: {rand_bp_pos}\n")
				vet_of_faults.append((reg_flipping, pos_flipping))

			else:	#Registers
				
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
			
		
		
		#Starting the fault injection number i
		xsct.sendline("mwr 0x40000004 " + str(i) ) #Set to the injection number
		xsct.sendline("mwr 0x40000000 0x0")  #set the value 0 stand for the golden run
		
		if rand_input:
			xsct.sendline("mwr 0x40000014 0x0") #if the value of random seed is zero generate input on the board
		else:	
			random_seed = data[1+(num_of_mf*3)] #read the random seed in the input file
			print(random_seed)
			xsct.sendline("mwr 0x40000014 " + str(random_seed))	#set the random seed

		xsct.sendline("mwr 0x4000000c " + str(num_bench)) #set the num of benchmark

		#GOLDEN RUN
		xsct.sendline("con -addr 0x00100000")	#start the execution over the target board, from the bootstrap

		try:
			xsct.expect(".*Breakpoint.*")	#wait fot the golden run execution, this is the final bp
			
		except:
			#crash during the golden run
			print("An timeout exception occurs during the golden run")
			continue	#in case of crash during the golden run, skip this fault

		
		#START THE FAULT INJECTION RUNs
		crash = False

		#based on the collected features, set the number of run for each fault (7 for events, 1 for memory dump, 8 for all)
		num_of_run = 7
		feature_num = 0
		if(feature == "memory"):
			num_of_run = 1
		elif(feature == "all"):
			num_of_run = 8	

		#loop over the faulty run for each fault
		for y in range(num_of_run): 

			#based on the faulty run set the feature to collect
			if y == 7 or (y < 7 and feature == "memory"): # in case of memory or the 8th run the features is memory
				feature_num = 1
			if y < 7 and (feature == "all" or feature == "events"): # in case of events or all the first 7th are events
				feature_num = 0

			xsct.sendline("mwr 0x40000010 " + str(feature_num)) 	#set the type of feature
			xsct.sendline("mwr 0x40000000 0x0") 					#reset to zero the number of faulty run
			xsct.sendline("mwr 0x40000000 " + str(int(y+1)) ) 		#set the number of faulty run for the current fault
			
			#set the faulty breakpoint
			rand_bp_cmd = "bpadd " + str(rand_bp_pos)
			xsct.sendline(rand_bp_cmd)
			
			
			#START THE FAULTY RUN
			#xsct.sendline("rst")
			xsct.sendline("con -addr 0x00100000")
			#xsct.expect(".*unnin.*")
			

			xsct.expect(".*Breakpoint.*") #wait for the faulty brackpoint
			print("raggiunto bp e fare injection: " + rand_bp_cmd )
			
			#for each injection points inject the faults
			for j in range(num_of_mf):
				if fault_location == "memory":
					fault_injection(xsct, 0, vet_of_faults[j][1], vet_of_faults[j][0], crash, fault_location, y, j)
				else:	
					fault_injection(xsct, vet_of_faults[j][0], vet_of_faults[j][1], 0, crash, fault_location, y, j)

			#Remove the faulty breakpoint and set the value to remove the next
			xsct.sendline("bpremove " + str(num_bp_remove))
			print("bpremove " + str(num_bp_remove))
			num_bp_remove = num_bp_remove + 1
			
			xsct.sendline("con") #continue the execution after the breakpoint
			
			try:
				xsct.expect(".*Breakpoint.*")  #wait for the final breakpoint
				
			except:
				print("An timeout exception occurs") #classify the fault as a crash, if the benchmark execution never reaches the final bp
				crash = True
				break

			#in case of memory fault, reset the injection location to the original value, performing onother bitflip in the same position 
			if fault_location == "memory":
				for j in range(num_of_mf):
					fault_injection(xsct, 0, vet_of_faults[j][1], vet_of_faults[j][0], crash, fault_location, num_of_run, num_of_mf)		
		
		#In case of no crash faults classify the fault
		if crash == False:
			xsct.sendline("mrd 0x40000008")		#read the result of the comparison
			xsct.expect(".*40000008: *")
			value = xsct.readline().decode()
			
			if value[len(value)-5] == '1':		#if 1 classify the fault as a benign
				print("---Benign---")
				f.write("benign\n")
			else:
				print("---SDC---")				#if 0 classify tge fault as a SDC
				f.write("SDC\n")
		else:									#else classify the fault as Crash/Hangs
			if fault_location == "memory":
				fault_injection(xsct, reg_flipping, pos_flipping, rand_memory_pos, crash, fault_location, num_of_run, num_of_mf)
			print("---Crash/Hangs---")
			f.write("crash/hangs\n")
		f.flush()			
	f.close()

if __name__ == "__main__":
	main(args=parse_args())	
