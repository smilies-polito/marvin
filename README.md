# AI-based soft error detection for embedded applications.

1. Target platform: Xilinx Pynq Z2 with Zynq-7000 SoC
2. Target real-time operating system: FreeRTOS
3. Fault-injection performed through debugger (breakpoint; flip a random bit; continue) or Interrupt Service Routine (when it's time to injext an interrupt is generated; the ISR flips a random bit)
4. Micro-architectural features: Hardware Performance Counters (HPC) counting for events, like cache hit/miss, memory accesses, branches etc.
5. Other features: outputs of the run (application-specific)
5. Detection:
    * Generate a new set of inputs (different for each simulation)
    * Golden run (execution without faults) and collect HPC
    * Faulty run (execution with faults) and collect HPC
    * Compare the two


## TO DO
1. Write the PC on a file on board
2. Transfer the file from the board to the pc
