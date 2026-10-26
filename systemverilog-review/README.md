# RTL and SystemVerilog refresher

Read **systemverilog-review.pdf**. The editable source is `main.tex`.

The guide starts with clocked hardware and essential syntax. It then derives reusable blocks and covers SRAM/DRAM interfaces, signed arithmetic and fixed point, pipelines, reset/CDC, dataflow and CGRA basics, a small cocotb workflow, and a pinned tiny-tpu project walkthrough. Each topic connects its update rules to a changed design requirement.

Project references use public commit `04ad69238072369ac3b5c43c495a3124b62a95aa`. The SystemVerilog and hardened Verilog variants differ; the guide identifies those differences rather than combining their behavior. No original project files were changed.

## Run the examples

Install Icarus Verilog (`iverilog` and `vvp`) and Python 3.10 or later. The examples were run with Icarus 12.0, Python 3.13, and cocotb 2.0.0.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python verify.py
```

The script runs 14 simulation configurations/tests and writes `verification.json` after success:

- Counter limits 1, 3, 10, and 16.
- FIFO depths 1, 3, and 8, including stalls, wraparound, simultaneous input/output, and reset while occupied.
- One-entry ready/valid register, synchronous-read RAM with old-data collisions, signed MAC with wraparound, active/shadow weight commit, streaming-sum FSM, and generated lane adders.
- The complete cocotb example printed in the guide.

The independent reference models use a fixed random seed. The tests check accepted transfers, ordering, cycle alignment, and boundary behavior. They do not constitute exhaustive proofs.

For optional generic synthesis checks, install Yosys and run:

```sh
python3 check_synthesis.py
```

This checks seven core modules at their default parameters: parsing, hierarchy, process lowering, structural checks, and absence of inferred latches. Results are in `synthesis-checks.json`. The generated multidimensional packed-port syntax example is simulated with Icarus; it is outside this Yosys check.

These checks do not include technology mapping, physical SRAM inference, static timing, physical implementation, CDC signoff, or the original tiny-tpu regression/formal suite. The guide's partial snippets illustrate concepts; the eight complete modules are the compiled examples.

## Rebuild the PDF

Open this folder in the Codex LaTeX editor, or use Tectonic:

```sh
tectonic main.tex
mv main.pdf systemverilog-review.pdf
```

The PDF was rendered and visually checked for layout. No company-specific material is included.
