import pexpect
import time
import random

#init: 0x00100660
#fin:  0x001007b0


def bitFlipping(hex_value):
	'''Convert hex in bin, perform a bit flipping in a random position and return the hex value'''
	scale = 16 ## equals to hexadecimal

	num_of_bits = 32

	bin_value = bin(int(hex_value, scale))[2:].zfill(num_of_bits)
	#print(bin_value)
	rand_pos = random.randint(0, 31)
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
	
def read_pmu_register(xsct, i, f):
	'''read and save in a file all the PMU register, save the file where the python script is executed'''
	xsct.sendline("rrd cp15 c9")
	xsct.expect(".*pmcr: *")
	value = "      pmcr: "
	value = value + xsct.readline().decode()
	value = value + xsct.readline().decode()
	value = value + xsct.readline().decode()
	value = value + xsct.readline().decode()
	print("PMU Register:\n" + value)
	
	f.write(value)
	
		

def main():
	f = open("PMU_register", "w")
	xsct = pexpect.spawn("xsct")
	xsct.expect("xsct%")
	print(xsct.before.decode())   #init


	xsct.sendline("source /home/enrico/Desktop/marvin/scriptTCL/init.tcl")
	xsct.expect(".*Successfully downloaded.*")
	#print(xsct.after.decode())  #%xsct

	xsct.sendline("bpadd -file freertos_hello_world.c -line 155") #TO CHANGE
	xsct.expect(".*Breakpoint 0.*")
	#print(xsct.after.decode())


	for i in range(10):
	    print("range n: ", i)
	    f.write(str(i) + "\n")
	    #rand_bp_cmd = "bpadd -file freertos_hello_world.c -line " + str(random.randint(93, 113)) #bp on LOC
	    rand_bp_cmd = "bpadd " + str (random.randint(1050208, 1050544)) #bp on elf file address pay attention that here number are decimal, normal address rappresentation is hex   #TO CHANGE
	    xsct.sendline(rand_bp_cmd)
	    #xsct.expect(".*Breakpoint " + str(i+1) + ".*")
	    #print(xsct.after.decode())
	    
	    xsct.sendline("con -addr 0x00100000")
	    #xsct.expect("xsct%")  #not needed
	    #xsct.sendline("state")
	    xsct.expect(".*Breakpoint.*")
	    #print(xsct.after.decode())
	    print("raggiunto bp e fare injection: " + rand_bp_cmd )
	    
	    num = random.randint(0, 15)
	    
	    reg = "r"
	    if num == 13:
	    	reg = "sp"
	    elif num == 14:
	    	reg = "lr"
	    elif num == 15:
	    	reg = "pc"
	    else:		 	
	    	reg = "r" + str(num)
	    read_cmd = "rrd " + reg
	    print("CMD: " + read_cmd)
	    xsct.sendline(read_cmd)
	    xsct.expect(".*" + reg + ": *")
	    value = xsct.readline().decode()
	    print(reg + ": " + str(value))
	    flipped_value = bitFlipping(value)
	    print("bit Flip: " + flipped_value)
	    xsct.sendline("rwr " + reg + " " + flipped_value)
	    
	    xsct.sendline("bpremove " + str(i+1))
	    xsct.sendline("con")
	    crash = False
	    try:
	    	xsct.expect(".*Breakpoint.*")
	    except:
	    	#need to save that a crash or loop stack occurs
	    	print("An timeout exception occurs")
	    	crash = True
	    	f.write("crash/hangs\n")
	    if crash == False:
	    	#read compare and save output
	    	f.write("SDC/benign\n")
	    #read_pmu_register(xsct, i, f)
	    
	f.close()	    
	    
   
   
if __name__ == "__main__":
	main()

