# 
# Usage: To re-create this platform project launch xsct with below options.
# xsct /home/enrico/Desktop/project_bk/design_1_wrapper/platform.tcl
# 
# OR launch xsct and run below command.
# source /home/enrico/Desktop/project_bk/design_1_wrapper/platform.tcl
# 
# To create the platform in a different location, modify the -out option of "platform create" command.
# -out option specifies the output directory of the platform project.

platform create -name {design_1_wrapper}\
-hw {/home/enrico/Desktop/vivado_project/Hello_word_pynqZ2/design_1_wrapper.xsa}\
-out {/home/enrico/Desktop/project_bk}

platform write
domain create -name {freertos10_xilinx_ps7_cortexa9_0} -display-name {freertos10_xilinx_ps7_cortexa9_0} -os {freertos10_xilinx} -proc {ps7_cortexa9_0} -runtime {cpp} -arch {32-bit} -support-app {freertos_hello_world}
platform generate -domains 
platform active {design_1_wrapper}
domain active {zynq_fsbl}
domain active {freertos10_xilinx_ps7_cortexa9_0}
platform generate -quick
platform generate
platform clean
platform generate
platform generate
platform clean
platform generate
platform generate
platform generate
platform generate
platform generate
platform generate
platform generate
platform generate
platform generate
