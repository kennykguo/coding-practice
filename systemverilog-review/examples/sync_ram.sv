`timescale 1ns/1ps
module sync_ram #(
    parameter int W = 8, DEPTH = 8,
    localparam int AW = (DEPTH <= 1) ? 1 : $clog2(DEPTH)
) (
    input  logic clk, rst,
    input  logic wr_en, rd_en,
    input  logic [AW-1:0] wr_addr, rd_addr,
    input  logic [W-1:0] wr_data,
    output logic rd_valid,
    output logic [W-1:0] rd_data
);
    // Valid addresses only. This model specifies old data on a collision.
    logic [W-1:0] mem [0:DEPTH-1];
    always_ff @(posedge clk) begin
        if (rst) begin
            rd_valid <= 1'b0;
        end else begin
            rd_valid <= rd_en;
            if (rd_en)
                rd_data <= mem[rd_addr];
            if (wr_en)
                mem[wr_addr] <= wr_data;
        end
    end
endmodule
