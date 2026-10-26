`timescale 1ns/1ps
module stream_sum (
    input  logic clk, rst, start,
    input  logic [4:0] command_count,
    input  logic in_valid,
    output logic in_ready,
    input  logic [7:0] in_data,
    output logic busy, done,
    output logic [15:0] sum
);
    typedef enum logic [1:0] {IDLE, RUN, DONE} state_t;
    state_t state, next_state;
    logic [4:0] left;
    assign in_ready = (state == RUN);
    assign busy = (state != IDLE);
    assign done = (state == DONE);
    always_comb begin
        next_state = state;
        case (state)
            IDLE: if (start) begin
                if (command_count == 0) next_state = DONE;
                else next_state = RUN;
            end
            RUN: if (in_valid && in_ready && left == 1)
                next_state = DONE;
            DONE: next_state = IDLE;
            default: next_state = IDLE;
        endcase
    end
    always_ff @(posedge clk) begin
        if (rst) begin
            state <= IDLE;
            left <= '0;
            sum <= '0;
        end else begin
            state <= next_state;
            if (state == IDLE && start) begin
                left <= command_count;
                sum <= '0;
            end else if (state == RUN && in_valid && in_ready) begin
                sum <= sum + {8'b0, in_data};
                left <= left - 1'b1;
            end
        end
    end
endmodule
