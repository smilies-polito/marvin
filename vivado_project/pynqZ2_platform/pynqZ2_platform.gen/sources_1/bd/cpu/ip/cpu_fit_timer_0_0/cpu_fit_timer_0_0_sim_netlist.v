// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2024.1 (lin64) Build 5076996 Wed May 22 18:36:09 MDT 2024
// Date        : Tue Jul  9 13:40:04 2024
// Host        : travelmate running 64-bit Ubuntu 22.04.4 LTS
// Command     : write_verilog -force -mode funcsim
//               /home/kike/Desktop/marvin/vivado_project/pynqZ2_platform/pynqZ2_platform.gen/sources_1/bd/cpu/ip/cpu_fit_timer_0_0/cpu_fit_timer_0_0_sim_netlist.v
// Design      : cpu_fit_timer_0_0
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xc7z020clg400-1
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CHECK_LICENSE_TYPE = "cpu_fit_timer_0_0,fit_timer,{}" *) (* downgradeipidentifiedwarnings = "yes" *) (* x_core_info = "fit_timer,Vivado 2024.1" *) 
(* NotValidForBitStream *)
module cpu_fit_timer_0_0
   (Clk,
    Rst,
    Interrupt);
  (* x_interface_info = "xilinx.com:signal:clock:1.0 CLK.Clk CLK" *) (* x_interface_parameter = "XIL_INTERFACENAME CLK.Clk, ASSOCIATED_RESET Rst, FREQ_HZ 100000000, FREQ_TOLERANCE_HZ 0, PHASE 0.0, CLK_DOMAIN cpu_processing_system7_0_0_FCLK_CLK0, INSERT_VIP 0" *) input Clk;
  (* x_interface_info = "xilinx.com:signal:reset:1.0 RST.Rst RST" *) (* x_interface_parameter = "XIL_INTERFACENAME RST.Rst, POLARITY ACTIVE_HIGH, INSERT_VIP 0" *) input Rst;
  (* x_interface_info = "xilinx.com:signal:interrupt:1.0 INTERRUPT.Interrupt INTERRUPT" *) (* x_interface_parameter = "XIL_INTERFACENAME INTERRUPT.Interrupt, SENSITIVITY LEVEL_HIGH, SUGGESTED_PRIORITY HIGH, PortWidth 1" *) output Interrupt;

  wire Clk;
  wire Interrupt;
  wire Rst;

  (* C_EXT_RESET_HIGH = "1" *) 
  (* C_FAMILY = "zynq" *) 
  (* C_INACCURACY = "0" *) 
  (* C_NO_CLOCKS = "6216" *) 
  cpu_fit_timer_0_0_FIT_timer U0
       (.Clk(Clk),
        .Interrupt(Interrupt),
        .Rst(Rst));
endmodule

(* ORIG_REF_NAME = "Divide_part" *) 
module cpu_fit_timer_0_0_Divide_part
   (loop_Bit,
    Rst_d1,
    CE,
    Rst_d1_reg_0,
    Rst_d1_reg_1,
    Clk,
    Rst,
    loop_Bit_0,
    loop_Bit_1);
  output loop_Bit;
  output Rst_d1;
  output CE;
  output Rst_d1_reg_0;
  output Rst_d1_reg_1;
  input Clk;
  input Rst;
  input loop_Bit_0;
  input loop_Bit_1;

  wire CE;
  wire Clk;
  wire \One_SRL16.SRL16E_I_i_1__0_n_0 ;
  wire Rst;
  wire Rst_d1;
  wire Rst_d1_reg_0;
  wire Rst_d1_reg_1;
  wire loop_Bit;
  wire loop_Bit_0;
  wire loop_Bit_1;

  LUT3 #(
    .INIT(8'h0E)) 
    \More_Than_Two.SRLC16E_1_i_2 
       (.I0(Rst_d1),
        .I1(loop_Bit_1),
        .I2(Rst),
        .O(Rst_d1_reg_1));
  (* box_type = "PRIMITIVE" *) 
  (* srl_bus_name = "U0/\\Using_SRL16s.SRL16s " *) 
  (* srl_name = "U0/\\Using_SRL16s.SRL16s[1].Divide_I/One_SRL16.SRL16E_I " *) 
  SRL16E #(
    .INIT(16'h0001),
    .IS_CLK_INVERTED(1'b0)) 
    \One_SRL16.SRL16E_I 
       (.A0(1'b1),
        .A1(1'b0),
        .A2(1'b1),
        .A3(1'b1),
        .CE(1'b1),
        .CLK(Clk),
        .D(\One_SRL16.SRL16E_I_i_1__0_n_0 ),
        .Q(loop_Bit));
  LUT3 #(
    .INIT(8'hFE)) 
    \One_SRL16.SRL16E_I_i_1 
       (.I0(loop_Bit),
        .I1(Rst),
        .I2(Rst_d1),
        .O(CE));
  (* SOFT_HLUTNM = "soft_lutpair0" *) 
  LUT3 #(
    .INIT(8'h0E)) 
    \One_SRL16.SRL16E_I_i_1__0 
       (.I0(Rst_d1),
        .I1(loop_Bit),
        .I2(Rst),
        .O(\One_SRL16.SRL16E_I_i_1__0_n_0 ));
  (* SOFT_HLUTNM = "soft_lutpair0" *) 
  LUT3 #(
    .INIT(8'h0E)) 
    \One_SRL16.SRL16E_I_i_2 
       (.I0(Rst_d1),
        .I1(loop_Bit_0),
        .I2(Rst),
        .O(Rst_d1_reg_0));
  FDRE #(
    .INIT(1'b0)) 
    Rst_d1_reg
       (.C(Clk),
        .CE(1'b1),
        .D(Rst),
        .Q(Rst_d1),
        .R(1'b0));
endmodule

(* ORIG_REF_NAME = "Divide_part" *) 
module cpu_fit_timer_0_0_Divide_part__parameterized0
   (loop_Bit,
    \Using_SRL16s.Clk_En_I_1 ,
    CE,
    CE_0,
    \One_SRL16.SRL16E_I_0 ,
    Clk,
    Rst,
    Rst_d1,
    loop_Bit_1);
  output loop_Bit;
  output \Using_SRL16s.Clk_En_I_1 ;
  output CE;
  input CE_0;
  input \One_SRL16.SRL16E_I_0 ;
  input Clk;
  input Rst;
  input Rst_d1;
  input loop_Bit_1;

  wire CE;
  wire CE_0;
  wire Clk;
  wire \One_SRL16.SRL16E_I_0 ;
  wire Rst;
  wire Rst_d1;
  wire \Using_SRL16s.Clk_En_I_1 ;
  wire loop_Bit;
  wire loop_Bit_1;
  wire \not_First.Clk_En_Out_i_i_1_n_0 ;
  wire \not_First.Out1 ;
  wire \not_First.Out1_i_1__0_n_0 ;

  LUT3 #(
    .INIT(8'hFE)) 
    \More_Than_Two.SRLC16E_1_i_1 
       (.I0(\Using_SRL16s.Clk_En_I_1 ),
        .I1(Rst),
        .I2(Rst_d1),
        .O(CE));
  (* box_type = "PRIMITIVE" *) 
  (* srl_bus_name = "U0/\\Using_SRL16s.SRL16s " *) 
  (* srl_name = "U0/\\Using_SRL16s.SRL16s[2].Divide_I/One_SRL16.SRL16E_I " *) 
  SRL16E #(
    .INIT(16'h0001),
    .IS_CLK_INVERTED(1'b0)) 
    \One_SRL16.SRL16E_I 
       (.A0(1'b1),
        .A1(1'b1),
        .A2(1'b0),
        .A3(1'b1),
        .CE(CE_0),
        .CLK(Clk),
        .D(\One_SRL16.SRL16E_I_0 ),
        .Q(loop_Bit));
  (* SOFT_HLUTNM = "soft_lutpair1" *) 
  LUT4 #(
    .INIT(16'h2F20)) 
    \not_First.Clk_En_Out_i_i_1 
       (.I0(loop_Bit_1),
        .I1(Rst),
        .I2(\not_First.Out1 ),
        .I3(\Using_SRL16s.Clk_En_I_1 ),
        .O(\not_First.Clk_En_Out_i_i_1_n_0 ));
  FDRE #(
    .INIT(1'b0)) 
    \not_First.Clk_En_Out_i_reg 
       (.C(Clk),
        .CE(1'b1),
        .D(\not_First.Clk_En_Out_i_i_1_n_0 ),
        .Q(\Using_SRL16s.Clk_En_I_1 ),
        .R(1'b0));
  (* SOFT_HLUTNM = "soft_lutpair1" *) 
  LUT2 #(
    .INIT(4'h2)) 
    \not_First.Out1_i_1__0 
       (.I0(loop_Bit),
        .I1(Rst),
        .O(\not_First.Out1_i_1__0_n_0 ));
  FDRE \not_First.Out1_reg 
       (.C(Clk),
        .CE(1'b1),
        .D(\not_First.Out1_i_1__0_n_0 ),
        .Q(\not_First.Out1 ),
        .R(1'b0));
endmodule

(* ORIG_REF_NAME = "Divide_part" *) 
module cpu_fit_timer_0_0_Divide_part__parameterized1
   (loop_Bit,
    Interrupt,
    CE,
    \More_Than_Two.SRLC16E_1_0 ,
    Clk,
    \Using_SRL16s.Clk_En_I_1 ,
    Rst);
  output loop_Bit;
  output Interrupt;
  input CE;
  input \More_Than_Two.SRLC16E_1_0 ;
  input Clk;
  input \Using_SRL16s.Clk_En_I_1 ;
  input Rst;

  wire CE;
  wire Clk;
  wire Interrupt;
  wire \More_Than_Two.SRL16E_n_i_1_n_0 ;
  wire \More_Than_Two.SRLC16E_1_0 ;
  wire \More_Than_Two.The_Rest[1].SRLC16E_I_i_1_n_0 ;
  wire \More_Than_Two.shifts_0 ;
  wire \More_Than_Two.shifts_1 ;
  wire Rst;
  wire \Using_SRL16s.Clk_En_I_1 ;
  wire loop_Bit;
  wire \not_First.Clk_En_Out_i_i_1__0_n_0 ;
  wire \not_First.Out1_i_1_n_0 ;
  wire \not_First.Out1_reg_n_0 ;
  wire \NLW_More_Than_Two.SRLC16E_1_Q_UNCONNECTED ;
  wire \NLW_More_Than_Two.The_Rest[1].SRLC16E_I_Q_UNCONNECTED ;

  (* box_type = "PRIMITIVE" *) 
  (* srl_bus_name = "U0/\\Using_SRL16s.SRL16s " *) 
  (* srl_name = "U0/\\Using_SRL16s.SRL16s[3].Divide_I/More_Than_Two.SRL16E_n " *) 
  SRL16E #(
    .INIT(16'h0000),
    .IS_CLK_INVERTED(1'b0)) 
    \More_Than_Two.SRL16E_n 
       (.A0(1'b0),
        .A1(1'b0),
        .A2(1'b1),
        .A3(1'b0),
        .CE(CE),
        .CLK(Clk),
        .D(\More_Than_Two.SRL16E_n_i_1_n_0 ),
        .Q(loop_Bit));
  (* SOFT_HLUTNM = "soft_lutpair2" *) 
  LUT2 #(
    .INIT(4'h2)) 
    \More_Than_Two.SRL16E_n_i_1 
       (.I0(\More_Than_Two.shifts_0 ),
        .I1(Rst),
        .O(\More_Than_Two.SRL16E_n_i_1_n_0 ));
  (* box_type = "PRIMITIVE" *) 
  SRLC16E #(
    .INIT(16'h0001),
    .IS_CLK_INVERTED(1'b0)) 
    \More_Than_Two.SRLC16E_1 
       (.A0(1'b1),
        .A1(1'b1),
        .A2(1'b1),
        .A3(1'b1),
        .CE(CE),
        .CLK(Clk),
        .D(\More_Than_Two.SRLC16E_1_0 ),
        .Q(\NLW_More_Than_Two.SRLC16E_1_Q_UNCONNECTED ),
        .Q15(\More_Than_Two.shifts_1 ));
  (* box_type = "PRIMITIVE" *) 
  SRLC16E #(
    .INIT(16'h0000),
    .IS_CLK_INVERTED(1'b0)) 
    \More_Than_Two.The_Rest[1].SRLC16E_I 
       (.A0(1'b1),
        .A1(1'b1),
        .A2(1'b1),
        .A3(1'b1),
        .CE(CE),
        .CLK(Clk),
        .D(\More_Than_Two.The_Rest[1].SRLC16E_I_i_1_n_0 ),
        .Q(\NLW_More_Than_Two.The_Rest[1].SRLC16E_I_Q_UNCONNECTED ),
        .Q15(\More_Than_Two.shifts_0 ));
  (* SOFT_HLUTNM = "soft_lutpair2" *) 
  LUT2 #(
    .INIT(4'h2)) 
    \More_Than_Two.The_Rest[1].SRLC16E_I_i_1 
       (.I0(\More_Than_Two.shifts_1 ),
        .I1(Rst),
        .O(\More_Than_Two.The_Rest[1].SRLC16E_I_i_1_n_0 ));
  LUT3 #(
    .INIT(8'hB8)) 
    \not_First.Clk_En_Out_i_i_1__0 
       (.I0(\Using_SRL16s.Clk_En_I_1 ),
        .I1(\not_First.Out1_reg_n_0 ),
        .I2(Interrupt),
        .O(\not_First.Clk_En_Out_i_i_1__0_n_0 ));
  FDRE #(
    .INIT(1'b0)) 
    \not_First.Clk_En_Out_i_reg 
       (.C(Clk),
        .CE(1'b1),
        .D(\not_First.Clk_En_Out_i_i_1__0_n_0 ),
        .Q(Interrupt),
        .R(1'b0));
  LUT2 #(
    .INIT(4'h2)) 
    \not_First.Out1_i_1 
       (.I0(loop_Bit),
        .I1(Rst),
        .O(\not_First.Out1_i_1_n_0 ));
  FDRE \not_First.Out1_reg 
       (.C(Clk),
        .CE(1'b1),
        .D(\not_First.Out1_i_1_n_0 ),
        .Q(\not_First.Out1_reg_n_0 ),
        .R(1'b0));
endmodule

(* C_EXT_RESET_HIGH = "1" *) (* C_FAMILY = "zynq" *) (* C_INACCURACY = "0" *) 
(* C_NO_CLOCKS = "6216" *) (* ORIG_REF_NAME = "FIT_timer" *) 
module cpu_fit_timer_0_0_FIT_timer
   (Clk,
    Rst,
    Interrupt);
  input Clk;
  input Rst;
  output Interrupt;

  wire CE;
  wire CE_0;
  wire Clk;
  wire Interrupt;
  wire Rst;
  wire Rst_d1;
  wire \Using_SRL16s.Clk_En_I_1 ;
  wire \Using_SRL16s.SRL16s[1].Divide_I_n_3 ;
  wire \Using_SRL16s.SRL16s[1].Divide_I_n_4 ;
  wire loop_Bit;
  wire loop_Bit_1;
  wire loop_Bit_2;

  cpu_fit_timer_0_0_Divide_part \Using_SRL16s.SRL16s[1].Divide_I 
       (.CE(CE),
        .Clk(Clk),
        .Rst(Rst),
        .Rst_d1(Rst_d1),
        .Rst_d1_reg_0(\Using_SRL16s.SRL16s[1].Divide_I_n_3 ),
        .Rst_d1_reg_1(\Using_SRL16s.SRL16s[1].Divide_I_n_4 ),
        .loop_Bit(loop_Bit),
        .loop_Bit_0(loop_Bit_1),
        .loop_Bit_1(loop_Bit_2));
  cpu_fit_timer_0_0_Divide_part__parameterized0 \Using_SRL16s.SRL16s[2].Divide_I 
       (.CE(CE_0),
        .CE_0(CE),
        .Clk(Clk),
        .\One_SRL16.SRL16E_I_0 (\Using_SRL16s.SRL16s[1].Divide_I_n_3 ),
        .Rst(Rst),
        .Rst_d1(Rst_d1),
        .\Using_SRL16s.Clk_En_I_1 (\Using_SRL16s.Clk_En_I_1 ),
        .loop_Bit(loop_Bit_1),
        .loop_Bit_1(loop_Bit));
  cpu_fit_timer_0_0_Divide_part__parameterized1 \Using_SRL16s.SRL16s[3].Divide_I 
       (.CE(CE_0),
        .Clk(Clk),
        .Interrupt(Interrupt),
        .\More_Than_Two.SRLC16E_1_0 (\Using_SRL16s.SRL16s[1].Divide_I_n_4 ),
        .Rst(Rst),
        .\Using_SRL16s.Clk_En_I_1 (\Using_SRL16s.Clk_En_I_1 ),
        .loop_Bit(loop_Bit_2));
endmodule
`ifndef GLBL
`define GLBL
`timescale  1 ps / 1 ps

module glbl ();

    parameter ROC_WIDTH = 100000;
    parameter TOC_WIDTH = 0;
    parameter GRES_WIDTH = 10000;
    parameter GRES_START = 10000;

//--------   STARTUP Globals --------------
    wire GSR;
    wire GTS;
    wire GWE;
    wire PRLD;
    wire GRESTORE;
    tri1 p_up_tmp;
    tri (weak1, strong0) PLL_LOCKG = p_up_tmp;

    wire PROGB_GLBL;
    wire CCLKO_GLBL;
    wire FCSBO_GLBL;
    wire [3:0] DO_GLBL;
    wire [3:0] DI_GLBL;
   
    reg GSR_int;
    reg GTS_int;
    reg PRLD_int;
    reg GRESTORE_int;

//--------   JTAG Globals --------------
    wire JTAG_TDO_GLBL;
    wire JTAG_TCK_GLBL;
    wire JTAG_TDI_GLBL;
    wire JTAG_TMS_GLBL;
    wire JTAG_TRST_GLBL;

    reg JTAG_CAPTURE_GLBL;
    reg JTAG_RESET_GLBL;
    reg JTAG_SHIFT_GLBL;
    reg JTAG_UPDATE_GLBL;
    reg JTAG_RUNTEST_GLBL;

    reg JTAG_SEL1_GLBL = 0;
    reg JTAG_SEL2_GLBL = 0 ;
    reg JTAG_SEL3_GLBL = 0;
    reg JTAG_SEL4_GLBL = 0;

    reg JTAG_USER_TDO1_GLBL = 1'bz;
    reg JTAG_USER_TDO2_GLBL = 1'bz;
    reg JTAG_USER_TDO3_GLBL = 1'bz;
    reg JTAG_USER_TDO4_GLBL = 1'bz;

    assign (strong1, weak0) GSR = GSR_int;
    assign (strong1, weak0) GTS = GTS_int;
    assign (weak1, weak0) PRLD = PRLD_int;
    assign (strong1, weak0) GRESTORE = GRESTORE_int;

    initial begin
	GSR_int = 1'b1;
	PRLD_int = 1'b1;
	#(ROC_WIDTH)
	GSR_int = 1'b0;
	PRLD_int = 1'b0;
    end

    initial begin
	GTS_int = 1'b1;
	#(TOC_WIDTH)
	GTS_int = 1'b0;
    end

    initial begin 
	GRESTORE_int = 1'b0;
	#(GRES_START);
	GRESTORE_int = 1'b1;
	#(GRES_WIDTH);
	GRESTORE_int = 1'b0;
    end

endmodule
`endif
