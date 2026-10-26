`timescale 1ns/1ps
module mac #(
    parameter int W = 8, AW = 20
) (
    input  logic clk, rst, in_valid,
    input  logic signed [W-1:0] x, weight,
    input  logic signed [AW-1:0] acc_in,
    output logic out_valid,
    output logic signed [AW-1:0] result
);
    // Contract: AW >= 2*W. Arithmetic wraps if AW bits overflow.
    logic signed [2*W-1:0] product;
    logic signed [AW-1:0] product_extended;
    assign product = x * weight;
    assign product_extended = product;
    always_ff @(posedge clk) begin
        if (rst) begin
            out_valid <= 1'b0;
            result <= '0;
        end else begin
            out_valid <= in_valid;
            if (in_valid)
                result <= acc_in + product_extended;
        end
    end
endmodule
