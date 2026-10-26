`timescale 1ns/1ps
module lane_adders #(
    parameter int LANES = 2, W = 8
) (
    input  logic [LANES-1:0][W-1:0] a, b,
    output logic [LANES-1:0][W:0] y
);
    for (genvar i = 0; i < LANES; i++) begin : lane
        assign y[i] = {1'b0, a[i]} + {1'b0, b[i]};
    end
endmodule
