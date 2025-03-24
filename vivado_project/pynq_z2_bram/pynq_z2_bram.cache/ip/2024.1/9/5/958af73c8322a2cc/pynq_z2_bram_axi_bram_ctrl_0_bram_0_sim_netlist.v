// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2024.1 (lin64) Build 5076996 Wed May 22 18:36:09 MDT 2024
// Date        : Mon Jul 15 13:38:33 2024
// Host        : travelmate running 64-bit Ubuntu 22.04.4 LTS
// Command     : write_verilog -force -mode funcsim -rename_top decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix -prefix
//               decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix_ pynq_z2_bram_axi_bram_ctrl_0_bram_0_sim_netlist.v
// Design      : pynq_z2_bram_axi_bram_ctrl_0_bram_0
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xc7z020clg400-1
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CHECK_LICENSE_TYPE = "pynq_z2_bram_axi_bram_ctrl_0_bram_0,blk_mem_gen_v8_4_8,{}" *) (* downgradeipidentifiedwarnings = "yes" *) (* x_core_info = "blk_mem_gen_v8_4_8,Vivado 2024.1" *) 
(* NotValidForBitStream *)
module decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix
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
  decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix_blk_mem_gen_v8_4_8 U0
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
`pragma protect encoding = (enctype = "BASE64", line_length = 76, bytes = 52768)
`pragma protect data_block
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
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
