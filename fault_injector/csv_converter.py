import csv
import sys

from utils import parse_args, get_instraction

num_pc = 42 #all are 168



def main(args):
	#take fault injection configuration parameters
	num_of_fault = args.number_faults #number of faults
	benchmark = args.benchmark
	fault_location = args.injection_location
	num_multi = args.multibit 

	#Create an empty dataset, a csv file
	ds_name = "ds_" + str(benchmark) + "_" + str(fault_location) + "_" + str(num_of_fault) + "_" + str(num_multi) + ".csv"
	f = open(ds_name, "w")

	#Write the header line for the csv file
	header = "num,"
	for i in range(num_multi):
		header = header + "reg,pos,loc,"
	header = header + "input_seed" + ","	
	header = header + "instraction" + ","
	header = header + "res"
	for i in range(num_pc):
		header = header + "," + str(i)
	header = header + ",dump"  	
	f.write(header + "\n")	
	
	#Open the fault file
	res = open("./faults", "r")

	last = res.readline()
	#skip empty line
	while "Fault" not in last:
		last = res.readline()
	seed = 0
	#Cycle on fault
	for i in range(num_of_fault):
		print("processing " + str(i))
		cont_len = True;
		bk = []
		row_ev = ""

		#take seed	
		seed = res.readline().strip().split(':')[1]
		
		#take hpc value 
		for ev in range(num_pc):
			aus = res.readline()
			print(aus)
			ev_c = aus.strip().split(':')
			if len(ev_c) != 2:
				cont_len = False
				print("in brackckksdf")
				if len(ev_c) == 5:
					bk = ev_c
					
				break
				
			else:		
				row_ev = row_ev + "," + str(ev_c[1])
		print(row_ev)
		#check if there are also the memory dump feature and take it 
		memory_dump = ""
		read_line = res.readline()
		mem_feature = False
		if  "Memory Dump:" in read_line:
			print("memo dup")
			mem_feature = True
			while True:
				read_line = res.readline()
				if "reg:" not in read_line:
					memory_dump = memory_dump + read_line.strip()	
				else:
					break	

		print(read_line)

		row = str(i) + ","
		for y in range(num_multi):
			line_list = []
			if bk != []:
				line_list = bk 
			else:
				if y == 0:
					line_list = read_line.strip().split(':')
				else:	
					line_list = res.readline().strip().split(':')
			print(line_list)
					
			row = row + line_list[2].split()[0] + "," + line_list[3].split()[0] + "," + line_list[4] + ","
		
		row = row + seed + ","
		row = row + f'"{get_instraction(int(line_list[4]))}"' +  ","
			
		res_x = res.readline().strip()
		row = row + res_x

		
		while True:
			read_line = res.readline()
			if "Fault" not in read_line:
				memory_dump = memory_dump + read_line.strip()	
			else:
				break

		if res_x != "crash/hangs":
			row = row + row_ev
			if mem_feature:
				row = row + "," + memory_dump
			else:
				row = row + "," + "-" #add another one for memory dump	 
		else:
			for k in range(num_pc):
				row = row + "," + "-"
			row = row + "," + "-" #add another one for memory dump
		if cont_len:
			row = row + "\n"
			f.write(row)
			
	res.close()
	f.close()

if __name__ == "__main__":
	main(args=parse_args())
