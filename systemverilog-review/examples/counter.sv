`timescale 1ns/1ps
module counter #(
    parameter int LIMIT = 10,
    localparam int CW = (LIMIT <= 1) ? 1 : $clog2(LIMIT)
) (
    input  logic clk, rst, en,
    output logic [CW-1:0] count,
    output logic tick
);
    // Contract: LIMIT >= 1. Reset is synchronous and active high.
    always_ff @(posedge clk) begin
        if (rst) begin
            count <= '0;
            tick <= 1'b0;
        end else begin
            tick <= 1'b0;
            if (en) begin
                if (count == CW'(LIMIT-1)) begin
                    count <= '0;
                    tick <= 1'b1;
                end else begin
                    count <= count + 1'b1;
                end
            end
        end
    end
endmodule
