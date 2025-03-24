# 
# Usage: To re-create this platform project launch xsct with below options.
# xsct /home/kike/Desktop/marvin/marvin/pynq_z2_bram_wrapper/platform.tcl
# 
# OR launch xsct and run below command.
# source /home/kike/Desktop/marvin/marvin/pynq_z2_bram_wrapper/platform.tcl
# 
# To create the platform in a different location, modify the -out option of "platform create" command.
# -out option specifies the output directory of the platform project.

platform create -name {pynq_z2_bram_wrapper}\
-hw {/home/kike/Desktop/marvin/vivado_project/pynq_z2_bram/pynq_z2_bram_wrapper.xsa}\
-out {/home/kike/Desktop/marvin/marvin}

platform write
domain create -name {freertos10_xilinx_ps7_cortexa9_0} -display-name {freertos10_xilinx_ps7_cortexa9_0} -os {freertos10_xilinx} -proc {ps7_cortexa9_0} -runtime {cpp} -arch {32-bit} -support-app {freertos_hello_world}
platform generate -domains 
platform active {pynq_z2_bram_wrapper}
domain active {zynq_fsbl}
domain active {freertos10_xilinx_ps7_cortexa9_0}
platform generate -quick
platform generate
platform generate
platform active {pynq_z2_bram_wrapper}
bsp reload
platform active {pynq_z2_bram_wrapper}
platform generate
platform generate
platform generate
platform active {pynq_z2_bram_wrapper}
bsp reload
domain active {zynq_fsbl}
bsp reload
platform generate -domains freertos10_xilinx_ps7_cortexa9_0 
platform generate -domains freertos10_xilinx_ps7_cortexa9_0 
platform generate -domains freertos10_xilinx_ps7_cortexa9_0 
platform generate -domains freertos10_xilinx_ps7_cortexa9_0 
platform generate -domains freertos10_xilinx_ps7_cortexa9_0 
platform generate -domains freertos10_xilinx_ps7_cortexa9_0 
platform generate -domains freertos10_xilinx_ps7_cortexa9_0 
platform generate -domains freertos10_xilinx_ps7_cortexa9_0 
platform generate -domains freertos10_xilinx_ps7_cortexa9_0 
platform generate -domains freertos10_xilinx_ps7_cortexa9_0 
platform generate -domains freertos10_xilinx_ps7_cortexa9_0 
platform generate
platform generate
platform generate
