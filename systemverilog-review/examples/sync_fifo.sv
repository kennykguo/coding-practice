`timescale 1ns/1ps
module sync_fifo #(
    parameter int W = 8, DEPTH = 4,
    localparam int AW = (DEPTH <= 1) ? 1 : $clog2(DEPTH),
    localparam int CW = $clog2(DEPTH+1)
) (
    input  logic clk, rst,
    input  logic in_valid,
    output logic in_ready,
    input  logic [W-1:0] in_data,
    output logic out_valid,
    input  logic out_ready,
    output logic [W-1:0] out_data
);
    // Contract: DEPTH >= 1; combinational head read, no empty bypass.
    logic [W-1:0] mem [0:DEPTH-1];
    logic [AW-1:0] rd_ptr, wr_ptr;
    logic [CW-1:0] count;
    logic push, pop;
    assign out_valid = (count != 0);
    assign out_data = mem[rd_ptr];
    assign pop = out_valid && out_ready;
    assign in_ready = (count < CW'(DEPTH)) || pop;
    assign push = in_valid && in_ready;
    always_ff @(posedge clk) begin
        if (rst) begin
            rd_ptr <= '0;
            wr_ptr <= '0;
            count <= '0;
        end else begin
            if (push) begin
                mem[wr_ptr] <= in_data;
                wr_ptr <= (wr_ptr == AW'(DEPTH-1)) ? '0 : wr_ptr + 1'b1;
            end
            if (pop)
                rd_ptr <= (rd_ptr == AW'(DEPTH-1)) ? '0 : rd_ptr + 1'b1;
            case ({push, pop})
                2'b10: count <= count + 1'b1;
                2'b01: count <= count - 1'b1;
                default: ;
            endcase
        end
    end
endmodule
