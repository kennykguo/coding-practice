`timescale 1ns/1ps
module rv_register #(
    parameter int W = 8
) (
    input  logic clk, rst,
    input  logic in_valid,
    output logic in_ready,
    input  logic [W-1:0] in_data,
    output logic out_valid,
    input  logic out_ready,
    output logic [W-1:0] out_data
);
    assign in_ready = !out_valid || out_ready;
    always_ff @(posedge clk) begin
        if (rst) begin
            out_valid <= 1'b0;
        end else if (in_ready) begin
            out_valid <= in_valid;
            if (in_valid)
                out_data <= in_data;
        end
    end
endmodule
