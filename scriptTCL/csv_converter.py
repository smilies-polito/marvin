import csv
import sys

num_pc = 42 #all are 168

def main():
	num_of_fault = int(sys.argv[1])
	f = open("dataset.csv", "w")
	header = "num,reg,pos,loc,res"
	for i in range(num_pc):
		header = header + "," + str(i)
	f.write(header + "\n")	
	
	res = open("/tools/Xilinx/Vitis/2022.2/dataset", "r")
	evs = open("out_bello", "r")

	for i in range(num_of_fault):
		row = str(i) + ","
		line_list = res.readline().strip().split(':')
		res_x = res.readline().strip()
		row = row + line_list[2].split()[0] + "," + line_list[3].split()[0] + "," + line_list[4] + "," + res_x
		
		crash = False;
		cont_len = True;
		print(evs.readline())
		last = evs.readline()
		while "Fault" not in last:
			last = evs.readline()
		for ev in range(num_pc):
			if res_x != "crash/hangs":
				aus = evs.readline()
				print(aus)
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
	main()
