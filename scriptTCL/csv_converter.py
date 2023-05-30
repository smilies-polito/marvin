import csv
import sys


def main():
	num_of_fault = int(sys.argv[1])
	f = open("dataset.csv", "w")
	header = "num,reg,pos,loc,res"
	for i in range(168):
		header = header + "," + str(i)
	f.write(header + "\n")	
	
	res = open("/tools/Xilinx/Vitis/2022.2/dataset", "r")
	evs = open("out_bello", "r")

	for i in range(num_of_fault):
		row = str(i) + ","
		line_list = res.readline().strip().split(':')
		res_x = res.readline().strip()
		row = row + line_list[2].split()[0] + "," + line_list[3].split()[0] + "," + line_list[4] + "," + res_x
		
		evs.readline()
		evs.readline()
		for ev in range(168):
			if res_x != "crash/hangs":
				ev_c = evs.readline().strip().split(':')[1]
				row = row + "," + str(ev_c)
			else:
				row= row + "," + "-"	
		row = row + "\n"	
		f.write(row)

		
	res.close()
	f.close()

if __name__ == "__main__":
	main()
