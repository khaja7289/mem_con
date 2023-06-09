import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer


@cocotb.test()
async def memory_controller_test(dut):
    # Test Case 1: Write and Read
    dut.reset = 1
    await RisingEdge(dut.clk)
    dut.reset = 0

    # Perform write operation
    dut.write_address = 0x10
    dut.data_in = 0xABCD
    dut.write_enable = 1
    await RisingEdge(dut.clk)
    dut.write_enable = 0

    # Perform read operation
    dut.read_address = 0x10
    dut.read_enable = 1
    await RisingEdge(dut.clk)
    dut.read_enable = 0

    # Wait for read operation to complete
    await RisingEdge(dut.data_out)

    # Check the read data
    expected_data = 0xABCD
    assert dut.data_out == expected_data, f"Read data mismatch. Expected: {expected_data}, Got: {dut.data_out}"

    # Test Case 2: Write to Multiple Addresses
    dut.reset = 1
    await RisingEdge(dut.clk)
    dut.reset = 0

    # Perform multiple write operations
    addresses = [0x20, 0x30, 0x40]
    data_values = [0x1111, 0x2222, 0x3333]
    for i in range(len(addresses)):
        dut.write_address = addresses[i]
        dut.data_in = data_values[i]
        dut.write_enable = 1
        await RisingEdge(dut.clk)
        dut.write_enable = 0

    # Perform read operations for the written addresses
    for i in range(len(addresses)):
        dut.read_address = addresses[i]
        dut.read_enable = 1
        await RisingEdge(dut.clk)
        dut.read_enable = 0
        await RisingEdge(dut.data_out)
        assert dut.data_out == data_values[i], f"Read data mismatch for address {hex(addresses[i])}. Expected: {data_values[i]}, Got: {dut.data_out}"

    # Test Case 3: Read from Unwritten Address
    dut.reset = 1
    await RisingEdge(dut.clk)
    dut.reset = 0

    # Perform read operation from unwritten address
    dut.read_address = 0x50
    dut.read_enable = 1
    await RisingEdge(dut.clk)
    dut.read_enable = 0
    await RisingEdge(dut.data_out)
    assert dut.data_out == 0, "Read data mismatch for unwritten address"

    # Finish the test
    await RisingEdge(dut.clk)
