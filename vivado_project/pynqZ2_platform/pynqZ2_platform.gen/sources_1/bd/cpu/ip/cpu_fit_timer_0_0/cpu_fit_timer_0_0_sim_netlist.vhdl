-- Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
-- Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2024.1 (lin64) Build 5076996 Wed May 22 18:36:09 MDT 2024
-- Date        : Tue Jul  9 13:40:04 2024
-- Host        : travelmate running 64-bit Ubuntu 22.04.4 LTS
-- Command     : write_vhdl -force -mode funcsim
--               /home/kike/Desktop/marvin/vivado_project/pynqZ2_platform/pynqZ2_platform.gen/sources_1/bd/cpu/ip/cpu_fit_timer_0_0/cpu_fit_timer_0_0_sim_netlist.vhdl
-- Design      : cpu_fit_timer_0_0
-- Purpose     : This VHDL netlist is a functional simulation representation of the design and should not be modified or
--               synthesized. This netlist cannot be used for SDF annotated simulation.
-- Device      : xc7z020clg400-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity cpu_fit_timer_0_0_Divide_part is
  port (
    loop_Bit : out STD_LOGIC;
    Rst_d1 : out STD_LOGIC;
    CE : out STD_LOGIC;
    Rst_d1_reg_0 : out STD_LOGIC;
    Rst_d1_reg_1 : out STD_LOGIC;
    Clk : in STD_LOGIC;
    Rst : in STD_LOGIC;
    loop_Bit_0 : in STD_LOGIC;
    loop_Bit_1 : in STD_LOGIC
  );
  attribute ORIG_REF_NAME : string;
  attribute ORIG_REF_NAME of cpu_fit_timer_0_0_Divide_part : entity is "Divide_part";
end cpu_fit_timer_0_0_Divide_part;

architecture STRUCTURE of cpu_fit_timer_0_0_Divide_part is
  signal \One_SRL16.SRL16E_I_i_1__0_n_0\ : STD_LOGIC;
  signal \^rst_d1\ : STD_LOGIC;
  signal \^loop_bit\ : STD_LOGIC;
  attribute box_type : string;
  attribute box_type of \One_SRL16.SRL16E_I\ : label is "PRIMITIVE";
  attribute srl_bus_name : string;
  attribute srl_bus_name of \One_SRL16.SRL16E_I\ : label is "U0/\Using_SRL16s.SRL16s ";
  attribute srl_name : string;
  attribute srl_name of \One_SRL16.SRL16E_I\ : label is "U0/\Using_SRL16s.SRL16s[1].Divide_I/One_SRL16.SRL16E_I ";
  attribute SOFT_HLUTNM : string;
  attribute SOFT_HLUTNM of \One_SRL16.SRL16E_I_i_1__0\ : label is "soft_lutpair0";
  attribute SOFT_HLUTNM of \One_SRL16.SRL16E_I_i_2\ : label is "soft_lutpair0";
begin
  Rst_d1 <= \^rst_d1\;
  loop_Bit <= \^loop_bit\;
\More_Than_Two.SRLC16E_1_i_2\: unisim.vcomponents.LUT3
    generic map(
      INIT => X"0E"
    )
        port map (
      I0 => \^rst_d1\,
      I1 => loop_Bit_1,
      I2 => Rst,
      O => Rst_d1_reg_1
    );
\One_SRL16.SRL16E_I\: unisim.vcomponents.SRL16E
    generic map(
      INIT => X"0001",
      IS_CLK_INVERTED => '0'
    )
        port map (
      A0 => '1',
      A1 => '0',
      A2 => '1',
      A3 => '1',
      CE => '1',
      CLK => Clk,
      D => \One_SRL16.SRL16E_I_i_1__0_n_0\,
      Q => \^loop_bit\
    );
\One_SRL16.SRL16E_I_i_1\: unisim.vcomponents.LUT3
    generic map(
      INIT => X"FE"
    )
        port map (
      I0 => \^loop_bit\,
      I1 => Rst,
      I2 => \^rst_d1\,
      O => CE
    );
\One_SRL16.SRL16E_I_i_1__0\: unisim.vcomponents.LUT3
    generic map(
      INIT => X"0E"
    )
        port map (
      I0 => \^rst_d1\,
      I1 => \^loop_bit\,
      I2 => Rst,
      O => \One_SRL16.SRL16E_I_i_1__0_n_0\
    );
\One_SRL16.SRL16E_I_i_2\: unisim.vcomponents.LUT3
    generic map(
      INIT => X"0E"
    )
        port map (
      I0 => \^rst_d1\,
      I1 => loop_Bit_0,
      I2 => Rst,
      O => Rst_d1_reg_0
    );
Rst_d1_reg: unisim.vcomponents.FDRE
    generic map(
      INIT => '0'
    )
        port map (
      C => Clk,
      CE => '1',
      D => Rst,
      Q => \^rst_d1\,
      R => '0'
    );
end STRUCTURE;
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity \cpu_fit_timer_0_0_Divide_part__parameterized0\ is
  port (
    loop_Bit : out STD_LOGIC;
    \Using_SRL16s.Clk_En_I_1\ : out STD_LOGIC;
    CE : out STD_LOGIC;
    CE_0 : in STD_LOGIC;
    \One_SRL16.SRL16E_I_0\ : in STD_LOGIC;
    Clk : in STD_LOGIC;
    Rst : in STD_LOGIC;
    Rst_d1 : in STD_LOGIC;
    loop_Bit_1 : in STD_LOGIC
  );
  attribute ORIG_REF_NAME : string;
  attribute ORIG_REF_NAME of \cpu_fit_timer_0_0_Divide_part__parameterized0\ : entity is "Divide_part";
end \cpu_fit_timer_0_0_Divide_part__parameterized0\;

architecture STRUCTURE of \cpu_fit_timer_0_0_Divide_part__parameterized0\ is
  signal \^using_srl16s.clk_en_i_1\ : STD_LOGIC;
  signal \^loop_bit\ : STD_LOGIC;
  signal \not_First.Clk_En_Out_i_i_1_n_0\ : STD_LOGIC;
  signal \not_First.Out1\ : STD_LOGIC;
  signal \not_First.Out1_i_1__0_n_0\ : STD_LOGIC;
  attribute box_type : string;
  attribute box_type of \One_SRL16.SRL16E_I\ : label is "PRIMITIVE";
  attribute srl_bus_name : string;
  attribute srl_bus_name of \One_SRL16.SRL16E_I\ : label is "U0/\Using_SRL16s.SRL16s ";
  attribute srl_name : string;
  attribute srl_name of \One_SRL16.SRL16E_I\ : label is "U0/\Using_SRL16s.SRL16s[2].Divide_I/One_SRL16.SRL16E_I ";
  attribute SOFT_HLUTNM : string;
  attribute SOFT_HLUTNM of \not_First.Clk_En_Out_i_i_1\ : label is "soft_lutpair1";
  attribute SOFT_HLUTNM of \not_First.Out1_i_1__0\ : label is "soft_lutpair1";
begin
  \Using_SRL16s.Clk_En_I_1\ <= \^using_srl16s.clk_en_i_1\;
  loop_Bit <= \^loop_bit\;
\More_Than_Two.SRLC16E_1_i_1\: unisim.vcomponents.LUT3
    generic map(
      INIT => X"FE"
    )
        port map (
      I0 => \^using_srl16s.clk_en_i_1\,
      I1 => Rst,
      I2 => Rst_d1,
      O => CE
    );
\One_SRL16.SRL16E_I\: unisim.vcomponents.SRL16E
    generic map(
      INIT => X"0001",
      IS_CLK_INVERTED => '0'
    )
        port map (
      A0 => '1',
      A1 => '1',
      A2 => '0',
      A3 => '1',
      CE => CE_0,
      CLK => Clk,
      D => \One_SRL16.SRL16E_I_0\,
      Q => \^loop_bit\
    );
\not_First.Clk_En_Out_i_i_1\: unisim.vcomponents.LUT4
    generic map(
      INIT => X"2F20"
    )
        port map (
      I0 => loop_Bit_1,
      I1 => Rst,
      I2 => \not_First.Out1\,
      I3 => \^using_srl16s.clk_en_i_1\,
      O => \not_First.Clk_En_Out_i_i_1_n_0\
    );
\not_First.Clk_En_Out_i_reg\: unisim.vcomponents.FDRE
    generic map(
      INIT => '0'
    )
        port map (
      C => Clk,
      CE => '1',
      D => \not_First.Clk_En_Out_i_i_1_n_0\,
      Q => \^using_srl16s.clk_en_i_1\,
      R => '0'
    );
\not_First.Out1_i_1__0\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => \^loop_bit\,
      I1 => Rst,
      O => \not_First.Out1_i_1__0_n_0\
    );
\not_First.Out1_reg\: unisim.vcomponents.FDRE
     port map (
      C => Clk,
      CE => '1',
      D => \not_First.Out1_i_1__0_n_0\,
      Q => \not_First.Out1\,
      R => '0'
    );
end STRUCTURE;
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity \cpu_fit_timer_0_0_Divide_part__parameterized1\ is
  port (
    loop_Bit : out STD_LOGIC;
    Interrupt : out STD_LOGIC;
    CE : in STD_LOGIC;
    \More_Than_Two.SRLC16E_1_0\ : in STD_LOGIC;
    Clk : in STD_LOGIC;
    \Using_SRL16s.Clk_En_I_1\ : in STD_LOGIC;
    Rst : in STD_LOGIC
  );
  attribute ORIG_REF_NAME : string;
  attribute ORIG_REF_NAME of \cpu_fit_timer_0_0_Divide_part__parameterized1\ : entity is "Divide_part";
end \cpu_fit_timer_0_0_Divide_part__parameterized1\;

architecture STRUCTURE of \cpu_fit_timer_0_0_Divide_part__parameterized1\ is
  signal \^interrupt\ : STD_LOGIC;
  signal \More_Than_Two.SRL16E_n_i_1_n_0\ : STD_LOGIC;
  signal \More_Than_Two.The_Rest[1].SRLC16E_I_i_1_n_0\ : STD_LOGIC;
  signal \More_Than_Two.shifts_0\ : STD_LOGIC;
  signal \More_Than_Two.shifts_1\ : STD_LOGIC;
  signal \^loop_bit\ : STD_LOGIC;
  signal \not_First.Clk_En_Out_i_i_1__0_n_0\ : STD_LOGIC;
  signal \not_First.Out1_i_1_n_0\ : STD_LOGIC;
  signal \not_First.Out1_reg_n_0\ : STD_LOGIC;
  signal \NLW_More_Than_Two.SRLC16E_1_Q_UNCONNECTED\ : STD_LOGIC;
  signal \NLW_More_Than_Two.The_Rest[1].SRLC16E_I_Q_UNCONNECTED\ : STD_LOGIC;
  attribute box_type : string;
  attribute box_type of \More_Than_Two.SRL16E_n\ : label is "PRIMITIVE";
  attribute srl_bus_name : string;
  attribute srl_bus_name of \More_Than_Two.SRL16E_n\ : label is "U0/\Using_SRL16s.SRL16s ";
  attribute srl_name : string;
  attribute srl_name of \More_Than_Two.SRL16E_n\ : label is "U0/\Using_SRL16s.SRL16s[3].Divide_I/More_Than_Two.SRL16E_n ";
  attribute SOFT_HLUTNM : string;
  attribute SOFT_HLUTNM of \More_Than_Two.SRL16E_n_i_1\ : label is "soft_lutpair2";
  attribute box_type of \More_Than_Two.SRLC16E_1\ : label is "PRIMITIVE";
  attribute box_type of \More_Than_Two.The_Rest[1].SRLC16E_I\ : label is "PRIMITIVE";
  attribute SOFT_HLUTNM of \More_Than_Two.The_Rest[1].SRLC16E_I_i_1\ : label is "soft_lutpair2";
begin
  Interrupt <= \^interrupt\;
  loop_Bit <= \^loop_bit\;
\More_Than_Two.SRL16E_n\: unisim.vcomponents.SRL16E
    generic map(
      INIT => X"0000",
      IS_CLK_INVERTED => '0'
    )
        port map (
      A0 => '0',
      A1 => '0',
      A2 => '1',
      A3 => '0',
      CE => CE,
      CLK => Clk,
      D => \More_Than_Two.SRL16E_n_i_1_n_0\,
      Q => \^loop_bit\
    );
\More_Than_Two.SRL16E_n_i_1\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => \More_Than_Two.shifts_0\,
      I1 => Rst,
      O => \More_Than_Two.SRL16E_n_i_1_n_0\
    );
\More_Than_Two.SRLC16E_1\: unisim.vcomponents.SRLC16E
    generic map(
      INIT => X"0001",
      IS_CLK_INVERTED => '0'
    )
        port map (
      A0 => '1',
      A1 => '1',
      A2 => '1',
      A3 => '1',
      CE => CE,
      CLK => Clk,
      D => \More_Than_Two.SRLC16E_1_0\,
      Q => \NLW_More_Than_Two.SRLC16E_1_Q_UNCONNECTED\,
      Q15 => \More_Than_Two.shifts_1\
    );
\More_Than_Two.The_Rest[1].SRLC16E_I\: unisim.vcomponents.SRLC16E
    generic map(
      INIT => X"0000",
      IS_CLK_INVERTED => '0'
    )
        port map (
      A0 => '1',
      A1 => '1',
      A2 => '1',
      A3 => '1',
      CE => CE,
      CLK => Clk,
      D => \More_Than_Two.The_Rest[1].SRLC16E_I_i_1_n_0\,
      Q => \NLW_More_Than_Two.The_Rest[1].SRLC16E_I_Q_UNCONNECTED\,
      Q15 => \More_Than_Two.shifts_0\
    );
\More_Than_Two.The_Rest[1].SRLC16E_I_i_1\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => \More_Than_Two.shifts_1\,
      I1 => Rst,
      O => \More_Than_Two.The_Rest[1].SRLC16E_I_i_1_n_0\
    );
\not_First.Clk_En_Out_i_i_1__0\: unisim.vcomponents.LUT3
    generic map(
      INIT => X"B8"
    )
        port map (
      I0 => \Using_SRL16s.Clk_En_I_1\,
      I1 => \not_First.Out1_reg_n_0\,
      I2 => \^interrupt\,
      O => \not_First.Clk_En_Out_i_i_1__0_n_0\
    );
\not_First.Clk_En_Out_i_reg\: unisim.vcomponents.FDRE
    generic map(
      INIT => '0'
    )
        port map (
      C => Clk,
      CE => '1',
      D => \not_First.Clk_En_Out_i_i_1__0_n_0\,
      Q => \^interrupt\,
      R => '0'
    );
\not_First.Out1_i_1\: unisim.vcomponents.LUT2
    generic map(
      INIT => X"2"
    )
        port map (
      I0 => \^loop_bit\,
      I1 => Rst,
      O => \not_First.Out1_i_1_n_0\
    );
\not_First.Out1_reg\: unisim.vcomponents.FDRE
     port map (
      C => Clk,
      CE => '1',
      D => \not_First.Out1_i_1_n_0\,
      Q => \not_First.Out1_reg_n_0\,
      R => '0'
    );
end STRUCTURE;
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity cpu_fit_timer_0_0_FIT_timer is
  port (
    Clk : in STD_LOGIC;
    Rst : in STD_LOGIC;
    Interrupt : out STD_LOGIC
  );
  attribute C_EXT_RESET_HIGH : integer;
  attribute C_EXT_RESET_HIGH of cpu_fit_timer_0_0_FIT_timer : entity is 1;
  attribute C_FAMILY : string;
  attribute C_FAMILY of cpu_fit_timer_0_0_FIT_timer : entity is "zynq";
  attribute C_INACCURACY : integer;
  attribute C_INACCURACY of cpu_fit_timer_0_0_FIT_timer : entity is 0;
  attribute C_NO_CLOCKS : integer;
  attribute C_NO_CLOCKS of cpu_fit_timer_0_0_FIT_timer : entity is 6216;
  attribute ORIG_REF_NAME : string;
  attribute ORIG_REF_NAME of cpu_fit_timer_0_0_FIT_timer : entity is "FIT_timer";
end cpu_fit_timer_0_0_FIT_timer;

architecture STRUCTURE of cpu_fit_timer_0_0_FIT_timer is
  signal CE : STD_LOGIC;
  signal CE_0 : STD_LOGIC;
  signal Rst_d1 : STD_LOGIC;
  signal \Using_SRL16s.Clk_En_I_1\ : STD_LOGIC;
  signal \Using_SRL16s.SRL16s[1].Divide_I_n_3\ : STD_LOGIC;
  signal \Using_SRL16s.SRL16s[1].Divide_I_n_4\ : STD_LOGIC;
  signal loop_Bit : STD_LOGIC;
  signal loop_Bit_1 : STD_LOGIC;
  signal loop_Bit_2 : STD_LOGIC;
begin
\Using_SRL16s.SRL16s[1].Divide_I\: entity work.cpu_fit_timer_0_0_Divide_part
     port map (
      CE => CE,
      Clk => Clk,
      Rst => Rst,
      Rst_d1 => Rst_d1,
      Rst_d1_reg_0 => \Using_SRL16s.SRL16s[1].Divide_I_n_3\,
      Rst_d1_reg_1 => \Using_SRL16s.SRL16s[1].Divide_I_n_4\,
      loop_Bit => loop_Bit,
      loop_Bit_0 => loop_Bit_1,
      loop_Bit_1 => loop_Bit_2
    );
\Using_SRL16s.SRL16s[2].Divide_I\: entity work.\cpu_fit_timer_0_0_Divide_part__parameterized0\
     port map (
      CE => CE_0,
      CE_0 => CE,
      Clk => Clk,
      \One_SRL16.SRL16E_I_0\ => \Using_SRL16s.SRL16s[1].Divide_I_n_3\,
      Rst => Rst,
      Rst_d1 => Rst_d1,
      \Using_SRL16s.Clk_En_I_1\ => \Using_SRL16s.Clk_En_I_1\,
      loop_Bit => loop_Bit_1,
      loop_Bit_1 => loop_Bit
    );
\Using_SRL16s.SRL16s[3].Divide_I\: entity work.\cpu_fit_timer_0_0_Divide_part__parameterized1\
     port map (
      CE => CE_0,
      Clk => Clk,
      Interrupt => Interrupt,
      \More_Than_Two.SRLC16E_1_0\ => \Using_SRL16s.SRL16s[1].Divide_I_n_4\,
      Rst => Rst,
      \Using_SRL16s.Clk_En_I_1\ => \Using_SRL16s.Clk_En_I_1\,
      loop_Bit => loop_Bit_2
    );
end STRUCTURE;
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity cpu_fit_timer_0_0 is
  port (
    Clk : in STD_LOGIC;
    Rst : in STD_LOGIC;
    Interrupt : out STD_LOGIC
  );
  attribute NotValidForBitStream : boolean;
  attribute NotValidForBitStream of cpu_fit_timer_0_0 : entity is true;
  attribute CHECK_LICENSE_TYPE : string;
  attribute CHECK_LICENSE_TYPE of cpu_fit_timer_0_0 : entity is "cpu_fit_timer_0_0,fit_timer,{}";
  attribute downgradeipidentifiedwarnings : string;
  attribute downgradeipidentifiedwarnings of cpu_fit_timer_0_0 : entity is "yes";
  attribute x_core_info : string;
  attribute x_core_info of cpu_fit_timer_0_0 : entity is "fit_timer,Vivado 2024.1";
end cpu_fit_timer_0_0;

architecture STRUCTURE of cpu_fit_timer_0_0 is
  attribute C_EXT_RESET_HIGH : integer;
  attribute C_EXT_RESET_HIGH of U0 : label is 1;
  attribute C_FAMILY : string;
  attribute C_FAMILY of U0 : label is "zynq";
  attribute C_INACCURACY : integer;
  attribute C_INACCURACY of U0 : label is 0;
  attribute C_NO_CLOCKS : integer;
  attribute C_NO_CLOCKS of U0 : label is 6216;
  attribute x_interface_info : string;
  attribute x_interface_info of Clk : signal is "xilinx.com:signal:clock:1.0 CLK.Clk CLK";
  attribute x_interface_parameter : string;
  attribute x_interface_parameter of Clk : signal is "XIL_INTERFACENAME CLK.Clk, ASSOCIATED_RESET Rst, FREQ_HZ 100000000, FREQ_TOLERANCE_HZ 0, PHASE 0.0, CLK_DOMAIN cpu_processing_system7_0_0_FCLK_CLK0, INSERT_VIP 0";
  attribute x_interface_info of Interrupt : signal is "xilinx.com:signal:interrupt:1.0 INTERRUPT.Interrupt INTERRUPT";
  attribute x_interface_parameter of Interrupt : signal is "XIL_INTERFACENAME INTERRUPT.Interrupt, SENSITIVITY LEVEL_HIGH, SUGGESTED_PRIORITY HIGH, PortWidth 1";
  attribute x_interface_info of Rst : signal is "xilinx.com:signal:reset:1.0 RST.Rst RST";
  attribute x_interface_parameter of Rst : signal is "XIL_INTERFACENAME RST.Rst, POLARITY ACTIVE_HIGH, INSERT_VIP 0";
begin
U0: entity work.cpu_fit_timer_0_0_FIT_timer
     port map (
      Clk => Clk,
      Interrupt => Interrupt,
      Rst => Rst
    );
end STRUCTURE;
