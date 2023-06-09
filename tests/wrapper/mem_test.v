module top_module(
  input wire clk,
  input wire reset,
  input wire [7:0] read_address,
  input wire [7:0] write_address,
  input wire [31:0] data_in,
  input wire write_enable,
  input wire read_enable,
  output wire [31:0] data_out
);
  // Instantiate the memory controller module
  dut memory_controller(
    .clk(clk),
    .reset(reset),
    .read_address(read_address),
    .write_address(write_address),
    .data_in(data_in),
    .write_enable(write_enable),
    .read_enable(read_enable),
    .data_out(data_out)
  );
  initial begin
	$dumpfile("waves.vcd");
	$dumpvars;
end

endmodule
