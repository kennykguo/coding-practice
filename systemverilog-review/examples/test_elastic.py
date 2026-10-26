from collections import deque
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, FallingEdge, RisingEdge, ReadOnly

@cocotb.test()
async def preserve_order_under_stall(dut):
    dut.rst.value = 1
    dut.in_valid.value = 0
    dut.out_ready.value = 0
    dut.in_data.value = 0
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())
    await ClockCycles(dut.clk, 2)
    await FallingEdge(dut.clk)
    dut.rst.value = 0
    expected = deque()
    source = iter([11, 22, 33, 44])
    pending = next(source, None)
    for cycle in range(40):
        await FallingEdge(dut.clk)
        dut.in_valid.value = int(pending is not None)
        dut.in_data.value = pending if pending is not None else 0
        dut.out_ready.value = int(cycle > 4 and cycle % 4 != 0)
        await ReadOnly()               # settled, before the accepting edge
        if dut.out_valid.value == 1 and dut.out_ready.value == 1:
            assert expected
            assert int(dut.out_data.value) == expected.popleft()
        if pending is not None and dut.in_ready.value == 1:
            expected.append(pending)
            pending = next(source, None)
        await RisingEdge(dut.clk)
        await ReadOnly()               # settled state after the edge
        if pending is None and not expected:
            return
    assert False, "Timed out waiting for all four bytes"
