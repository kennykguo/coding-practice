`timescale 1ns/1ps
module weight_bank #(
    parameter int W = 8
) (
    input  logic clk, rst, load, swap,
    input  logic signed [W-1:0] weight_in,
    output logic signed [W-1:0] active, shadow,
    output logic signed [W-1:0] selected
);
    // Explicit bypass if a datapath must use the shadow on the swap edge.
    assign selected = swap ? shadow : active;
    always_ff @(posedge clk) begin
        if (rst) begin
            active <= '0;
            shadow <= '0;
        end else begin
            if (load) shadow <= weight_in;
            if (swap) active <= shadow;
        end
    end
endmodule
