# Marvin A Micro Architectural Events Aware Real-Time Embedded System Fault Injector

**Target platform**: Xilinx Pynq Z2 with Zynq-7000 SoC<br/>
**Target real-time operating system**: FreeRTOS<br/>
**Benchmark**: Dijkstra, QuickSort, SHA (MiBench: https://vhosts.eecs.umich.edu/mibench/).<br/>

Fault-injection performed through a debugger (breakpoint; flip a random bit; continue) with the novelty of the collection of the Micro-architectural features: Hardware Performance Counters (HPC) counting for events, like cache hit/miss, memory accesses, branches etc.

## Run the fault injection Tutorial
Before starting, we need to have the Xilinx 2022 toolchain working to open and compile the Hello_word_freeRTOS.

For running the fault injection, both files *scriptTCL/script_filtered_pc_completed.py* or *scriptTCL/script_filtered_pc_completed_timer.py* can be used the second one in addiction print on the screen the temporal information about how much time is passed for each faulty campaign.<br/>
In both case, the FI campaign information needs to be set, modifying the global variables in the script file: <br/>
<br/>
init_task = "10050c" #ToCHANGE <br/>
fin_task = "102e34"  #ToCHANGE<br/>
final_bp = "195"    #ToCHANGE   <br/>
fault_location = "pc" #ToCHANGE possible value memory or registers<br/>
fault = True        #ToCHANGE<br/>
num_of_sample = 1 #number of sample given a fault<br/>
num_of_run = 7<br/>
<br/>
The *init_task* and *fin_task* are the assembly Line of Code addresses on which the selected benchmark starts and finishes. The *final_bp* indicates the line of code on which the final breakpoint is set; don't modify it if the FreeRTOS code is not changed.<br/>
The *fault_location* to specify the injection location can be pc for the program counter only, memory for the address and registers for the CPU registers (special registers are not included).<br/>
The *fault* boolean variable (only present in the script with the timer), if set to true, runs the injection campaign; if set to false, run simply the benchmark to measure the time.<br/>
<br/>
The *num_of_sample* indicates the number of complete faulty execution for each fault; let it set to 1.<br/>
The *num_of_run* indicates the number of runs for each fault to collect all the micro-architectural events, with the Arm Cortex A9 keeping it equal to 7.<br/> 
<br/>
To execute the Fault Injection Campaign, connect the Pynq Z2 board and turn it on, then execute the python *scriptTCL/sniffer.py* file for collecting all the architectural events while the sniffer is running, start the FI script (*scriptTCL/script_filtered_pc_completed.py*) with the parameters the number of faults.<br/><br/>
At the end, to create the final dataset, run the Python script *scriptTCL/csv_converter.py*.
