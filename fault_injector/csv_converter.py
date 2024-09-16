import csv
import sys

from utils import parse_args, get_instraction

num_pc = 42 #all are 168



def main(args):
	num_of_fault = args.number_faults #number of faults
	benchmark = args.benchmark
	fault_location = args.injection_location
	num_multi = args.multibit 

	ds_name = "ds_" + str(benchmark) + "_" + str(fault_location) + "_" + str(num_of_fault) + "_" + str(num_multi) + ".csv"

	f = open(ds_name, "w")

	header = "num,"
	for i in range(num_multi):
		header = header + "reg,pos,loc,"
	header = header + "instraction" + ","
	header = header + "res"	
	for i in range(num_pc):
		header = header + "," + str(i)
	f.write(header + "\n")	
	
	res = open("./faults", "r")
	evs = open("./hpc", "r")

	for i in range(num_of_fault):
		row = str(i) + ","
		for y in range(num_multi):
			line_list = res.readline().strip().split(':')
			row = row + line_list[2].split()[0] + "," + line_list[3].split()[0] + "," + line_list[4] + ","
			row = row + f'"{get_instraction(int(line_list[4]))}"' +  ","
			
		res_x = res.readline().strip()
		row = row + res_x

		crash = False;
		cont_len = True;
		#print(evs.readline())
		last = evs.readline()
		while "Fault" not in last:
			last = evs.readline()
		for ev in range(num_pc):
			if res_x != "crash/hangs":
				aus = evs.readline()
				#print(aus)
				ev_c = aus.strip().split(':')
				if len(ev_c) != 2:
					cont_len = False
				else:		
					row = row + "," + str(ev_c[1])
			else:
				crash = True;
				row= row + "," + "-"	
		if cont_len:
			row = row + "\n"
			f.write(row)
		
				
		
	res.close()
	f.close()

if __name__ == "__main__":
	main(args=parse_args())
