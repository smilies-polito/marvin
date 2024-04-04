# Marvin A Micro Architectural Events Aware Real-Time Embedded System Fault Injector

**Target platform**: Xilinx Pynq Z2 with Zynq-7000 SoC\n
**Target real-time operating system**: FreeRTOS\n
**Benchmark**: Dijkstra, QuickSort, SHA (MiBench: https://vhosts.eecs.umich.edu/mibench/).\n

Fault-injection performed through debugger (breakpoint; flip a random bit; continue) with the novelty of the collection of the Micro-architectural features: Hardware Performance Counters (HPC) counting for events, like cache hit/miss, memory accesses, branches etc.

## Run the fault injection Tutorial

For running the fault injection, both file scriptTCL/script_filtered_pc_completed.py or scriptTCL/script_filtered_pc_completed_timer.py can be used the second one in addiction print on screen the temporal information about how much time is passed for each faulty campaign.\n
In the both case the FI campaign information need to be setted modifying the global variables in the script file: \n

init_task = "10050c" #ToCHANGE 
fin_task = "102e34"  #ToCHANGE
final_bp = "195"	#ToCHANGE	
fault_location = "pc" #ToCHANGE possible value memory or registers
fault = True		#ToCHANGE
num_of_sample = 1 #number of sample given a fault
num_of_run = 7
