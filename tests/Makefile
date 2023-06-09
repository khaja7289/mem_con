SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/../hdl/dut.v
VERILOG_SOURCES += $(PWD)/wrappers/dut_test.v
TOPLEVEL = dut_test
MODULE = mem_test
include $(shell cocotb-config --makefiles)/Makefile.sim
