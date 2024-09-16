// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2024.1 (lin64) Build 5076996 Wed May 22 18:36:09 MDT 2024
// Date        : Mon Jul 15 13:38:33 2024
// Host        : travelmate running 64-bit Ubuntu 22.04.4 LTS
// Command     : write_verilog -force -mode funcsim
//               /home/kike/Desktop/marvin/vivado_project/pynq_z2_bram/pynq_z2_bram.gen/sources_1/bd/pynq_z2_bram/ip/pynq_z2_bram_axi_bram_ctrl_0_bram_0/pynq_z2_bram_axi_bram_ctrl_0_bram_0_sim_netlist.v
// Design      : pynq_z2_bram_axi_bram_ctrl_0_bram_0
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xc7z020clg400-1
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CHECK_LICENSE_TYPE = "pynq_z2_bram_axi_bram_ctrl_0_bram_0,blk_mem_gen_v8_4_8,{}" *) (* downgradeipidentifiedwarnings = "yes" *) (* x_core_info = "blk_mem_gen_v8_4_8,Vivado 2024.1" *) 
(* NotValidForBitStream *)
module pynq_z2_bram_axi_bram_ctrl_0_bram_0
   (clka,
    rsta,
    ena,
    wea,
    addra,
    dina,
    douta,
    rsta_busy);
  (* x_interface_info = "xilinx.com:interface:bram:1.0 BRAM_PORTA CLK" *) (* x_interface_parameter = "XIL_INTERFACENAME BRAM_PORTA, MEM_ADDRESS_MODE BYTE_ADDRESS, MEM_SIZE 8192, MEM_WIDTH 32, MEM_ECC NONE, MASTER_TYPE BRAM_CTRL, READ_WRITE_MODE READ_WRITE, READ_LATENCY 1" *) input clka;
  (* x_interface_info = "xilinx.com:interface:bram:1.0 BRAM_PORTA RST" *) input rsta;
  (* x_interface_info = "xilinx.com:interface:bram:1.0 BRAM_PORTA EN" *) input ena;
  (* x_interface_info = "xilinx.com:interface:bram:1.0 BRAM_PORTA WE" *) input [3:0]wea;
  (* x_interface_info = "xilinx.com:interface:bram:1.0 BRAM_PORTA ADDR" *) input [31:0]addra;
  (* x_interface_info = "xilinx.com:interface:bram:1.0 BRAM_PORTA DIN" *) input [31:0]dina;
  (* x_interface_info = "xilinx.com:interface:bram:1.0 BRAM_PORTA DOUT" *) output [31:0]douta;
  output rsta_busy;

  wire [31:0]addra;
  wire clka;
  wire [31:0]dina;
  wire [31:0]douta;
  wire ena;
  wire rsta;
  wire rsta_busy;
  wire [3:0]wea;
  wire NLW_U0_dbiterr_UNCONNECTED;
  wire NLW_U0_rstb_busy_UNCONNECTED;
  wire NLW_U0_s_axi_arready_UNCONNECTED;
  wire NLW_U0_s_axi_awready_UNCONNECTED;
  wire NLW_U0_s_axi_bvalid_UNCONNECTED;
  wire NLW_U0_s_axi_dbiterr_UNCONNECTED;
  wire NLW_U0_s_axi_rlast_UNCONNECTED;
  wire NLW_U0_s_axi_rvalid_UNCONNECTED;
  wire NLW_U0_s_axi_sbiterr_UNCONNECTED;
  wire NLW_U0_s_axi_wready_UNCONNECTED;
  wire NLW_U0_sbiterr_UNCONNECTED;
  wire [31:0]NLW_U0_doutb_UNCONNECTED;
  wire [31:0]NLW_U0_rdaddrecc_UNCONNECTED;
  wire [3:0]NLW_U0_s_axi_bid_UNCONNECTED;
  wire [1:0]NLW_U0_s_axi_bresp_UNCONNECTED;
  wire [31:0]NLW_U0_s_axi_rdaddrecc_UNCONNECTED;
  wire [31:0]NLW_U0_s_axi_rdata_UNCONNECTED;
  wire [3:0]NLW_U0_s_axi_rid_UNCONNECTED;
  wire [1:0]NLW_U0_s_axi_rresp_UNCONNECTED;

  (* C_ADDRA_WIDTH = "32" *) 
  (* C_ADDRB_WIDTH = "32" *) 
  (* C_ALGORITHM = "1" *) 
  (* C_AXI_ID_WIDTH = "4" *) 
  (* C_AXI_SLAVE_TYPE = "0" *) 
  (* C_AXI_TYPE = "1" *) 
  (* C_BYTE_SIZE = "8" *) 
  (* C_COMMON_CLK = "0" *) 
  (* C_COUNT_18K_BRAM = "0" *) 
  (* C_COUNT_36K_BRAM = "2" *) 
  (* C_CTRL_ECC_ALGO = "NONE" *) 
  (* C_DEFAULT_DATA = "0" *) 
  (* C_DISABLE_WARN_BHV_COLL = "0" *) 
  (* C_DISABLE_WARN_BHV_RANGE = "0" *) 
  (* C_ELABORATION_DIR = "./" *) 
  (* C_ENABLE_32BIT_ADDRESS = "1" *) 
  (* C_EN_DEEPSLEEP_PIN = "0" *) 
  (* C_EN_ECC_PIPE = "0" *) 
  (* C_EN_RDADDRA_CHG = "0" *) 
  (* C_EN_RDADDRB_CHG = "0" *) 
  (* C_EN_SAFETY_CKT = "1" *) 
  (* C_EN_SHUTDOWN_PIN = "0" *) 
  (* C_EN_SLEEP_PIN = "0" *) 
  (* C_EST_POWER_SUMMARY = "Estimated Power for IP     :     5.3746 mW" *) 
  (* C_FAMILY = "zynq" *) 
  (* C_HAS_AXI_ID = "0" *) 
  (* C_HAS_ENA = "1" *) 
  (* C_HAS_ENB = "0" *) 
  (* C_HAS_INJECTERR = "0" *) 
  (* C_HAS_MEM_OUTPUT_REGS_A = "0" *) 
  (* C_HAS_MEM_OUTPUT_REGS_B = "0" *) 
  (* C_HAS_MUX_OUTPUT_REGS_A = "0" *) 
  (* C_HAS_MUX_OUTPUT_REGS_B = "0" *) 
  (* C_HAS_REGCEA = "0" *) 
  (* C_HAS_REGCEB = "0" *) 
  (* C_HAS_RSTA = "1" *) 
  (* C_HAS_RSTB = "0" *) 
  (* C_HAS_SOFTECC_INPUT_REGS_A = "0" *) 
  (* C_HAS_SOFTECC_OUTPUT_REGS_B = "0" *) 
  (* C_INITA_VAL = "0" *) 
  (* C_INITB_VAL = "0" *) 
  (* C_INIT_FILE = "NONE" *) 
  (* C_INIT_FILE_NAME = "no_coe_file_loaded" *) 
  (* C_INTERFACE_TYPE = "0" *) 
  (* C_LOAD_INIT_FILE = "0" *) 
  (* C_MEM_TYPE = "0" *) 
  (* C_MUX_PIPELINE_STAGES = "0" *) 
  (* C_PRIM_TYPE = "1" *) 
  (* C_READ_DEPTH_A = "2048" *) 
  (* C_READ_DEPTH_B = "2048" *) 
  (* C_READ_LATENCY_A = "1" *) 
  (* C_READ_LATENCY_B = "1" *) 
  (* C_READ_WIDTH_A = "32" *) 
  (* C_READ_WIDTH_B = "32" *) 
  (* C_RSTRAM_A = "0" *) 
  (* C_RSTRAM_B = "0" *) 
  (* C_RST_PRIORITY_A = "CE" *) 
  (* C_RST_PRIORITY_B = "CE" *) 
  (* C_SIM_COLLISION_CHECK = "ALL" *) 
  (* C_USE_BRAM_BLOCK = "1" *) 
  (* C_USE_BYTE_WEA = "1" *) 
  (* C_USE_BYTE_WEB = "1" *) 
  (* C_USE_DEFAULT_DATA = "0" *) 
  (* C_USE_ECC = "0" *) 
  (* C_USE_SOFTECC = "0" *) 
  (* C_USE_URAM = "0" *) 
  (* C_WEA_WIDTH = "4" *) 
  (* C_WEB_WIDTH = "4" *) 
  (* C_WRITE_DEPTH_A = "2048" *) 
  (* C_WRITE_DEPTH_B = "2048" *) 
  (* C_WRITE_MODE_A = "WRITE_FIRST" *) 
  (* C_WRITE_MODE_B = "WRITE_FIRST" *) 
  (* C_WRITE_WIDTH_A = "32" *) 
  (* C_WRITE_WIDTH_B = "32" *) 
  (* C_XDEVICEFAMILY = "zynq" *) 
  (* downgradeipidentifiedwarnings = "yes" *) 
  (* is_du_within_envelope = "true" *) 
  pynq_z2_bram_axi_bram_ctrl_0_bram_0_blk_mem_gen_v8_4_8 U0
       (.addra({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,addra[12:2],1'b0,1'b0}),
        .addrb({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0}),
        .clka(clka),
        .clkb(1'b0),
        .dbiterr(NLW_U0_dbiterr_UNCONNECTED),
        .deepsleep(1'b0),
        .dina(dina),
        .dinb({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0}),
        .douta(douta),
        .doutb(NLW_U0_doutb_UNCONNECTED[31:0]),
        .eccpipece(1'b0),
        .ena(ena),
        .enb(1'b0),
        .injectdbiterr(1'b0),
        .injectsbiterr(1'b0),
        .rdaddrecc(NLW_U0_rdaddrecc_UNCONNECTED[31:0]),
        .regcea(1'b1),
        .regceb(1'b1),
        .rsta(rsta),
        .rsta_busy(rsta_busy),
        .rstb(1'b0),
        .rstb_busy(NLW_U0_rstb_busy_UNCONNECTED),
        .s_aclk(1'b0),
        .s_aresetn(1'b0),
        .s_axi_araddr({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0}),
        .s_axi_arburst({1'b0,1'b0}),
        .s_axi_arid({1'b0,1'b0,1'b0,1'b0}),
        .s_axi_arlen({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0}),
        .s_axi_arready(NLW_U0_s_axi_arready_UNCONNECTED),
        .s_axi_arsize({1'b0,1'b0,1'b0}),
        .s_axi_arvalid(1'b0),
        .s_axi_awaddr({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0}),
        .s_axi_awburst({1'b0,1'b0}),
        .s_axi_awid({1'b0,1'b0,1'b0,1'b0}),
        .s_axi_awlen({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0}),
        .s_axi_awready(NLW_U0_s_axi_awready_UNCONNECTED),
        .s_axi_awsize({1'b0,1'b0,1'b0}),
        .s_axi_awvalid(1'b0),
        .s_axi_bid(NLW_U0_s_axi_bid_UNCONNECTED[3:0]),
        .s_axi_bready(1'b0),
        .s_axi_bresp(NLW_U0_s_axi_bresp_UNCONNECTED[1:0]),
        .s_axi_bvalid(NLW_U0_s_axi_bvalid_UNCONNECTED),
        .s_axi_dbiterr(NLW_U0_s_axi_dbiterr_UNCONNECTED),
        .s_axi_injectdbiterr(1'b0),
        .s_axi_injectsbiterr(1'b0),
        .s_axi_rdaddrecc(NLW_U0_s_axi_rdaddrecc_UNCONNECTED[31:0]),
        .s_axi_rdata(NLW_U0_s_axi_rdata_UNCONNECTED[31:0]),
        .s_axi_rid(NLW_U0_s_axi_rid_UNCONNECTED[3:0]),
        .s_axi_rlast(NLW_U0_s_axi_rlast_UNCONNECTED),
        .s_axi_rready(1'b0),
        .s_axi_rresp(NLW_U0_s_axi_rresp_UNCONNECTED[1:0]),
        .s_axi_rvalid(NLW_U0_s_axi_rvalid_UNCONNECTED),
        .s_axi_sbiterr(NLW_U0_s_axi_sbiterr_UNCONNECTED),
        .s_axi_wdata({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0}),
        .s_axi_wlast(1'b0),
        .s_axi_wready(NLW_U0_s_axi_wready_UNCONNECTED),
        .s_axi_wstrb({1'b0,1'b0,1'b0,1'b0}),
        .s_axi_wvalid(1'b0),
        .sbiterr(NLW_U0_sbiterr_UNCONNECTED),
        .shutdown(1'b0),
        .sleep(1'b0),
        .wea(wea),
        .web({1'b0,1'b0,1'b0,1'b0}));
endmodule
`pragma protect begin_protected
`pragma protect version = 1
`pragma protect encrypt_agent = "XILINX"
`pragma protect encrypt_agent_info = "Xilinx Encryption Tool 2024.1"
`pragma protect key_keyowner="Synopsys", key_keyname="SNPS-VCS-RSA-2", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=128)
`pragma protect key_block
RSqbsRZSIb+QlYJMfFv1T7uHQ7PiCEXQkl687MHGm2LgPB15GIYcPmqKUSXgtkLsIFes91PTAyyB
9H9cyY4ZUxedcRg/9ZOB5pm3zPqAbcvGPmg1ivMhr/MlS19t5lYKM2tQo+0Yd+arJXlVZu2BMnvn
+I3G9t9tJuWUIWKjI+I=

`pragma protect key_keyowner="Aldec", key_keyname="ALDEC15_001", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
VRSQ05ZaB6bIhFIQ823mTvlJaG9+5iW5C3+KxGjq0sq9ziCshKOLpOGPDMmOWDqA4uBaxC5IKISr
w8+A8mqbYjXo5m1g8sGjNaETS0HKJsK+l5Y++tN4IEUs+DwxgrPR/+LWtChuOzVkfC7BG3LVUEMj
zM3GAyGcXGJ3sdBItZAfsevyiy7kr4Fw+nk2hWytGteu1NZk3VzPE7KQHLkOlHBPXf6P0j8LpKcr
2oNDgQ/WaEmg6OOvFeJuaWDaee8Sn6wKP/caMyoGdSeczsPtRrJeoSRlbNHlxhCv7zg+Cn2AgwrR
PTqGsMrkhv9U0sq+waS0CmwChsk4WB7RspGYUg==

`pragma protect key_keyowner="Mentor Graphics Corporation", key_keyname="MGC-VELOCE-RSA", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=128)
`pragma protect key_block
tNziOjCznlvIl4dadmB9r23Duf+HQHWOuHmupEU3PJxrazHVtZdNKspG9sRXhF9mjbpnSiKYCdFK
Jr9W/dxUid36faFIPKQazVTuOiE0hkzVQAGpYxXjT/ITB/9EFBvgvP5L3EAhHv32x6MA1vkFSI7x
HrZ09YNFEF6T7DPTZE4=

`pragma protect key_keyowner="Mentor Graphics Corporation", key_keyname="MGC-VERIF-SIM-RSA-2", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
QCYfxgkUHlX1cre1q9aS3sVDIOX36YBK4ZwJXAVUwA6f1OQ77XibjpWJHt5FK9F0PcYp/j21pqzO
BRdkDcFLVAjxER4J5t5iMVhoeMk+3fpiKfYrm4WFl1ygsJsfFJP0jqO1OkjC8iFBtm3n6b7CTl1o
cjBbcBp8UgW6E8rf5inXA0dRqybnyxKJSnMFYLinvpVU6QEc4OKO7mi/i/s9p/efiP+CdQf0yDRU
Fw7o7x0D7tjBv943g5L+4wGZ2JYU+ISqn4Ajxy/bWTTJDe6T/15evhngS61MC8Xjamzc4YLZBP8o
ShfSLoeZeO+Hk5n3xzJRghM0DQ6Sj7NqXFY68w==

`pragma protect key_keyowner="Real Intent", key_keyname="RI-RSA-KEY-1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
Uy8FDDy3dZQGAnMQV0HBesEs+/oZdaq35Kj1PGhy9J/+EBZm0nhhQgYtku8tWABW2jKAC1GtNTvo
uReQyr1hteMxTbD5OIuqv86eb1hXZVENlZ7ichG8auUjkeHAkaSYNbHOuDLIhSqHEL67XbcZ9zPG
1JOY3+VONSww0KYPcQbGSo/2DaC5C0Y+mZODRfJ4+b0WXjce6UaJetilBc3VtqqmodIM2d3HDawF
R0xVJfHj86rXmUkY+SNUw60zsV6raCY6G3k/rXpei1d6zn8tCThkKG5fwiWY8zA7kRdTFIlVKP9h
fb6kfzRBRT/BgVQ8d4RgEcEVV8m3u/Mf4KIlTw==

`pragma protect key_keyowner="Xilinx", key_keyname="xilinxt_2023_11", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
Pk1GeRlkUK9lt6DVXYVdtOABlzDEWQDcBsP/p+Wo5HaglDLG5b8gk08xTP3IcJ1RKcfuARPMGO2s
/VqFbnVADV90T1rhjIuWMcBnzYQK/ALUvwv11Uju9Gn0fvPIz52l3QBnpjHI1nlsFB7WeqkzVfHZ
tg9gO9bPHjHLjVd9BzH6McrEWY5RkZ0UBy0Fmh/SownJX1b0YGE7LdwKydEMEpyvb28bwTOwfEv/
4RtsfYtEvTjo6e1ZBm66D9IQmKUu32wzTfn5bFZHdyjZg6+HcTzvHMtQX2+AggXfP6FsO2/83qkb
0bfj226fnLhr32dJxtsaJS5OR63GYtzDJ05ITA==

`pragma protect key_keyowner="Metrics Technologies Inc.", key_keyname="DSim", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
LCfWqKmUoUSVOTKNAl5p8n1hfz7SMU2kDOUMBjsDncgSFqiu2zUy1I6GSDrVnF/2umJG5/mWcpvi
rQaFJOlrJ8DNctSuavdlopRAwTMsVi6dAlNGrAawSiDIxtI3tN3MDVdMiH5H+pJMqMt59yXneyCf
2RRSRz2sUQK/aj0lXlqKjVJzVbk8HaBQ8akBJF4iWSMK4foIzJ6iO1EupYovuW6uEiO7jQRWezlW
pbbDenOHHWbfinuX5cbkjpTKHGsEKct65q+ZXJp60m3sconSK3Y2eLQxusuJ1FHDJ4GGKO8mEzCv
3cfGdXX3pVL81OfGO/JD1aMs9H98CO5ssbHqlw==

`pragma protect key_keyowner="Atrenta", key_keyname="ATR-SG-RSA-1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=384)
`pragma protect key_block
A4S1e3DHcTeWzaDVuWDRb3Yf1BjiEsR1RtAeL0BJ7J/oPWMNj96MeGsUiHtZoiYqteTZxqax2cyZ
PV0cMLoBK4Ya8CyM+BTnkFA2ablsGt5Es4TgG/nFS9VEhmeKxu8boAsqW5697aiqOATJf/LucQh5
GOnPXHAuPrDj0A/fu8N2QduqGyysWUSc1KsoJ0/0noJYvLJ2yOhFi4uIUYQfG5LOuOrca5P43pqA
iwUKW/RrFXal2acJdFeXIKffZpKanSV97urdzKyBvf9EPV/M8g9uPFJJ1z6aS+FbknhVPs0pt6eD
+J/qib4gVp/HGnRo4YlxauUMv6Yv9wxiaObY6ttDfYf5p3uzWZMlf3i7YOzZwcd4aS/6+vkD28LG
L9piBIpLx2dvQy74RdvCVdvaP1LC6RMju9RfuXJhuX4ZAmDxRi0zQyRda838ikzwYeOCSKLIvRPb
nuJ8Zx2ot8EFqSeGaaRFaEMU6Zf5SptCUuVMHvSkinBewcwrLB5uiJTJ

`pragma protect key_keyowner="Cadence Design Systems.", key_keyname="CDS_RSA_KEY_VER_1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
gj+uMxV+tK4Di7pgSOE82FOBeWmUB1A7OKFOSMUW3qrmQ4/YhryfHMlWPxfAq8avQL7tnBTnRFEg
czbErdIcNzYjrM7Qq00QC/mTqmeQX4/apbqGvN+rwK4RR5oj22wfTib/UQNEQX6fbpi6PtmAeUR9
eShsfq+YWcf7z2Zw4Q+o4+E6m4/3CzU68vglNpzNsJ8S9/8XpdIrvAA/WRAX6OEOC4wlNIKDZsq/
+zMbFgSzN1rP844I/CDmxYM0NIzBWWhYBkPfJyQyigmUoXb84lDip0/Dmnq4EHvu7D/tZNnDl5st
JpftRfEpT6S8e/5MBeKUuhbfg6etHo/oFZvPKQ==

`pragma protect key_keyowner="Synplicity", key_keyname="SYNP15_1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
aWTy3xv6SqKsldtLS2gY4KrTS8U+KtFNRHS314f6EYZy1MHE9t7oICJ8eNB8up8A+odoE23N3fJb
1alhaadeRWU2GjlIiK1LjZ5PQw+jb1u1GWtRiY+TcTlD75XUlqwykVBrCDfm565DmgZjZle9T3/t
WEfLo+m/8GfBe8trVnoftsk/XI00BMFXRzw8doPGDhNECS1NUrLebryb9iO5Hf4A/40dtslTARsR
nicN0KoIIyiQ+QzliqyXU/8VjS45inON8R0Kv9Qx46EXUp7bds5uQ7QycRhpLG0IPnMIweudU67w
eQmpHJzvZKBCZks/R0OafZx44H6Jib2+QazBCw==

`pragma protect key_keyowner="Mentor Graphics Corporation", key_keyname="MGC-PREC-RSA", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
UGdPiChIPj1lSozqzCQx17Bi+8FWSuMUMzXUkDLH5zcP1t8tZLzh4CU4WAR8lmJxn8gH763fLp5c
RYU6zA0yxHzl2ksc5YRU1XEfQQT9ha8fQnz+18wVKcsa5UIOfMbGDwnS9yfX59ntG8CB0uF8bJKE
y1CS6U/1Stfs1w2mF94iDxI2n2GJlb1UPtWpmxMBI88hY0GktTPXP2Y7JKl8zRl/Lq0wIF8pHwXk
B4nOgKm6hfzPj0xZ6E/TuER/JE3fy8RSm24IlL/CUgpReEslEOYjQ4EKKZRG9/fxg26utQWW9p+G
fWVU53qrFGzBhKQ96Paj1ROkv6hDHyUb6n7uSw==

`pragma protect data_method = "AES128-CBC"
`pragma protect encoding = (enctype = "BASE64", line_length = 76, bytes = 52960)
`pragma protect data_block
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
Fl9RhpVvRA==
`pragma protect end_protected
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
