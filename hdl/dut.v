module memory_controller (
  input wire clk,
  input wire reset,
  input wire [7:0] read_address,
  input wire [7:0] write_address,
  input wire [31:0] data_in,
  input wire write_enable,
  input wire read_enable,
  output wire [31:0] data_out
);
  reg [31:0] memory [255:0];

  always @(posedge clk or posedge reset) begin
    if (reset) begin
      // Reset memory contents
      for (int i = 0; i < 256; i = i + 1) begin
        memory[i] <= 32'h00000000;
      end
    end else begin
      // Write operation
      if (write_enable) begin
        memory[write_address] <= data_in;
      end

      // Read operation
      if (read_enable) begin
        data_out <= memory[read_address];
      end
    end
  end
endmodule
