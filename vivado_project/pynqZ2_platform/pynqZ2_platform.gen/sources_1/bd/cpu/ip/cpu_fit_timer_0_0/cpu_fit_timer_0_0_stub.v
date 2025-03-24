// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2024.1 (lin64) Build 5076996 Wed May 22 18:36:09 MDT 2024
// Date        : Tue Jul  9 13:40:04 2024
// Host        : travelmate running 64-bit Ubuntu 22.04.4 LTS
// Command     : write_verilog -force -mode synth_stub
//               /home/kike/Desktop/marvin/vivado_project/pynqZ2_platform/pynqZ2_platform.gen/sources_1/bd/cpu/ip/cpu_fit_timer_0_0/cpu_fit_timer_0_0_stub.v
// Design      : cpu_fit_timer_0_0
// Purpose     : Stub declaration of top-level module interface
// Device      : xc7z020clg400-1
// --------------------------------------------------------------------------------

// This empty module with port declaration file causes synthesis tools to infer a black box for IP.
// The synthesis directives are for Synopsys Synplify support to prevent IO buffer insertion.
// Please paste the declaration into a Verilog source file or add the file as an additional source.
(* x_core_info = "fit_timer,Vivado 2024.1" *)
module cpu_fit_timer_0_0(Clk, Rst, Interrupt)
/* synthesis syn_black_box black_box_pad_pin="Rst,Interrupt" */
/* synthesis syn_force_seq_prim="Clk" */;
  input Clk /* synthesis syn_isclock = 1 */;
  input Rst;
  output Interrupt;
endmodule
